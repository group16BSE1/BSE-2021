#City-Worker pay Check Program
try:
    location = input("enter name of city: ").lower
    payment = int(input("enter salary: "))

    if(location == "space"):
        choice = "Without a doubt , I’ll take it."
    elif(location == "mbarara"):
        if(payment <= 4000000):
            choice = "No Thanks, I can find something better"
        else:
            choice = "Sure, I can work with this"
    elif(location == "kampala"):
        if(payment < 10000000):
            choice = "No way!"
        else:
            choice = "Sure, I can work with this"
    elif(payment >= 6000000):
        choice = "Sure, I can work with this"
    else:
        choice = "No Thanks, I can find something better"

    print(choice)
except ValueError:
    print("Error, failed to execute")