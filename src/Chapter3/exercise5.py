#Guest checking price Program
try:
    guests = int(input("Enter the number of guests attending: "))

    if guests <= 0:
        print("Please enter a number greater than 0!")
    elif guests <= 50:
        print("It will cost you $4000")
    elif guests <= 100:
        print("It will cost you $10000")
    elif guests <= 200:
        print("It will cost you $15000")
    else:
        print("It will cost you $20000")
        
except ValueError:
    print("Please enter a valid number of guests!")