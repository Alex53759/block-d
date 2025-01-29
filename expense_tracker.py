# Expense Tracker Program

# This program tracks and manages expenses by allowing users to add, view,

# calculate total expenses, and delete specific expenses using dictionaries.


# Dictionary to store expenses, where the key is a unique identifier

# (a combination of category and date), and the value is a dictionary with 'category', 'amount', 'date'.

expenses = {}


# Function to add a new expense

def add_expense(category, amount, date):
    """"
    Adds a new expense to the expenses dictionary.


    Args:
    category (str): The category of the expense (e.g., 'Food', 'Transport')
    amount (float): The amount of the expense.
    date (str): The date of the expense (e.g., '2025-01-28')
    """
    # Create a unique key for the expense using category and date

    expense_id = f "{category}_{date}"

    # If the expense already exists, notify the user and return

    if expense_id in expenses:
        print("Expenses added successfully")

# Function to view all expenses
def view_expenses()
    """
    Displays all expenses in a reading format.
    If there are no expenses, it shows a message indicating that.
    """
    if not expenses:
        print("No expenses to show")
        return

print("All Expenses")
print(f"{'Category':<20}"){'Amount':<10} {'Date':<15"}
print ("-"* 45)

# Function to calculate the total amount of all expenses
def total_expenses():
    """
    Calculates and returns the total sum of all expenses.

    Returns:
        float: The total amount of all expenses.
    """
    total = sum(expense['amount'] for expenses in expenses.values()
    return total