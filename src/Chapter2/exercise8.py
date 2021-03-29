money = float(input('Enter your initial investment: '))
rate = float(input('Enter the rate per year in %: '))
time = int(input('Enter the years of the investment: '))
times_per_year = int(input('Enter the times interest is compounded in a year: '))

principal = money * (1 + ((rate/100) / times_per_year)) ** time
print(f'Investments is: {principal:.2f}.')