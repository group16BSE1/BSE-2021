#question 1 solution
hoursWorked = int(input("Enter hours: "))
rate = int(input("Enter the rate: "))

#calculation for the pay
if hoursWorked > 40:
    excessHours = hoursWorked - 40
    pay = (excessHours * 1.5) * rate
    finalpay = (rate * 40) + pay
    print(f'PAY: {finalpay}')
else:
    finalpay2 = rate * hoursWorked
    print(f'PAY: {finalpay2}')
