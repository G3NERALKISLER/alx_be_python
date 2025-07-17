monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your annual savings, including interest, is: {annual_savings}")
                          