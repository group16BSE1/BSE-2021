#This calculates the difference in units
def differnce_check(begin_units, end_units):
    if end_units >= begin_units:
        units_used = end_units - begin_units
    else:
        #For readings where the ending units are less than beginning units
        units_used = (1000000000 - begin_units) + end_units
    return units_used / 10


#calculation for residential customer
def residential_user(galon_units):
    galon_units = galon_units
    total = 5.00 + (0.0005 * galon_units)
    return total


#calculation for commercial customer
def commercial_user(galon_units):
    galon_units = galon_units 
    if galon_units <= 4000000:
        total = 1000.00
    else:
        total = 1000 + (0.00025 * galon_units)    
    return total  


#Function for the industrial users
def industrial_user(galon_units):
    galon_units = galon_units
    if galon_units <= 4000000:
        total = 1000.00
    elif galon_units > 4000000 and galon_units <= 10000000: 
        total = 2000.00    
    else:
        total = 2000.00 + (0.000025 * galon_units)
    
    return total    


#This functions prints the details including the cost of water usage
def printDetails(user_code, start_units, end_units, diff_units, cost_of_Units):
    print('\n\n')
    print(f'Customer code: {user_code}')
    print(f'Beginning metre reading: {start_units}')
    print(f'Ending metre reading: {end_units}')
    print(f'Galons of water used: {diff_units}')
    print(f'Amount billed: ${cost_of_Units:.2f}')
    print('\n')

def main():
    while True:
        user_code = input("ENTER CUSTOMER CODE: ").lower()
        if user_code in ['r', 'c', 'i']:
            start_units = int(input("ENTER BEGINNING METER READING: "))
            end_units = int(input("ENTER ENDING METER READING: "))
            diff_units = differnce_check(start_units, end_units) #calculates difference of the units
            if user_code == 'r':
                cost_of_Units = residential_user(diff_units)
            elif user_code == 'c':
                cost_of_Units = commercial_user(diff_units)
            elif user_code == 'i':
                cost_of_Units = industrial_user(diff_units) 
        else:
            break

        
        printDetails(user_code, start_units, end_units, diff_units, cost_of_Units)
        
    
main()