# Expense Tracker Program
# This program tracks and manages expenses by allowing users to add, view, 
# calculate total expenses, and delete specific expenses using dictionaries.

# Dictionary to store expenses, where the key is a unique identifier
# (a combination of category and date), and the value is a dictionary with 'category', 'amount', 'date'.
expenses = {}

# Function to add a new expense
def add_expense(category, amount, date):
    """
    Adds a new expense to the expenses dictionary.
    
    Args:
        category (str): The category of the expense (e.g., 'Food', 'Transport').
        amount (float): The amount of the expense.
        date (str): The date of the expense (e.g., '2025-01-28').
    """
    # Create a unique key for the expense using category and date
    expense_id = f"{category}_{date}"
    
    # If the expense already exists, notify the user and return
    if expense_id in expenses:
        print(f"Expense already exists for {category} on {date}.")
        return
    
    # Create a dictionary for the expense details
    expense = {'category': category, 'amount': amount, 'date': date}
    
    # Add the expense to the dictionary using the unique ID as the key
    expenses[expense_id] = expense
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    """
    Displays all expenses in a readable format.
    If there are no expenses, it shows a message indicating that.
    """
    if not expenses:
        print("No expenses to show.")
        return
    
    print("All Expenses:")
    print(f"{'Category':<20} {'Amount':<10} {'Date':<15}")
    print("-" * 45)
    
    # Loop through the expenses dictionary and print each expense
    for expense_id, expense in expenses.items():
        print(f"{expense['category']:<20} {expense['amount']:<10} {expense['date']:<15}")

# Function to calculate the total amount of all expenses
def total_expenses():
    """
    Calculates and returns the total sum of all expenses.
    
    Returns:
        float: The total amount of all expenses.
    """
    total = sum(expense['amount'] for expense in expenses.values())
    return total

# Function to delete a specific expense by category and date
def delete_expense(category, date):
    """
    Deletes an expense from the dictionary by its category and date.
    
    Args:
        category (str): The category of the expense to delete.
        date (str): The date of the expense to delete.
    """
    # Create the unique key based on category and date
    expense_id = f"{category}_{date}"
    
    # Check if the expense exists
    if expense_id in expenses:
        del expenses[expense_id]
        print(f"Expense for {category} on {date} has been deleted.")
    else:
        print(f"No expense found for {category} on {date}.")

# Function to filter expenses by category or date
def filter_expenses(category=None, date=None):
    """
    Filters expenses based on category and/or date.
    
    Args:
        category (str, optional): The category to filter by (e.g., 'Food').
        date (str, optional): The date to filter by (e.g., '2025-01-28').
    
    Returns:
        list: A list of filtered expenses.
    """
    filtered = {}
    
    for expense_id, expense in expenses.items():
        # Check if the expense matches the filter criteria
        if (category is None or expense['category'] == category) and (date is None or expense['date'] == date):
            filtered[expense_id] = expense
    
    return filtered

# Main program loop
def main():
    """
    Main loop to interact with the user. It provides options to add, view, 
    calculate total expenses, delete, or filter expenses.
    """
    while True:
        # Display menu options
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Exp，enses")
        print("3. Calculate Total Expenses")
        print("4. Delete Expense")
        print("5. Filter Expenses")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice (1-6): ")
        
        # Option 1: Add an expense
        if choice == '1':
            category = input("Enter category (e.g., 'Food'): ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        
        # Option 2: View all expenses
        elif choice == '2':
            view_expenses()
        
        # Option 3: Calculate total expenses
        elif choice == '3':
            total = total_expenses()
            print(f"Total Expenses: {total}")
        
        # Option 4: Delete an expense
        elif choice == '4':
            category = input("Enter category of the expense to delete: ")
            date = input("Enter date of the expense to delete (YYYY-MM-DD): ")
            delete_expense(category, date)
        
        # Option 5: Filter expenses
        elif choice == '5':
            category = input("Enter category to filter by (or leave blank to skip): ")
            date = input("Enter date to filter by (or leave blank to skip): ")
            
            # If user left fields blank, filter by nothing
            if category == "":
                category = None
            if date == "":
                date = None
            
            filtered = filter_expenses(category, date)
            if filtered:
                print("Filtered Expenses:")
                for expense_id, expense in filtered.items():
                    print(f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}")
            else:
                print("No expenses match your filters.")
        
        # Option 6: Exit
        elif choice == '6':
            print("Exiting Expense Tracker. Goodbye!")
            break
        
        # Handle invalid input
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

# Run the program
if __name__ == '__main__':
    main()
