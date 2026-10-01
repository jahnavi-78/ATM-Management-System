from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class Transaction:
    transaction_type: str
    amount: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self):
        return {
            "transaction_type": self.transaction_type,
            "amount": self.amount,
            "timestamp": self.timestamp
        }

@dataclass
class Account:
    account_id: str
    pin_hash: str
    balance: float = 0.0
    transactions: List[Transaction] = field(default_factory=list)

    def to_dict(self):
        return {
            "account_id": self.account_id,
            "pin_hash": self.pin_hash,
            "balance": self.balance,
            "transactions": [t.to_dict() for t in self.transactions]
        }

    @classmethod
    def from_dict(cls, data):
        transactions = [Transaction(**t) for t in data.get('transactions', [])]
        return cls(
            account_id=data['account_id'],
            pin_hash=data['pin_hash'],
            balance=data.get('balance', 0.0),
            transactions=transactions
        )
