#Start of function
def computepay(hour, rate):
    if hour <= 40:
        pay = hour * rate
    else:
        pay = ((hour - 40) * (1.5 * rate)) + (40 * rate)
    return pay


hours = float(input('Enter Hours: '))
rates = float(input('Enter Rate: '))
print(f'Pay: {computepay(hours, rates)}')
