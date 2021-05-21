# A program that prompts for a list of numbers that prints out maximum and minimum number!

myList = []

while True:
    number = input('Enter a number: ')
    if number == 'done':
        break
    try:
        value = float(number)
    except:
        print('Invalid input')
        continue

    myList.append(value)

print(f'Minimum Number: {min(myList)}\nMaximum Number: {max(myList)}')