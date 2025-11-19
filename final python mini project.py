# Expense Tracker Application

# List to store all expense entries as dictionaries
expenses = []

def show_menu():
    print("\n----- Expense Tracker Menu -----")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total and By Category")
    print("4. Delete Expense")  # New option added
    print("5. Exit")

def add_expense():
    try:
        amount = float(input("Enter the amount: "))
        description = input("Enter description: ").strip()
        category = input("Enter category (Food/Travel/Other): ").strip().capitalize()
        if category not in ['Food', 'Travel', 'Other']:
            print("Invalid category entered. Setting category as 'Other'.")
            category = 'Other'
        expenses.append({"amount": amount, "description": description, "category": category})
        print("Expense added successfully.")
    except ValueError:
        print("Invalid input for amount. Please enter a numeric value.")

def view_all_expenses():
    print("\nAll Recorded Expenses:")
    if not expenses:
        print("No expenses recorded yet.")
    else:
        for i, exp in enumerate(expenses, 1):
            print(f"{i}. {exp['description']} - {exp['category']} - ₹{exp['amount']:.2f}")

def view_total_and_by_category():
    if not expenses:
        print("\nNo expenses to summarize.")
        return
    total = sum(exp['amount'] for exp in expenses)
    print(f"\nTotal Expenses: ₹{total:.2f}")
    category_totals = {}
    for exp in expenses:
        category_totals[exp['category']] = category_totals.get(exp['category'], 0) + exp['amount']

    print("Expenses by Category:")
    for category, amt in category_totals.items():
        print(f" - {category}: ₹{amt:.2f}")

def delete_expense():
    view_all_expenses()
    if not expenses:
        return
    try:
        num = int(input("Enter the number of the expense to delete: "))
        if 1 <= num <= len(expenses):
            deleted = expenses.pop(num - 1)
            print(f"Deleted: {deleted['description']} - {deleted['category']} - ₹{deleted['amount']:.2f}")
        else:
            print("Invalid selection. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            view_total_and_by_category()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            print("Thank you for using Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
