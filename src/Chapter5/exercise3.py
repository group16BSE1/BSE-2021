#Global variables of stock coins
nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0

#Global variables of money in xx.xx and cents ie xx.xx * 100 to enable us call them by other functions
#They are also updated by another function
g_money_toPay = 0
g_cents_toPayConverted = 0

#Global variables of the coins inserted by the user
#These will be updated by automatically after every user
#We use a global keyword to update it inside another function
#Since a function cant directly change a global variable
g_nickles_count = 0
g_dimes_count = 0
g_quarters_count = 0
g_ones_count = 0
g_five_count = 0 


def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')
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