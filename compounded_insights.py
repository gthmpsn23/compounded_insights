# Compounded_insights.py

import math

# Function that calculates average market returns

def market_returns(stock_market_returns, years, initial_deposit, monthly_deposits,):
    
    """ Calculates market returns based on user inputs
    User input inital deposit, monthly deposits and years of investment
    """

    monthly_rate = stock_market_returns / 12
    total_months = years * 12
    # annual_total = 0

    future_value = initial_deposit * math.pow(1 + monthly_rate, total_months)
    for month in range(1, total_months + 1):
        future_value += monthly_deposits * math.pow(1 + monthly_rate, total_months - month)
        # if month % 12 == 0:
        #     annual_total += 1
        #     print(f"Year {annual_total} = {future_value}")


    return future_value

def market_returns_increase(stock_market_returns, years, initial_deposit, monthly_deposit, increase):

    """ Works the same as the market_returns function but allows the user the increase the amount of their monthly deposit by a percentage per year
    """
    

    monthly_rate = stock_market_returns / 12
    total_months = years * 12

    future_value = initial_deposit * (1 + monthly_rate) ** total_months
    for month in range(1, total_months + 1):
        future_value += monthly_deposit * (1 + monthly_rate) ** (total_months - month)
        if month % 12 == 0:
            monthly_deposit *= (1 + increase) 
    return future_value


def savings_returns(savings_interest, years, initial_deposit, monthly_deposits ):
    """Calculates the users return if they put their money in a savings account"""
    
    monthly_rate = savings_interest / 12
    total_months = years * 12

    future_value = initial_deposit * math.pow(1 + monthly_rate, total_months)
    for month in range(1, total_months + 1):
        future_value += monthly_deposits * math.pow(1 + monthly_rate, total_months - month)

    return future_value

def savings_returns_increase(savings_interest, years, initial_deposit, monthly_deposit, increase):
    """`Calculates the users return if they increased their deposit amount by a percentage each year"""

    monthly_rate = savings_interest / 12
    total_months = years * 12

    future_value = initial_deposit * (1 + monthly_rate) ** total_months
    for month in range(1, total_months + 1):
        future_value += monthly_deposit * (1 + monthly_rate) ** (total_months - month)
        if month % 12 == 0:
            monthly_deposit *= (1 + increase) 
    return future_value

# Investment Calculator

def investment_calculator(): 

    # Collects deposit and investment duration from user

    initial_deposit = float(input("Enter your initial deposit: "))
    monthly_deposit = float(input("Enter your monthly deposits: "))
    years = int(input("How many years do you plan on investing? "))

# Average percentage return over the past 50 years adjusted for inflation.

    stock_market_returns = 0.075

# Average rate of inflation since 1990

    average_inflation = 0.025

# Average savings interest rate since 1990

    average_interest = 0.03

# Savings interest rate adjusted for inflation

    savings_interest = average_interest - average_inflation 

    # Calculates total deposits
    
    total_deposits = ((monthly_deposit * 12) * years) + initial_deposit

    # Calculates market return

    market_return_value = market_returns(stock_market_returns, years, initial_deposit, monthly_deposit)

    # Calculates saving returns

    saving_return_value = savings_returns(savings_interest, years, initial_deposit, monthly_deposit)

    # Rounds calculation to nearest decimal

    difference = market_return_value - saving_return_value

    difference_rounded = round(difference, 2)

    # Calculates total interest accrued

    market_interest_accrued = market_return_value - total_deposits

    market_interest_accrued_rounded = round(market_interest_accrued, 2)

    savings_interest_accrued = saving_return_value - total_deposits

    savings_interest_accrued_rounded = round(savings_interest_accrued, 2)

    # Prints results

    print(f"\nMarket Investment Value after {years} years: £{market_return_value:.2f}\n")

    print(f"Savings Investment Value after {years} years: £{saving_return_value:.2f}\n")

    print(f"You will be £{difference_rounded} better off by investing in the market!\n")

    print(f"If you invested your money into the market, you would have accumilated £{market_interest_accrued_rounded} on top of your total deposits of £{total_deposits} \n")

    print(f"If you put your money into a savings account, you would have only accumilated £{savings_interest_accrued_rounded} on top of your total deposits of £{total_deposits}\n")

    # Allows user to increase monthly deposits every year by a percentage

    increase_percentage = input("Do you want to see what happens if you increase your monthly deposit every year? (yes/no): \n")
    while True:
        if increase_percentage.lower() == "yes":
            try:
                increase = float(input("Enter the percentage you want to increase it by as a decimal (1% = 0.01): \n"))
                market_return_value_increase = market_returns_increase(stock_market_returns, years, initial_deposit, monthly_deposit, increase)
                market_return_value_increase_round = round(market_return_value_increase)
                print(f"You would have £{market_return_value_increase_round} at the end of the 30 years\n")
                additional_return = market_return_value_increase_round - market_interest_accrued_rounded
                print(f"That's an extra £{additional_return} from only a 1% increase per year!")
                break
            except ValueError:
                print("That's  not a number, please try again")
        elif increase_percentage.lower() == "no":
            print("No problem!")
            break
        else: 
            print("Incorrect input, please try again")


investment_calculator()

 