import getpass
from .services import ATMService

class ATMCLI:
    def __init__(self, service: ATMService):
        self.service = service

    def run(self):
        while True:
            print("\n=== Professional ATM System ===")
            print("1. Login")
            print("2. Create Account")
            print("3. Exit")
            choice = input("Select an option: ").strip()

            try:
                if choice == '1':
                    self._login()
                elif choice == '2':
                    self._create_account()
                elif choice == '3':
                    print("Thank you for using the Professional ATM System. Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except Exception as e:
                print(f"System Error: {str(e)}")

    def _create_account(self):
        print("\n--- Create Account ---")
        account_id = input("Enter Account ID (Username): ").strip()
        pin = getpass.getpass("Enter a 4-digit PIN: ").strip()
        try:
            self.service.create_account(account_id, pin)
            print("Account created successfully!")
        except ValueError as e:
            print(f"Error: {str(e)}")

    def _login(self):
        print("\n--- Login ---")
        account_id = input("Account ID: ").strip()
        pin = getpass.getpass("PIN: ").strip()
        if self.service.authenticate(account_id, pin):
            print("Login successful!")
            self._account_menu()
        else:
            print("Error: Invalid Account ID or PIN.")

    def _account_menu(self):
        while True:
            print(f"\n--- Account Menu ({self.service.current_user.account_id}) ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Logout")
            choice = input("Select an option: ").strip()

            try:
                if choice == '1':
                    print(f"Current Balance: ${self.service.get_balance():.2f}")
                elif choice == '2':
                    amount = float(input("Amount to deposit: $"))
                    self.service.deposit(amount)
                    print(f"Deposit of ${amount:.2f} successful.")
                elif choice == '3':
                    amount = float(input("Amount to withdraw: $"))
                    self.service.withdraw(amount)
                    print(f"Withdrawal of ${amount:.2f} successful.")
                elif choice == '4':
                    history = self.service.get_transaction_history()
                    print("\nTransaction History:")
                    if not history:
                        print("No transactions found.")
                    else:
                        for t in history:
                            print(f"{t.timestamp} | {t.transaction_type} | ${t.amount:.2f}")
                elif choice == '5':
                    self.service.logout()
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid option.")
            except ValueError as e:
                if "could not convert string to float" in str(e).lower():
                    print("Input Error: Please enter a valid number.")
                else:
                    print(f"Input Error: {str(e)}")
            except PermissionError as e:
                print(f"Access Denied: {str(e)}")
                break
            except Exception as e:
                print(f"Unexpected Error: {str(e)}")
