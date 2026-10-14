print("==Expene Tracker==")
import json
from datetime import datetime

FILE_NAME = "add_expense.txt"


def add_expense():
    print("\n== Add Expense ==")

    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date! Example: 2026-10-13")

    categories = ["Food", "Transport", "Shopping", "Education", "Bills", "Others"]
    expenses = {}

    for category in categories:
        while True:
            try:
                amount = float(input(f"Enter expense for {category} (Rs.): "))

                if amount < 0:
                    print("Expense cannot be negative.")
                    continue

                expenses[category] = amount
                break

            except ValueError:
                print("Please enter a valid number.")

    record = {
        "Date": date,
        "Expense": expenses,
        "Total Expense": sum(expenses.values())
    }

    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(json.dumps(record) + "\n")

        print("\nExpense saved successfully!")
        print(f"Date: {date}")
        print(f"Total Expense: Rs. {record['Total Expense']:.2f}")

    except OSError as error:
        print(f"Could not save expense: {error}")


def load_expenses():
    records = []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    records.append(json.loads(line))

    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not read expense file: {error}")

    return records


def display_record(record):
    print(f"\nDate: {record['Date']}")
    print("Expenses:")

    for category, amount in record["Expense"].items():
        print(f"  {category}: Rs. {amount:.2f}")

    print(f"Total: Rs. {record['Total Expense']:.2f}")


def view_all_expenses():
    print("\n== All Expenses ==")
    records = load_expenses()

    if not records:
        print("No expenses found.")
        return

    for record in records:
        display_record(record)


def daily_report():
    print("\n== Daily Report ==")
    date = input("Enter date (YYYY-MM-DD): ").strip()
    records = load_expenses()

    daily_records = [
        record for record in records
        if record["Date"] == date
    ]

    if not daily_records:
        print("No expenses found for this date.")
        return

    total = 0

    for record in daily_records:
        display_record(record)
        total += record["Total Expense"]

    print(f"\nTotal spending on {date}: Rs. {total:.2f}")


def monthly_report():
    print("\n== Monthly Report ==")
    month = input("Enter month (YYYY-MM): ").strip()

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month! Example: 2026-10")
        return

    records = load_expenses()

    monthly_records = [
        record for record in records
        if record["Date"].startswith(month)
    ]

    if not monthly_records:
        print("No expenses found for this month.")
        return

    total = 0

    for record in monthly_records:
        display_record(record)
        total += record["Total Expense"]

    print(f"\nTotal spending in {month}: Rs. {total:.2f}")


def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Daily Report")
        print("4. Monthly Report")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_expense()
        elif choice == 2:
            view_all_expenses()
        elif choice == 3:
            daily_report()
        elif choice == 4:
            monthly_report()
        elif choice == 5:
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice! Please select 1 to 5.")


if __name__ == "__main__":
    main()
