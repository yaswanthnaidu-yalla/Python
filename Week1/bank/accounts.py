from utils import logger, timer, retry
import json
from exceptions import InsufficientFundsError, InvalidAmountError
class BankAccount:
    def __init__(self,owner,balance=0.0):
        self.owner = owner
        self.__balance = balance
    def _log_transaction(self,action,amount):
        with open("data/transaction.log","a") as file:
            file.write(f"{self.owner}|{action}|${amount}|New Balance: ${self.balance}\n")
    def save_to_file(self, filename="data/account_data.json"):
        data= {
            "owner":self.owner,
            "balance":self.balance
        }  

        with open(filename, "w") as file:
            json.dump(data,file,indent=4)
        print(f"Account state safely backed up to {filename}")    
    @classmethod
    def from_dict(cls, data):
        return cls(**data)
    @classmethod
    def load_from_file(cls, filename="data/account_data.json"):
        try:
            with open(filename,"r") as file:
                data = json.load(file)
            return cls.from_dict(data)    
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Returning a default account.")
            return cls("unknown",0.0)
    
    
    @staticmethod
    def validate_amount(amount):
        if amount<=0:
            raise InvalidAmountError(amount)
            

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,value):
        self.__balance = value

    @logger

    def deposit(self, amount):
        self.validate_amount(amount)    
        self.__balance += amount
        self._log_transaction("Deposit",amount)
        return self.balance
    
    def batch_deposit(self,*amounts):
        valid_amounts=[amt for amt in amounts if amt>0]
        for amount in valid_amounts:
            self.deposit(amount)
        print(f"Processed{len(valid_amounts)}Valid deposits out of {len(amounts)} attempted")
        return self.balance    

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -=amount
            self._log_transaction("Withdrawl",amount)
            return self.__balance
        else:
            raise InsufficientFundsError(amount, self.balance)
        
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
        
class BaseAccount:
    def get_benefits(self):
        return "Free ATM withdrawals."

class CreditLine(BaseAccount):
    def get_benefits(self):
        return "Borrowing limit of $5000. " + super().get_benefits()

class Rewards(BaseAccount):
    def get_benefits(self):
        return "2% Cash Back. " + super().get_benefits()

class PremiumTravelCard(CreditLine, Rewards):
    def get_benefits(self):
        return "No foreign transaction fees. " + super().get_benefits()    


        






