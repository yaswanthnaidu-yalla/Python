from dataclasses import dataclass, field

from datetime import datetime

@dataclass(frozen=True)

class Transaction:

    txn_id: str

    amount: float

    processor: str

    

    timestamp: datetime = field(default_factory=datetime.now)

    def __post_init__(self):

        if self.amount <= 0:

            raise ValueError(f"Invalid transaction amount: {self.amount}")