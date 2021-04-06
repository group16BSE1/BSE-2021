
#calculation for the pay
try:
    hoursWorked = int(input("Enter hours: "))
    rate = int(input("Enter the rate: "))
    int(hoursWorked)
    int(rate)
    if hoursWorked > 40:
        excessHours = hoursWorked - 40
        pay = (excessHours * 1.5) * rate
        finalpay = (rate * 40) + pay
        print(f'PAY: {finalpay}')
    else:
        finalpay2 = rate * hoursWorked
        print(f'PAY: {finalpay2}')
except:
    print("Error, please enter numeric input")