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


def main():
    while True:
        user_code = input("ENTER CUSTOMER CODE: ").lower()
        if user_code in ['r', 'c', 'i']:
            start_units = int(input("ENTER BEGINNING METER READING: "))
            end_units = int(input("ENTER ENDING METER READING: "))
            diff_units = differnce_check(start_units, end_units) #calculates difference of the units
            if user_code == 'r':
                cost_of_Units = residential_user(diff_units)
                print(cost_of_Units)
            elif user_code == 'c':
                cost_of_Units = commercial_user(diff_units)
                print(cost_of_Units)

    
main()