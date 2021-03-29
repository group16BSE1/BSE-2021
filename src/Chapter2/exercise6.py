from math import sqrt
x1=int(input("enter x1: "))
x2=int(input("enter x2: "))
y1=int(input("enter y1: "))
y2=int(input("enter y2: "))

distance = ((((x2-x1)**2) + ((y2-y1)**2)))
print('Distance between the points is: ', sqrt(distance))