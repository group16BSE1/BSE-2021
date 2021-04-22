#Maximum and minimum difinition
numberList = []                        
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break

    try:
        number = float(input_number)
        numberList.append(input_number)
    except ValueError:
        print('Invalid input')
       
if numberList:
    print('Maximum: ', max(numberList) or None)
    print('Minimum: ', min(numberList) or None)