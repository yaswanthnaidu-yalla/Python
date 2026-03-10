# Bank — Python OOP Learning Project

A command-line banking simulation built as a practical exercise in core Python concepts. The project covers object-oriented programming, decorators, abstract base classes, dataclasses, generators, multiple inheritance, and persistence — all applied to a realistic banking domain.

---

## Project Structure

```
bank/
├── accounts.py       # Account classes and inheritance hierarchy
├── exceptions.py     # Custom exception types
├── models.py         # Frozen dataclass for transactions
├── payments.py       # Abstract payment processor and concrete implementations
├── utils.py          # Decorators and a transaction log generator
├── main.py           # CLI menu and entry point
├── test_banking.py   # pytest test suite
├── requirements.txt  # Project dependencies
└── data/             # Auto-generated at runtime
    ├── {name}_save.json    # Persisted account state per user
    └── transaction.log     # Append-only transaction log
```

---

## Running the Project

```bash
python main.py
```

On first run, the `data/` directory is created automatically. You will be prompted to create a new account or load an existing one.

### CLI Options

| Option | Description |
|---|---|
| 1. Deposit | Add funds to the account |
| 2. Withdraw | Remove funds, raises error if insufficient |
| 3. Apply Interest | Savings accounts only — applies 5% annual interest |
| 4. Process Payment | Pay via UPI or Razorpay gateway |
| 5. View History | Filters transaction log for the current user |
| 6. Save and Exit | Persists account state to `data/{name}_save.json` |

### Running Tests

```bash
python -m pytest test_banking.py -v
```

---

## Concepts Demonstrated

### Object-Oriented Programming (`accounts.py`)
- **Encapsulation** — account balance is a private attribute exposed via a `@property` with a controlled setter
- **Inheritance** — `SavingsAccount` and `CurrentAccount` extend `BankAccount`
- **Multiple Inheritance & MRO** — `PremiumTravelCard` inherits from both `CreditLine` and `Rewards`, demonstrating Python's Method Resolution Order with cooperative `super()` calls
- **Class methods** — `from_dict()` and `load_from_file()` serve as alternative constructors
- **Static methods** — `validate_amount()` as shared validation logic that requires no instance state
- **`*args`** — `batch_deposit()` accepts a variable number of amounts and silently filters out invalid ones

### Custom Exceptions (`exceptions.py`)
Three domain-specific exceptions with descriptive messages:
- `InsufficientFundsError` — raised when a withdrawal exceeds the available balance
- `InvalidAmountError` — raised when a zero or negative amount is provided
- `AccountNotFoundError` — raised when looking up a non-existent account

### Dataclasses (`models.py`)
- `Transaction` is a `frozen=True` dataclass, making instances immutable after creation
- A `__post_init__` guard rejects non-positive transaction amounts
- Timestamp defaults to creation time via `field(default_factory=datetime.now)`

### Abstract Base Classes (`payments.py`)
- `PaymentProcessor` is an ABC that cannot be instantiated directly
- `UPIProcessor` and `RazorpayProcessor` implement `process_payment()`, `refund()`, and `get_status()`
- Shared validation logic lives in the base class and is reused by both subclasses
- `@retry(max_attempts=3)` is applied to `UPIProcessor.process_payment()` to demonstrate resilience handling

### Decorators & Generators (`utils.py`)
- `@logger` — logs the function name, arguments, and return value around every call
- `@timer` — measures and prints execution time for any wrapped function
- `@retry(max_attempts=n)` — a parameterised decorator that retries a failing function up to `n` times before re-raising the exception
- `transaction_history()` — a generator that lazily reads the transaction log line by line, avoiding loading the entire file into memory at once

### Persistence
- `save_to_file()` serialises account state to a named JSON file (`data/{name}_save.json`)
- `load_from_file()` deserialises it back on the next session
- Every deposit and withdrawal is appended to `data/transaction.log`
- The `data/` directory is created automatically if it does not exist

---

## Test Coverage

9 tests covering the core domain logic:

| Test | What it verifies |
|---|---|
| `test_initial_balance` | Account initialises with the correct balance |
| `test_deposit_increases_balance` | Valid deposit updates balance correctly |
| `test_invalid_deposit_raises_error` | Zero and negative deposits raise `InvalidAmountError` |
| `test_insufficient_funds` | Withdrawal beyond balance raises `InsufficientFundsError` |
| `test_batch_deposit_filters_invalid` | Only valid amounts from a batch are applied |
| `test_savings_interest_calculation` | Interest is computed and applied correctly |
| `test_transaction_is_frozen` | Modifying a `Transaction` field raises `FrozenInstanceError` |
| `test_account_type_persistence` | Subclass-specific methods are only present on the correct type |
| `test_json_save_load` | Account state is correctly written to disk |

---

## Requirements

- Python 3.10 or higher (for `match` statement support)
- pytest (see `requirements.txt`)

```bash
pip install -r requirements.txt
```
[← Back to Python Progress](../../README.md)
