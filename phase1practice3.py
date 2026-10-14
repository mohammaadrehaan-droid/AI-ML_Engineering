
import json

def create_account():
    name = input("Enter your name: ").strip()
    account_number = int(input("Enter account number: "))
    balance = int(input("Enter initial deposit: "))

    customer = {
        "Name": name,
        "Account Number": account_number,
        "Balance": balance,
        "History": [balance]
    }

    with open("bank.json", "w") as f:
        json.dump(customer, f, indent=4)

    print("Account created successfully!")


def deposit_money():
    with open("bank.json", "r") as f:
        customer = json.load(f)

    amount = int(input("Enter deposit amount: "))

    if amount > 0:
        customer["Balance"] += amount
        customer["History"].append(amount)

        with open("bank.json", "w") as f:
            json.dump(customer, f, indent=4)

        print("Deposit successful!")
        print("New balance:", customer["Balance"])
    else:
        print("Enter a positive amount!")


def transaction_history():
    with open("bank.json", "r") as f:
        customer = json.load(f)

    print("Transaction History:")
    print(customer["History"])


def view_details():
    account_number = int(input("Enter your account number: "))

    with open("bank.json", "r") as f:
        customer = json.load(f)

    if customer["Account Number"] == account_number:
        print("Name:", customer["Name"])
        print("Account Number:", customer["Account Number"])
        print("Balance:", customer["Balance"])
    else:
        print("Account not found!")


while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Transaction History")
    print("4. View Account Details")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_account()

        elif choice == 2:
            deposit_money()

        elif choice == 3:
            transaction_history()

        elif choice == 4:
            view_details()

        elif choice == 5:
            print("Thanks for using this app!")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
