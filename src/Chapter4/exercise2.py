#funtion investment
def investment(c, r, n, t):
    val_of_investment = c * (1 + ((r / 100) / n)) ** t
    return val_of_investment


principal = float(input('Enter your initial investment: '))
rate = float(input('Enter the rate per year in %: '))
years = int(input('Enter the years of the investment: '))
times_in_year = int(input('Enter the times interest is compounded in a year: '))


amount = investment(principal, rate, times_in_year, years)
print(f'Final Value of Investments is: {amount:.2f}.') #function caller with print statement
