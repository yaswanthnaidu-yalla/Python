from abc import ABC, abstractmethod
from utils import retry

class PaymentProcessor(ABC):
    def validate_amount(self,amount):
        if amount<=0:
            raise ValueError("Amount must be positive")
        print(f"Amount ${amount} validated.")
        return True
    
    @abstractmethod
    def process_payment(self, amount):
        pass
    @abstractmethod
    def refund(self, transaction_id):
        pass
    @abstractmethod
    def get_status(self, transaction_id):
        pass


class UPIProcessor(PaymentProcessor):    
    @retry(max_attempts=3)
    def process_payment(self, amount):

        self.validate_amount(amount) 

        print(f" Processing ${amount} via UPI (GPay/PhonePe)...")

        return f"UPI_TXN_{amount}"



    def refund(self, transaction_id):

        print(f" Refunding UPI transaction: {transaction_id}")



    def get_status(self, transaction_id):

        return "SUCCESS"



class RazorpayProcessor(PaymentProcessor):

    def process_payment(self, amount):

        self.validate_amount(amount)

        print(f" Processing ${amount} via Razorpay Credit Card Gateway...")

        return f"RZP_TXN_{amount}"



    def refund(self, transaction_id):

        print(f" Refunding Razorpay transaction: {transaction_id}")



    def get_status(self, transaction_id):

        return "PENDING"