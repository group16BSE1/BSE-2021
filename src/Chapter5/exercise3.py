#Global variables of stock coins
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0

#Function prints the current stock value
#Receives global variables of the coin stock as arguments
def stock_contains(n_value, d_value, q_value, o_value, f_value):
    print(f'{n_value:>2} -- nickels')
    print(f'{d_value:>2} -- dimes')
    print(f'{q_value:>2} -- quarter')
    print(f'{o_value:>2} -- one dollar bill')
    print(f'{f_value:>2} -- five dollar bill')


print('WELCOME TO THE VENDING MACHINE CHANGE MAKER PROGRAM!\n\tCURRENT STOCK CONTAINS\n')
stock_contains(nickels, dimes, quarters, one_dollar, five_dollar)