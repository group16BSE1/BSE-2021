#Total number, Total and Average calculator
numCounter = 0
total = 0.0
while True:
    number = input("Enter a number: ")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invalid Input')
        continue
    numCounter = numCounter+1
    total = total + num1

print (f'Total: {total} Number of Items: {numCounter} Average: {total/numCounter}')