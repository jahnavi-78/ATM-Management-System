import os
from atm.storage import Storage
from atm.services import ATMService
from atm.cli import ATMCLI

def main():
    # Setup data directory securely based on file location
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'users.json')
    
    # Initialize application layers via dependency injection
    storage = Storage(filepath=data_path)
    service = ATMService(storage=storage)
    cli = ATMCLI(service=service)
    
    # Start the application
    cli.run()

if __name__ == "__main__":
    main()
