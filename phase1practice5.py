
import json

print("=== LOGIN AND USER MANAGEMENT SYSTEM ===")
print("1. Register User")
print("2. Login")
print("3. View User")
print("4. Search User")
print("5. Delete User")
print("6. Exit")


def register_user():
    username = input("Setup Username: ").strip()

    if not username.isalnum():
        print("Invalid Username! Example: Ali123")
        return None

    password = input("Setup Password: ")

    if not password.isalnum():
        print("Invalid Password! Use letters and digits only.")
        return None

    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match!")
        return None

    try:
        with open("Register_User.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    for user in users:
        if user["Username"] == username:
            print("Username already exists!")
            return None

    data = {
        "Username": username,
        "Password": password
    }

    users.append(data)

    with open("Register_User.json", "w") as file:
        json.dump(users, file, indent=4)

    print("Registered successfully!")


def user_login():
    user_name = input("Enter Username: ").strip()
    user_password = input("Enter Password: ")

    try:
        with open("Register_User.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("No registered users found!")
        return

    for user in users:
        if user["Username"] == user_name:
            if user["Password"] == user_password:
                print("Login successful!")
            else:
                print("Invalid Password!")
            return

    print("Invalid Username!")


def view_users():
    try:
        with open("Register_User.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("User file not found!")
        return

    if not users:
        print("No users registered yet!")
        return

    for user in users:
        print("--------------------")
        print("Username:", user["Username"])
        print("--------------------")


def search_user():
    user_name = input("Enter Username: ").strip()

    try:
        with open("Register_User.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("User file not found!")
        return

    for user in users:
        if user_name == user["Username"]:
            print("User found!")
            print("Username:", user["Username"])
            return

    print("User not found!")


def delete_user():
    user_name = input("Enter Username to Delete: ").strip()

    try:
        with open("Register_User.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        print("User file not found!")
        return

    for user in users:
        if user["Username"] == user_name:
            users.remove(user)

            with open("Register_User.json", "w") as file:
                json.dump(users, file, indent=4)

            print("User deleted successfully!")
            return

    print("User not found!")


while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        continue

    if choice == 1:
        register_user()
    elif choice == 2:
        user_login()
    elif choice == 3:
        view_users()
    elif choice == 4:
        search_user()
    elif choice == 5:
        delete_user()
    elif choice == 6:
        print("Thanks for using the system!")
        break
    else:
        print("Invalid choice! Enter a number from 1 to 6.")
