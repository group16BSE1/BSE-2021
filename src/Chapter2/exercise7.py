from math import modf

money = float(input('ENTER THE MONEY YOU WOULD LIKE TO CHANGE: '))

separated_money = modf(money)
money_coin, money_paper = separated_money

#Start of paper calculation
twenties = money_paper // 20
bal = money_paper - (twenties * 20)

tens = bal // 10
bal1 = bal - (tens * 10)

fives = bal1 // 5
bal2 = bal1 - (fives * 5)

ones = bal2 // 1
bal3 = bal2 - (ones * 1)
#End of paper calculation

#Start of coin calculation
quarters = money_coin // 0.25
bal4 = money_coin - (quarters * 0.25)

dimes = bal4 // 0.1
bal5 = bal4 - (dimes * 0.1)

nickle = bal5 // 0.05
bal6 = bal5 - (nickle * 0.05)

penny = bal6 // 0.01
bal7 = bal6 - (penny * 0.01)
#End of coin calculation

print('Your change is .......')
print(f'Twenties:   {round(twenties)}')
print(f'Tens:       {round(tens)}')
print(f'Fives:      {round(fives)}')
print(f'Ones:       {round(ones)}')
print(f'Quarters:   {round(quarters)}')
print(f'Dimes:      {round(dimes)}')
print(f'Nickle:     {round(nickle)}')
print(f'Penny:      {round(penny)}')



