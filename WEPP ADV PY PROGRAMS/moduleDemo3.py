from finance import *

if __name__== "__main__":
    expenses=[1500,200,300]
    incomes=[4000.1500]
    total_expenses = calculate_expenses(expenses)                    #2000
    total_income = calculate_income(incomes)                         #5500
    total_savings = calculate_savings(total_income, total_expenses)  #3500

    print(f"Total Expenses: ${total_expenses}")
    print(f"Total Income: ${total_income}")
    print(f"Total Savings: ${total_savings}")