import os
import csv
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

FILENAME = 'expenses.csv'

# Step 1: Make sure the CSV file exists and has headers
def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass  # If the file already exists, do nothing

# Step 2: Add a new expense to the CSV
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    category = input("Enter category (e.g., food, transport): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    note = input("Enter a note (optional): ")

    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    
    print("✅ Expense added successfully!")

# addition: added a new view expenses
def view_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found yet.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader) 

    if len(rows) <= 1:
        print("No expenses to show.")
        return

    print("\n=== All Expenses ===")
    print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Note'}")
    print("-" * 50)

    for row in rows[1:]:  
        if len(row) < 4:
            continue  # Skip any incomplete rows
        date, category, amount, note = row
        print(f"{date:<12} {category:<15} {amount:<10} {note}")

# addition: this will let you filter expenses
def filter_expenses():
    if not os.path.exists(FILENAME):
        print("No expenses found yet.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses to filter.")
        return

    print("\nFilter by:")
    print("1. Category")
    print("2. Date")
    choice = input("Enter your choice (1–2): ")

    if choice == '1':
        keyword = input("Enter category to filter by: ").lower()
        filtered = [row for row in rows[1:] if row[1].strip().lower() == keyword.strip().lower()]
    elif choice == '2':
        keyword = input("Enter date to filter by (YYYY-MM-DD): ")
        filtered = [row for row in rows[1:] if row[0].strip() == keyword.strip()]
    else:
        print("Invalid choice.")
        return

    if not filtered:
        print("No matching expenses found.")
        return

    print("\n=== Filtered Expenses ===")
    print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Note'}")
    print("-" * 50)

    for row in filtered:
        date, category, amount, note = row
        print(f"{date:<12} {category:<15} {amount:<10} {note}")

# addition: it show the total spending
def show_total_spending():
    if not os.path.exists(FILENAME):
        print("No expenses found yet.")
        return

    with open(FILENAME, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        print("No expenses to calculate.")
        return

    print("\nCalculate total spending:")
    print("1. Overall total")
    print("2. By category")
    print("3. By date")
    choice = input("Enter your choice (1–3): ")

    if choice == '1':
        total = sum(float(row[2]) for row in rows[1:])
        print(f"\n Total Spending: ₹{total:.2f}")

    elif choice == '2':
        category_totals = {}
        for row in rows[1:]:
            category = row[1].strip().lower()
            amount = float(row[2])
            category_totals[category] = category_totals.get(category, 0) + amount

        print("\n=== Spending by Category ===")
        for category, total in category_totals.items():
            print(f"{category.title()}: ₹{total:.2f}")

    elif choice == '3':
        date_totals = {}
        for row in rows[1:]:
            date = row[0].strip()
            amount = float(row[2])
            date_totals[date] = date_totals.get(date, 0) + amount

        print("\n=== Spending by Date ===")
        for date, total in date_totals.items():
            print(f"{date}: ₹{total:.2f}")

    else:
        print("Invalid choice.")

# Step 3: Main menu loop
def main():
    initialize_file()

    while True:
        clear_screen() # clears terminal at the start of every loop 

        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses")
        print("4. Show Total Spending")
        print("5. Quit")

        choice = input("Enter your choice (1–2): ")

        if choice == '1':
            add_expense()
            input("\nPress Enter to return to menu...")
        elif choice == '2':
            view_expenses()
            input("\nPress Enter to return to menu...")
        elif choice == '3':
            filter_expenses()
            input("\nPress Enter to return to menu...")
        elif choice == '4':
            show_total_spending()
            input("\nPress Enter to return to menu...")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()