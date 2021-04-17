#Voter Age Checking Program
try:
    age = int(input('Enter your age: '))
    if age >= 18:
        print("You can vote!")
    elif age >= 0 and age <=17:
        print("Your too young to vote!")
    else:
        print("Your not a time traveller!")        
except ValueError:
    print("Please enter a valid age!")
    


    