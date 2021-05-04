#This calculates the difference in units
def differnce_check(begin_units, end_units):
    if end_units >= begin_units:
        units_used = end_units - begin_units
    else:
        #For readings where the ending units are less than beginning units
        units_used = (1000000000 - begin_units) + end_units
    return units_used


