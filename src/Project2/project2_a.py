yearInput=input('Please enter a year: ')
listOutput = []

try:
    with open('measles.txt', 'r') as fileRead:
        for lines in fileRead:
            line = lines.split()
            if line:
                if yearInput in ["ALL", 'all', '']: #If User asks for all the years
                    listOutput.append(lines)
                elif line[4].startswith(yearInput): #If the user enters a specific year
                    listOutput.append(lines)

except IOError:
    print('Could not read file, File doesnt exist!!')

if listOutput:
    file = input("Enter name of file in which data will be written: ")
    with open(file,'w') as fileRead:
        for lines in listOutput:
            fileRead.write(lines)
else:
    print('No data to write')