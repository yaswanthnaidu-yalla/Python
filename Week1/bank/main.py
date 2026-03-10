import os
from payments import  UPIProcessor, RazorpayProcessor
from accounts import  BankAccount, SavingsAccount, CurrentAccount



def setup():
    """Ensure the environment is ready."""
    if not os.path.exists("data"):
        os.makedirs("data")
        print("| System: Created missing 'data/' directory.")
def get_save_path(name):
    return f"data/{name.lower()}_save.json"
def get_account():
    print("\n--- Banking System ---")
    print("1. Create New Account")
    print("2. Load Existing Account")
    entry_choice = input("Selection: ")

    if entry_choice == "2":
        name = input("Enter account holder name: ")
        path = get_save_path(name)
        print(f"looking for: {path}")
        if not os.path.exists(path):
            print(f"No saved account found for '{name}'.")
            return get_account()
        return BankAccount.load_from_file(filename=path)

    print("\n--- Select Account Type ---")
    print("1. Basic | 2. Savings | 3. Current")
    type_choice = input("Selection: ")
    name = input("Enter owner name: ")
    initial_deposit = float(input("Initial Deposit: "))

    match type_choice:
        case "2":
            return SavingsAccount(name, initial_deposit)
        case "3":
            return CurrentAccount(name, initial_deposit)
        case _:
            return BankAccount(name, initial_deposit)

def cli_menu():
    setup()
    account = get_account()
    processors = {"1": UPIProcessor(), "2": RazorpayProcessor()}

    while True:
        print(f"\n| User: {account.owner} | Balance: ${account.balance:.2f} |")
        print("-" * 40)
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Apply Interest")
        print("4. Process Payment")
        print("5. View History")
        print("6. Save and Exit")
        
        choice = input("Action: ")

        try:
            match choice:
                case "1":
                    amount = float(input("Amount: "))
                    account.deposit(amount)
                
                case "2":
                    amount = float(input("Amount: "))
                    account.withdraw(amount)
                
                case "3":
                    if isinstance(account, SavingsAccount):
                        earned = account.apply_interest(rate=0.05,time=1)
                        print(f"Interest Earned: ${earned:.2f}")
                    else:
                        print("Error: Interest only available for Savings Accounts")
                
                case "4":
                    print("1. UPI | 2. Razorpay")
                    gate = input("Gateway: ")
                    if gate in processors:
                        amt = float(input("Amount: "))
                        txn_id = processors[gate].process_payment(amt)
                        account.withdraw(amt)
                        print(f"Success. Transaction ID: {txn_id}")
                    else:
                        print("Invalid Gateway")

                case "5":
                    from utils import transaction_history
                    print("\n--- Transaction Log ---")
                    found = False
                    for entry in transaction_history():
                        if account.owner in entry:
                            print(entry)
                            found = True
                    if not found:
                        print("No transactions found on this account")        

                case "6":
                    path = get_save_path(account.owner)
                    account.save_to_file(filename=path)
                    print("Account saved. Session ended.")
                    return

                case _:
                    print("Invalid input")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    cli_menu()