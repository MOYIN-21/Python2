import math

investment_amount = float(input("Enter investment amount: "))
annual_interest_rate = float(input("Enter annual interest rate in percentage: "))
number_of_years = float(input("Enter number of years: "))
monthly_interest_rate = annual_interest_rate / 1200
future_investment_value = investment_amount * math.pow(1 + monthly_interest_rate, number_of_years * 12)
print("Accumulated value is $", future_investment_value)




