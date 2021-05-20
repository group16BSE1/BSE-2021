'''Function that repeatedly asks for a file name and returns
a file object if it exists'''
def open_file():
    while True:
        fileName = str(input('Enter a file name: '))
        try:
            fileHandle = open(fileName)
            break
        except IOError: #IOError for Input and Output errors, incase file doesnt exist
            print('File not available. Try again with correct file name')

    return fileHandle



def process_file(file):
    while True:
        yearInput = input('Please enter the year: ')
        if len(yearInput) == 4:
            try:
                # make sure the year entered is a number
                yearchecker = int(yearInput)
                if yearchecker > 1979 and yearchecker < 2013:
                    break
                else:
                    print('Year is not in range')
            except:
                print('Invalid, year should be digits')
        else:
            print('Year should be a 4 digit number!!')



    #yearInput = '2000'
    while True:
        incomeSelected = input('Please select income:'
                               '\n\t 1 \t Low income'
                               '\n\t 2 \t Lower middle income'
                               '\n\t 3 \t Upper middle income'
                               '\n\t 4 \t High income\n')
        if incomeSelected == '1':
            incomeIs = 'WB_LI'
            display_name = 'Low income'
            break
        elif incomeSelected == '2':
            incomeIs = 'WB_LMI'
            display_name = 'Lower middle income income'
            break
        elif incomeSelected == '3':
            incomeIs = 'WB_UMI'
            display_name = 'Upper middle income'
            break
        elif incomeSelected == '4':
            incomeIs = 'WB_HI'
            display_name = 'High income'
            break
        else:
            print('You entered false value, try again')
    counter = 0
    vaccine_total = 0
    lowestPercent = None
    highestPercent = None
    countryWithHighest = None
    countryWithLowest = None

    for line in file:
        if (line.find(incomeIs) != -1) and (line.find(yearInput) != -1):
            country = line[:50]
            country = country.strip()
            percent_of_vac = line[58:61]
            percent_of_vac = percent_of_vac.strip()
            percent_of_vac = int(percent_of_vac)
            # start point......getting the highest and lowest values

            if (lowestPercent is None) or (highestPercent is None):
                lowestPercent = percent_of_vac
                highestPercent = percent_of_vac
                countryWithHighest = country
                countryWithLowest = country
            elif lowestPercent > percent_of_vac:
                countryWithLowest = country
                lowestPercent = percent_of_vac
            elif highestPercent < percent_of_vac:
                countryWithHighest = country
                highestPercent = percent_of_vac
            # end point......getting the highest and lowest values

            counter += 1
            vaccine_total = vaccine_total + percent_of_vac
    # for loop end point

    average_vaccine = vaccine_total / counter
    print(f'For:'
          f'\n\tThe year:\t {yearInput}'
          f'\n\tIncome :\t {display_name}'
          f'\n\n\tCount :\t {counter}'
          f'\n\tAverage percentage:{average_vaccine}'
          f'\n\tHighest percentage:{highestPercent}\tCountry: {countryWithHighest}'
          f'\n\tLowest percentage:{lowestPercent}\tCountry: {countryWithLowest}')

def main():
    fileOpened = open_file()
    process_file(fileOpened)

if __name__ == '__main__':
    main()