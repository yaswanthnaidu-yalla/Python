#attributes - owner,balance
#methods - deposit, withdraw,getbalance
#add str and repr dunder methods.
class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -=amount
            return self.balance
        else:
            return "insufficient balance"
    def get_balance(self):
        return self.balance
    def __repr__(self):
        return f"BankAccount(name={self.owner},balance={self.balance})"
    
    def __str__(self):
        return f"{self.owner}, worth {self.balance}"

def run_demo():
    acc = BankAccount('Bobby',100.0)

    print(acc)
    print(repr(acc))

    print(f"Depositing $500.. New Balance: {acc.deposit(500)}")

    print(f"Withdrawing $300.. New Balance{acc.withdraw(300)}")

    print(f"Current Balance: {acc.get_balance()}")

    

if __name__ == "__main__":
    run_demo()    



    