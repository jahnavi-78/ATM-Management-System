import hashlib
from .models import Account, Transaction
from .storage import Storage

class ATMService:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.accounts = self.storage.load_all()
        self.current_user = None

    def _hash_pin(self, pin: str) -> str:
        """Securely hashes the PIN for storage."""
        return hashlib.sha256(pin.encode()).hexdigest()

    def create_account(self, account_id: str, pin: str) -> bool:
        if account_id in self.accounts:
            raise ValueError("Account already exists.")
        if not pin.isdigit() or len(pin) != 4:
            raise ValueError("PIN must be exactly 4 digits.")
        
        new_account = Account(account_id=account_id, pin_hash=self._hash_pin(pin))
        self.accounts[account_id] = new_account
        self.storage.save_all(self.accounts)
        return True

    def authenticate(self, account_id: str, pin: str) -> bool:
        account = self.accounts.get(account_id)
        if account and account.pin_hash == self._hash_pin(pin):
            self.current_user = account
            return True
        return False
        
    def logout(self):
        self.current_user = None

    def get_balance(self) -> float:
        self._require_auth()
        return self.current_user.balance

    def deposit(self, amount: float):
        self._require_auth()
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.current_user.balance += amount
        self.current_user.transactions.append(Transaction("DEPOSIT", amount))
        self.storage.save_all(self.accounts)

    def withdraw(self, amount: float):
        self._require_auth()
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.current_user.balance:
            raise ValueError("Insufficient funds.")
        
        self.current_user.balance -= amount
        self.current_user.transactions.append(Transaction("WITHDRAWAL", amount))
        self.storage.save_all(self.accounts)

    def get_transaction_history(self):
        self._require_auth()
        return self.current_user.transactions

    def _require_auth(self):
        if not self.current_user:
            raise PermissionError("User is not authenticated.")
