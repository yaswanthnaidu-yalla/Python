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
        

if __name__ == "__main__":
    run_demo()

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