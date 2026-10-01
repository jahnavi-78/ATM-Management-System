import json
import os
from .models import Account

class Storage:
    def __init__(self, filepath='data/users.json'):
        self.filepath = filepath
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                json.dump({}, f)

    def load_all(self):
        with open(self.filepath, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
        return {k: Account.from_dict(v) for k, v in data.items()}

    def save_all(self, accounts):
        with open(self.filepath, 'w') as f:
            json.dump({k: v.to_dict() for k, v in accounts.items()}, f, indent=4)
