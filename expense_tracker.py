# expense_tracker.py

# Initialize the expenses dictionary
expenses = {}

# Function to add a new expense
def add_expense(expenses, category, amount, date):
    expense_id = len(expenses) + 1  # Unique ID for each expense
    expenses[expense_id] = {"category": category, "amount": amount, "date": date}
    print(f"Expense added: {category} | Amount: ${amount} | Date: {date}")

# Function to view all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nAll Expenses:")
        for expense_id, expense in expenses.items():
            print(f"ID: {expense_id} | Category: {expense['category']} | Amount: ${expense['amount']} | Date: {expense['date']}")

# Function to filter expenses by category
def filter_expenses_by_category(expenses, category):
    filtered_expenses = {id: expense for id, expense in expenses.items() if expense['category'].lower() == category.lower()}
    if not filtered_expenses:
        print(f"No expenses found for category: {category}")
    else:
        print(f"\nExpenses for category '{category}':")
        for expense_id, expense in filtered_expenses.items():
            print(f"ID: {expense_id} | Amount: ${expense['amount']} | Date: {expense['date']}")

# Function to calculate total expenses
def calculate_total(expenses):
    total = sum(expense['amount'] for expense in expenses.values())
    print(f"\nTotal Expenses: ${total:.2f}")
    return total

# Function to delete an expense by ID
def delete_expense(expenses, expense_id):
    if expense_id in expenses:
        del expenses[expense_id]
        print(f"Expense ID {expense_id} deleted.")
    else:
        print(f"Expense ID {expense_id} not found.")

# Main program function (command-line interface)
def main():
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter Expenses by Category")
        print("4. Calculate Total Expenses")
        print("5. Delete Expense")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            category = input("Enter expense category: ").strip()
            amount = float(input("Enter expense amount: ").strip())
            date = input("Enter expense date (YYYY-MM-DD): ").strip()
            add_expense(expenses, category, amount, date)
        
        elif choice == "2":
            view_expenses(expenses)
        
        elif choice == "3":
            category = input("Enter category to filter by: ").strip()
            filter_expenses_by_category(expenses, category)
        
        elif choice == "4":
            calculate_total(expenses)
        
        elif choice == "5":
            try:
                expense_id = int(input("Enter the expense ID to delete: ").strip())
                delete_expense(expenses, expense_id)
            except ValueError:
                print("Invalid input. Please enter a valid expense ID.")
        
        elif choice == "6":
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
