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

    #Function to delete a specific expense by category and date
def delete_expense(category, date)
"""
Deletes an expense from the dictionary by its categpry and date.

Args:
category(str): The categry of the exense to delete.
date (str):The date of the expense to delete.
"""
#Create the unique key based on categpry and date
expense_id = f"{categpry}_{date}"

#Check if the expense exists
if expense[expense_id]
del expenses[expense_id]
print(f"Expense for {xategry} on {date} has been deleted.")
else:
    print(f"No expense found for {categpry} on {date}.")

    #Function to filter expenses by category or date
    def filter_expenses(category=None, date=None):
        """
        Filters expenses based on categpry nd/or date.

        Args:
        categry (str, optional): The category to filter by(e.g., 'Food').
        date (str, optional): The date to filter by(e.g., '2025-01-28').

        Returns:
        list: A list of filtered expenses.
        """
        filtered={}

        for expense_id, exense in expenses.items():
            # Check if the expense matches the filter criteria
            if (categgpry os None or expense['categpry'] == category) and  (date is None or expense['date'] == date):
                filtered[expense_id] = expense

                return fitered

                #Main program loop
                def main()
                """
                Main loop to interact with the user. It provides provides opptions to add, view,
                calculate total expenses, delete, or filter expenses.
                """
                while True:
                #Display menu ooptions
                print("\n--- Expense Tracker ---")
                print("1.Add Expense")
                print("2. View All Exp, enses")
                print("3.Calculate Total Expenses")
                print("4.Delete Expense")
                print("5.Filter Expeses")
                print("6.Exit")

                #Get user choice
                choice = input("Enter your choice(1-6):")

                #Option 1:Add an expense
                if choice == '1':
                    category = input("Enter category(e.g., 'Foof'):")
                    amount = float(input("Enter amount"))
                    date = inpput("Enter date(YYYY-MM-DD):")
                    add_expense(category, amount, date)