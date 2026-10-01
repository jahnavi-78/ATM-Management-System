import pytest
from atm.services import ATMService
from atm.storage import Storage

class MockStorage(Storage):
    def __init__(self):
        self.data = {}
        
    def _ensure_file_exists(self):
        pass
        
    def load_all(self):
        return self.data
        
    def save_all(self, accounts):
        self.data = accounts

@pytest.fixture
def atm_service():
    return ATMService(storage=MockStorage())

def test_create_account(atm_service):
    atm_service.create_account("user1", "1234")
    assert "user1" in atm_service.accounts

def test_create_account_invalid_pin(atm_service):
    with pytest.raises(ValueError, match="PIN must be exactly 4 digits"):
        atm_service.create_account("user2", "123")

def test_authenticate(atm_service):
    atm_service.create_account("user1", "1234")
    assert atm_service.authenticate("user1", "1234") is True
    assert atm_service.authenticate("user1", "0000") is False

def test_deposit_and_withdraw(atm_service):
    atm_service.create_account("user1", "1234")
    atm_service.authenticate("user1", "1234")
    
    atm_service.deposit(100.0)
    assert atm_service.get_balance() == 100.0
    
    atm_service.withdraw(40.0)
    assert atm_service.get_balance() == 60.0
    
    with pytest.raises(ValueError, match="Insufficient funds"):
        atm_service.withdraw(100.0)
