year=input('Enter year:')
l = []

try:
    with open('measles.txt', 'r') as f:
        for lines in f:
            line = lines.split()
            if line:
                if year in ["ALL", 'all', '']:
                    l.append(lines)
                elif line[4].startswith(year):
                    l.append(lines)

except IOError:
    print('Could not read file')
if l:
    file=input("Enter name of file in which data will be written: ")
    with open(file,'w') as f:
        for lines in l:
            f.write(lines)
else:
    print('No data to write')