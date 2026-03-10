
class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.__balance = balance
    @classmethod
    def from_dict(cls, data):
        owner_name=data.get("owner","unknown")
        starting_balance=data.get("balance",0.0)
        return cls(owner_name,starting_balance)
    
    @staticmethod
    def validate_amount(amount):
        if amount>0:
            return True
        else:
            print(f"Error:{amount} is not a valid amount. Must be greater than zero")
            return False

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        self.__balance = value

    def deposit(self, amount):
        if self.validate_amount(amount):    
            self.__balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -=amount
            return self.__balance
        else:
            return "insufficient balance"
        
    def get_balance(self):
        return self.balance
    
    def __repr__(self):
        return f"BankAccount(name={self.owner},balance={self.balance})"
    
    def __str__(self):
        return f"{self.owner}, worth {self.balance}"
    
class SavingsAccount(BankAccount):
    def apply_interest(self,rate,time):
        if(self.balance>0):
            interest_earned = self.balance*rate*time
            self.balance+=interest_earned
            print(f"Interest earned:{interest_earned}")
            print(f"New Balance:{self.balance}")
            return self.balance
        else:
            return "no interest applied"
      
class CurrentAccount(BankAccount):
    def withdraw_credit(self,amount,overdraft_limit):
        if(amount<=overdraft_limit):
            self.balance-= amount
            print(f"debited:{amount}")
            print(f"remnant limit:{overdraft_limit-amount}")
            return self.balance
        else:
            return "limit exceeded"
        
    


        






def run_demo():
    acc = BankAccount('Bobby',100.0)
    print(acc)
    print(repr(acc))
    print(f"Depositing $500.. New Balance: {acc.deposit(500)}")
    print(f"Withdrawing $100.. New Balance{acc.withdraw(100)}")
    print(f"Current Balance: {acc.get_balance()}")

    savings=SavingsAccount("Bobby",500.0)
    savings.deposit(200)
    savings.apply_interest(0.05,2)
    
    current=CurrentAccount("Bobby",300)
    print("withdraw 900")
    current.withdraw_credit(900,1000)
def run_demo2():
    api_data = {"owner":"Alice","balance":1500.0}

    account_from_api = BankAccount.from_dict(api_data)
    print("created with class method:", account_from_api)

    print("\nAttempting a negative deposit")

    account_from_api.deposit(-50)
    print("balance after bad deposit:",account_from_api.get_balance())    

if __name__ == "__main__":
    run_demo2()    



    