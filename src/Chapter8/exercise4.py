#  A program that opens the file romeo.txt and reads it line by line and also splits the lines

words = []
fhand = open('romeo.txt', 'r')

for line in fhand: #Iterate through the lines
    for word in line.split(' '):
        if word not in words:
            words.append(word)

print(sorted(words))