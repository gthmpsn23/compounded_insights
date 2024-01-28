import math

# Function that calculates average market returns
initial_deposit = 1000
monthly_deposit = 20
years = 15


# Average percentage return over the past 50 years adjusted for inflation.

stock_market_returns = 0.075

monthly_rate = stock_market_returns / 12
total_months = years * 12
annual_increase_count = 0


def market_returns_increase(stock_market_returns, years, initial_deposit, monthly_deposit):
    monthly_rate = stock_market_returns / 12
    total_months = years * 12

    future_value = initial_deposit * (1 + monthly_rate) ** total_months
    for month in range(1, total_months + 1):
        future_value += monthly_deposit * (1 + monthly_rate) ** (total_months - month)
        if month % 12 == 0:
            monthly_deposit *= (1 + 0.00) 
            # annual_increase_count += 1
            # print(f"Year {annual_increase_count}, New Monthly deposit = {monthly_deposit}")
    return future_value

# def market_returns_increase():

#     future_value = initial_deposit * (1 + monthly_rate) ** total_months
#     for month in range(1, total_months + 1):
#         future_value += monthly_deposit * (1 + monthly_rate) ** (total_months - month)
#         if month % 12 == 0:
#             monthly_deposit *= (1 + 0.05) 
#             # annual_increase_count += 1
#             # print(f"Year {annual_increase_count}, New Monthly deposit = {monthly_deposit}")
#     return future_value


# Collects deposit and investment duration from user

market_return = market_returns_increase(stock_market_returns, years, initial_deposit, monthly_deposit)

print(f"Market Investment Value after {years} years: {market_return}")

