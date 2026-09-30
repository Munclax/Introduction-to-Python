# Program to calculate total, average, highest and lowest expenses
# using a function and *args

def expense_summary(*expenses):

    total = 0
    count = 0
    high = None
    low = None
    # Go through every expense provided to the function
    for expense in expenses:
        # Find the highest expense
        if high is None or expense > high:
            high = expense
        # Find the lowest expense
        if low is None or expense < low:
            low = expense
        # Add the expense to the total
        total += expense
        count += 1
    # Calculate the average if at least one expense exists
    if count > 0:
        average = total / count
    else:
        average = 0
    # Return all the calculated values
    return total, average, high, low
# Taking expenses from the user
print("----- Expense Calculator -----")
e1 = float(input("Enter expense 1: "))
e2 = float(input("Enter expense 2: "))
e3 = float(input("Enter expense 3: "))
e4 = float(input("Enter expense 4: "))
e5 = float(input("Enter expense 5: "))
# Passing all expenses to the function using *args
total, average, high, low = expense_summary(e1, e2, e3, e4, e5)
# Displaying the results
print("\n----- Expense Summary -----")
print("Total expenses:", total)
print("Average expense:", average)
print("Highest expense:", high)
print("Lowest expense:", low)