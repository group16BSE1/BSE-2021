#  A program that reads through the mail box  splits the line starting from "From"

filename = input('Enter a file name: ')
count = 0

fileHandle = open(filename)
for line in fileHandle:
    if line.startswith('From: '):
        print(line.split(' ')[1])
        count = count + 1
print(f'There were {count} lines that start with From')