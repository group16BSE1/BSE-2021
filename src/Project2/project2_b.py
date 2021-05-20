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
        yearInput = int(input('Please enter the year: '))
        if yearInput >= 1000 and  (1979  < yearInput < 2013):
            yearInput = str(yearInput)
            break #Breaks if the year is correct
        else:
            print('Year is not valid!!')

    while True:
        incomeSelected = input('Please select income:'
                               '\n\t 1 \t Low income'
                               '\n\t 2 \t Lower middle income'
                               '\n\t 3 \t Upper middle income'
                               '\n\t 4 \t High income\n')
        if incomeSelected == '1':
            incomeUserInput = 'WB_LI'
            display_name = 'Low income'
            break
        elif incomeSelected == '2':
            incomeUserInput = 'WB_LMI'
            display_name = 'Lower middle income income'
            break
        elif incomeSelected == '3':
            incomeUserInput = 'WB_UMI'
            display_name = 'Upper middle income'
            break
        elif incomeSelected == '4':
            incomeUserInput = 'WB_HI'
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
        if (line.find(incomeUserInput) != -1) and (line.find(yearInput) != -1):
            country = line[:50].strip()
            percent_of_vac = int(line[58:61].strip())
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

    print(f'For the year: {yearInput} and Income level: {display_name}\n')
    print(f'Total findings: {counter} Countries')
    print(f'Average Vaccination: {round(average_vaccine, 2)}%')
    print(f'Highest: {highestPercent}% for: {countryWithHighest}')
    print(f'Lowest: {lowestPercent}% for {countryWithLowest}')


def main():
    fileOpened = open_file()
    process_file(fileOpened)

if __name__ == '__main__':
    main()