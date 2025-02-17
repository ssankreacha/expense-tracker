import csv
import datetime
import os
import matplotlib.pyplot as plt

# File to store expenses
EXPENSE_FILE = "expenses.csv"

# Categories for expenses
CATEGORIES = ["Food", "Rent", "Utilities", "Entertainment", "Transport", "Others"]

# Budget limit
MONTHLY_BUDGET = 1000  # Example budget in dollars


def initialize_file():
    """Create the CSV file if it doesn't exist."""
    if not os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Description"])


def add_expense():
    """Add a new expense to the file."""
    amount = float(input("Enter expense amount: $"))
    print("Categories: ", ", ".join(CATEGORIES))
    category = input("Enter category: ").capitalize()

    if category not in CATEGORIES:
        print("Invalid category! Adding under 'Others'.")
        category = "Others"

    description = input("Enter description: ")
    date = datetime.date.today().strftime("%Y-%m-%d")

    # Save the expense to the file
    with open(EXPENSE_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("✅ Expense added successfully!")

    check_budget_limit()


def view_expenses():
    """Display all expenses from the file."""
    print("\n📋 Expense History:")
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            print(f"📅 {row[0]} | 💰 ${row[1]} | 📂 {row[2]} | ✏️ {row[3]}")


def filter_expenses():
    """Filter expenses by category or date."""
    choice = input("Filter by (1) Category or (2) Date? ")

    if choice == "1":
        category = input("Enter category: ").capitalize()
        print(f"\n📂 Expenses in {category}:")
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[2] == category:
                    print(f"📅 {row[0]} | 💰 ${row[1]} | ✏️ {row[3]}")

    elif choice == "2":
        date = input("Enter date (YYYY-MM-DD): ")
        print(f"\n📅 Expenses on {date}:")
        with open(EXPENSE_FILE, "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if row[0] == date:
                    print(f"💰 ${row[1]} | 📂 {row[2]} | ✏️ {row[3]}")
    else:
        print("Invalid choice!")


def check_budget_limit():
    """Check if total spending exceeds the monthly budget."""
    total_spent = 0
    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            total_spent += float(row[1])

    if total_spent > MONTHLY_BUDGET:
        print(f"⚠️ Warning! You have exceeded your monthly budget of ${MONTHLY_BUDGET}.")
    else:
        print(f"📊 Current spending: ${total_spent} / ${MONTHLY_BUDGET}")


def generate_spending_chart():
    """Generate a pie chart showing expense distribution by category."""
    categories = {}

    with open(EXPENSE_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            category = row[2]
            amount = float(row[1])
            categories[category] = categories.get(category, 0) + amount

    if not categories:
        print("No data available for chart.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(categories.values(), labels=categories.keys(), autopct="%1.1f%%", startangle=90)
    plt.title("Expense Distribution by Category")
    plt.show()


def export_to_csv():
    """Export expenses to CSV format."""
    print(f"✅ Expenses saved to `{EXPENSE_FILE}` successfully!")


def main():
    """Main function to run the Expense Tracker."""
    initialize_file()

    while True:
        print("\n💰 EXPENSE TRACKER MENU 💰")
        print("1️⃣ Add Expense")
        print("2️⃣ View Expenses")
        print("3️⃣ Filter Expenses")
        print("4️⃣ Check Budget")
        print("5️⃣ Generate Spending Chart")
        print("6️⃣ Export Data to CSV")
        print("7️⃣ Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            filter_expenses()
        elif choice == "4":
            check_budget_limit()
        elif choice == "5":
            generate_spending_chart()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
