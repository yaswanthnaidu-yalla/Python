class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.message=f"Can't Withdraw {amount}. Current Balance is only{balance}"
        super().__init__(self.message)

class InvalidAmountError(Exception):
    def __init__(self, amount):
        self.message = f"Invalid amount:{amount}. Amount must be greater than zero."
        super().__init__(self.message)
class AccountNotFoundError(Exception):
    def __init__(self, account_id):
        self.message= f"Account with ID '{account_id}'was not found."
        super().__init__(self.message)
