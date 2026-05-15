import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


# Add new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

    if date == "":
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Enter category (Food/Travel/Shopping/Bills/etc): ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter numbers only.")
        return

    description = input("Enter short description: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!\n")


# View all expenses
def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) <= 1:
            print("No expenses found.\n")
            return

        print("\n--- All Expenses ---")
        for row in rows:
            print(row)
        print()


# Monthly summary
def monthly_summary():
    month = input("Enter month (YYYY-MM): ")
    total = 0
    category_summary = {}

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Date"].startswith(month):
                amount = float(row["Amount"])
                total += amount

                category = row["Category"]

                if category in category_summary:
                    category_summary[category] += amount
                else:
                    category_summary[category] = amount

    print(f"\nTotal Spending for {month}: ₹{total}")

    if total == 0:
        print("No expenses found for this month.\n")
        return

    print("\nCategory-wise Spending:")
    for category, amount in category_summary.items():
        print(f"{category}: ₹{amount}")

    highest_category = max(category_summary, key=category_summary.get)
    print(f"\nHighest Spending Category: {highest_category}")
    print()


# Main menu
def menu():
    create_file()

    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            monthly_summary()

        elif choice == "4":
            print("Exiting program. Thank you!")
            break

        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    menu()