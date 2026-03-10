from accounts import PremiumTravelCard
from models import Transaction
from payments import PaymentProcessor, UPIProcessor, RazorpayProcessor
import sys
from utils import transaction_history
from accounts import  BankAccount, SavingsAccount, CurrentAccount
from exceptions import InsufficientFundsError, InvalidAmountError 
def run_demo():
    stevon=BankAccount("Stevon",100.0)
    stevon.deposit(400)
    stevon.save_to_file("stevon_save.json")

    stevon_clone = BankAccount.load_from_file("stevon_save.json")
    print(f"Loaded from JSON: {stevon_clone}")

    print("\n--- Testing *args in Batch Processing---")
    stevon.batch_deposit(100, -50, 200, 0, 300)
def run_demo2():
    api_data = {"owner":"Alice","balance":1500.0}

    account_from_api = BankAccount.from_dict(api_data)
    print("created with class method:", account_from_api)

    print("\nAttempting a deposit")
    try:
        account_from_api.deposit(500)
    except InvalidAmountError as e:
        print(f"Alert: {e}")
    except InsufficientFundsError as e:
        print(f"Alert:{e}")
    else:
        print("Transaction successful")
        print(f"New Balance: {account_from_api.get_balance()}")
    finally:
        print("End of transaction")        
        


def run_demo3():
    print("\n---Reading Logs with Generator---")
    log_reader=transaction_history()    
    
    print("First transaction:", next(log_reader))
    print("Second transaction:", next(log_reader))
    
    
    print("Remaining transactions:")
    for transaction in log_reader:
        print(transaction)
           
    print("\n---Memory usage comparison---")
    massive_list = [x for x in range(1000000)]
    massive_generator = (x for x in range(1000000))
    
    print(f"List Memory:{sys.getsizeof(massive_list):,} bytes")
    print(f"Generator Memory:{sys.getsizeof(massive_generator):,} bytes")

def sorting():
    print("\n~~~Lambda and Functional ways used to sort~~~")

    stevon_mom = BankAccount("Stevon_Mom", 500)
    Alice_Dad = BankAccount("Alice_Dad", 1500)
    Stalice = BankAccount("Stalice", 50)
    bank_database = [stevon_mom, Alice_Dad,Stalice]

    bank_database.sort(key=lambda acc: acc.balance, reverse=True)
    print(f"Sorted Bank: {bank_database}")

    balance_comp = [acc.balance for acc in bank_database]
    print(f"Balances:{balance_comp}")

    vip_comp=[acc for acc in bank_database if acc.balance > 1000]
    print(f"VIP Clients: {vip_comp}")

def payments():
    print("\n--- Testing Abstract Base Classes ---")
    upi = UPIProcessor()

    upi.process_payment(500)
    
    razorpay = RazorpayProcessor()

    razorpay.process_payment(1200)

    print("\nAttempting to create a generic PaymentProcessor...")

    try:

        generic = PaymentProcessor()

    except TypeError as e:

        print(f" SUCCESSFUL CRASH: {e}")

def dataclasses():
    print("\n--- Testing Dataclasses ---") 

    txn1 = Transaction(txn_id="UPI_9982", amount=500.0, processor="GPay")    



    print(txn1)    

    

    print("\nAttempting to modify a frozen transaction...")

    try:

        txn1.amount = 9000.0 

    except Exception as e:

        print(f" SUCCESSFUL CRASH: {type(e).__name__} - {e}")

def multiple_inheritence():
    print("\n--- Testing Multiple Inheritance & MRO ---")
    print("The MRO Tuple:")
    for i, cls in enumerate(PremiumTravelCard.__mro__):
       print(f"  {i}. {cls.__name__}")
            
    print("\n--- Running the Cooperative Method ---")
       
    my_card = PremiumTravelCard()
    print(my_card.get_benefits())


if __name__ == "__main__":
    multiple_inheritence()