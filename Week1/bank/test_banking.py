import pytest
import os
from accounts import BankAccount, SavingsAccount
from exceptions import InsufficientFundsError,InvalidAmountError
from models import Transaction
from dataclasses import FrozenInstanceError

def test_initial_balance():
    acc = BankAccount("Test", 100)
    assert acc.balance == 100

def test_insufficient_funds():
    acc = BankAccount("Test", 50)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(100)
def test_deposit_increases_balance():
    acc = BankAccount("Steve", 100)
    acc.deposit(50)
    assert acc.balance == 150

def test_invalid_deposit_raises_error():
    acc = BankAccount("Steve", 100)
    with pytest.raises(InvalidAmountError):
        acc.deposit(-50)
    with pytest.raises(InvalidAmountError):
        acc.deposit(0)

def test_batch_deposit_filters_invalid():
    acc = BankAccount("Steve", 100)
    # batch_deposit should only process 100 and 200
    acc.batch_deposit(100, -50, 200, 0)
    assert acc.balance == 400 

def test_savings_interest_calculation():
    sav = SavingsAccount("Alice", 1000)
    sav.apply_interest(rate=0.05, time=1)
    assert sav.balance == 1050.0

def test_transaction_is_frozen():
    txn = Transaction(txn_id="TXN123", amount=100.0, processor="UPI")
    with pytest.raises(FrozenInstanceError):
        txn.amount = 200.0
def test_account_type_persistence():



    sav = SavingsAccount("Alice", 100)

    basic = BankAccount("Bob", 100)

    assert hasattr(sav, 'apply_interest')

    assert not hasattr(basic, 'apply_interest')



def test_json_save_load(tmp_path):

    

    os.chdir(tmp_path)

    os.makedirs("data")

    acc = BankAccount("Steve", 500)

    acc.save_to_file()

    

    assert os.path.exists(f"data/account_data.json")