#Rob Haynes
#24 March 2021

from math import sqrt

a = eval(input("Enter the length of side a:\n"))
c = eval(input("Enter the length of side c:\n"))

if a <= 0 or c <= 0:
    print("Sorry, lengths must be positive numbers.")
else:
    b = sqrt((c*c - a*a))
    print("The length of side b is ",b,".",sep='')
