import json
import os
import getpass

DATA_FILE = 'users.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def create_account():
    data = load_data()
    print("\n--- Create Account ---")
    username = input("Enter a username: ").strip()
    if username in data:
        print("Username already exists! Please try logging in or use a different username.")
        return

    pin = getpass.getpass("Enter a 4-digit PIN: ").strip()
    if not pin.isdigit() or len(pin) != 4:
        print("Invalid PIN. It must be exactly 4 digits.")
        return

    data[username] = {
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }
    save_data(data)
    print(f"Account for {username} created successfully!")

def login():
    data = load_data()
    print("\n--- Login ---")
    username = input("Enter username: ").strip()
    if username not in data:
        print("Username not found.")
        return None

    pin = getpass.getpass("Enter PIN: ").strip()
    if data[username]["pin"] == pin:
        print("Login successful!")
        return username
    else:
        print("Incorrect PIN.")
        return None

def check_balance(username, data):
    balance = data[username]["balance"]
    print(f"\nCurrent Balance: ${balance:.2f}")

def deposit(username, data):
    try:
        amount = float(input("Enter amount to deposit: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
        data[username]["balance"] += amount
        data[username]["transactions"].append(f"Deposited ${amount:.2f}")
        save_data(data)
        print(f"${amount:.2f} deposited successfully.")
    except ValueError:
        print("Invalid amount entered.")

def withdraw(username, data):
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
        if amount > data[username]["balance"]:
            print("Insufficient funds!")
            return
        
        data[username]["balance"] -= amount
        data[username]["transactions"].append(f"Withdrew ${amount:.2f}")
        save_data(data)
        print(f"${amount:.2f} withdrawn successfully.")
    except ValueError:
        print("Invalid amount entered.")

def transaction_history(username, data):
    transactions = data[username]["transactions"]
    print("\n--- Transaction History ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print("-", t)

def atm_menu(username):
    while True:
        data = load_data()
        print(f"\n=== Welcome, {username} ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == '1':
            check_balance(username, data)
        elif choice == '2':
            deposit(username, data)
        elif choice == '3':
            withdraw(username, data)
        elif choice == '4':
            transaction_history(username, data)
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    while True:
        print("\n=== ATM Management System ===")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == '1':
            user = login()
            if user:
                atm_menu(user)
        elif choice == '2':
            create_account()
        elif choice == '3':
            print("Thank you for using the ATM Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
