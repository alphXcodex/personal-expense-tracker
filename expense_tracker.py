import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(__file__).with_name("expenses.json")
DATE_FORMAT = "%Y-%m-%d"


def load_expenses():
    """Load saved expenses from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
        print("Warning: expenses.json is not in the expected format. Starting with an empty list.")
        return []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read expenses.json. Starting with an empty list.")
        return []


def save_expenses(expenses):
    """Save expenses so they remain available after the program closes."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def ask_amount():
    """Ask for a positive numeric expense amount."""
    while True:
        raw_amount = input("Amount (₹): ").strip()
        try:
            amount = float(raw_amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return round(amount, 2)
        except ValueError:
            print("Please enter a valid number, for example 125 or 49.50.")


def ask_date():
    """Ask for a date in YYYY-MM-DD format; Enter uses today's date."""
    while True:
        raw_date = input("Date (YYYY-MM-DD, press Enter for today): ").strip()
        if not raw_date:
            return datetime.today().strftime(DATE_FORMAT)
        try:
            return datetime.strptime(raw_date, DATE_FORMAT).strftime(DATE_FORMAT)
        except ValueError:
            print("Please enter a valid date in YYYY-MM-DD format, for example 2026-10-28.")


def add_expense(expenses):
    print("\n--- Add an Expense ---")
    category = input("Category (e.g. Food, Travel, Books): ").strip()
    while not category:
        print("Category cannot be empty.")
        category = input("Category: ").strip()

    description = input("Description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input("Description: ").strip()

    amount = ask_amount()
    date = ask_date()

    expense = {
        "id": max((item.get("id", 0) for item in expenses), default=0) + 1,
        "date": date,
        "category": category.title(),
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense saved successfully.")


def view_expenses(expenses):
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"{'ID':<4} {'Date':<12} {'Category':<14} {'Amount (₹)':>12}  Description")
    print("-" * 72)
    for item in sorted(expenses, key=lambda entry: (entry.get("date", ""), entry.get("id", 0))):
        print(
            f"{item.get('id', '-'):<4} "
            f"{item.get('date', '-'):<12} "
            f"{item.get('category', '-')[:14]:<14} "
            f"{item.get('amount', 0):>12.2f}  "
            f"{item.get('description', '')}"
        )


def show_total(expenses):
    total = sum(float(item.get("amount", 0)) for item in expenses)
    print(f"\nTotal expenses: ₹{total:.2f}")


def show_category_summary(expenses):
    print("\n--- Category Summary ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    totals = {}
    for item in expenses:
        category = item.get("category", "Uncategorized")
        totals[category] = totals.get(category, 0) + float(item.get("amount", 0))

    for category, total in sorted(totals.items()):
        print(f"{category:<18} ₹{total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n" + "=" * 34)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 34)
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Show total expenses")
        print("4. Show spending by category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category_summary(expenses)
        elif choice == "5":
            print("Your expenses are saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
