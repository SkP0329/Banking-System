import random
from datetime import datetime


# Store all bank accounts
accounts = {}


def generate_account_number():
    """Generate a unique 6-digit account number."""
    while True:
        account_number = random.randint(100000, 999999)

        if account_number not in accounts:
            return account_number


def create_account():
    print("\n========== CREATE ACCOUNT ==========")

    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    pin = input("Create a 4-digit PIN: ")

    if len(pin) != 4 or not pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    account_number = generate_account_number()

    accounts[account_number] = {
        "name": name,
        "phone": phone,
        "pin": pin,
        "balance": 0.0,
        "transactions": []
    }

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)
    print("Please remember your account number and PIN.")


def login():
    print("\n========== LOGIN ==========")

    try:
        account_number = int(input("Enter Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return None

    pin = input("Enter PIN: ")

    if account_number in accounts:
        if accounts[account_number]["pin"] == pin:
            print("\nLogin successful!")
            print("Welcome,", accounts[account_number]["name"])
            return account_number

    print("Invalid Account Number or PIN.")
    return None


def check_balance(account_number):
    balance = accounts[account_number]["balance"]

    print("\n========== ACCOUNT BALANCE ==========")
    print(f"Current Balance: ₹{balance:.2f}")


def deposit(account_number):
    print("\n========== DEPOSIT ==========")

    try:
        amount = float(input("Enter amount to deposit: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    accounts[account_number]["balance"] += amount

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    accounts[account_number]["transactions"].append(
        f"{time} - Deposited ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} deposited successfully.")
    print(f"New Balance: ₹{accounts[account_number]['balance']:.2f}")


def withdraw(account_number):
    print("\n========== WITHDRAW ==========")

    try:
        amount = float(input("Enter amount to withdraw: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    accounts[account_number]["transactions"].append(
        f"{time} - Withdrawn ₹{amount:.2f}"
    )

    print(f"₹{amount:.2f} withdrawn successfully.")
    print(f"Remaining Balance: ₹{accounts[account_number]['balance']:.2f}")


def transfer(account_number):
    print("\n========== TRANSFER MONEY ==========")

    try:
        receiver = int(input("Enter receiver Account Number: "))
    except ValueError:
        print("Invalid account number.")
        return

    if receiver not in accounts:
        print("Receiver account does not exist.")
        return

    if receiver == account_number:
        print("You cannot transfer money to your own account.")
        return

    try:
        amount = float(input("Enter amount to transfer: "))
    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount
    accounts[receiver]["balance"] += amount

    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    accounts[account_number]["transactions"].append(
        f"{time} - Transferred ₹{amount:.2f} to Account {receiver}"
    )

    accounts[receiver]["transactions"].append(
        f"{time} - Received ₹{amount:.2f} from Account {account_number}"
    )

    print("Money transferred successfully.")
    print(f"₹{amount:.2f} transferred to Account {receiver}.")


def transaction_history(account_number):
    print("\n========== TRANSACTION HISTORY ==========")

    transactions = accounts[account_number]["transactions"]

    if not transactions:
        print("No transactions found.")
        return

    for transaction in transactions:
        print(transaction)


def change_pin(account_number):
    print("\n========== CHANGE PIN ==========")

    old_pin = input("Enter old PIN: ")

    if old_pin != accounts[account_number]["pin"]:
        print("Incorrect old PIN.")
        return

    new_pin = input("Enter new 4-digit PIN: ")
    confirm_pin = input("Confirm new PIN: ")

    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must contain exactly 4 digits.")
        return

    if new_pin != confirm_pin:
        print("PINs do not match.")
        return

    accounts[account_number]["pin"] = new_pin

    print("PIN changed successfully.")


def account_menu(account_number):
    while True:
        print("\n================================")
        print("          ACCOUNT MENU")
        print("================================")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Change PIN")
        print("7. Logout")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(account_number)

        elif choice == "2":
            deposit(account_number)

        elif choice == "3":
            withdraw(account_number)

        elif choice == "4":
            transfer(account_number)

        elif choice == "5":
            transaction_history(account_number)

        elif choice == "6":
            change_pin(account_number)

        elif choice == "7":
            print("\nLogged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    while True:
        print("\n================================")
        print("       BANKING SYSTEM")
        print("================================")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            account_number = login()

            if account_number is not None:
                account_menu(account_number)

        elif choice == "3":
            print("\nThank you for using the Banking System.")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
