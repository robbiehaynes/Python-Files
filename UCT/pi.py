#Rob Haynes
#8 April 2021

from math import sqrt

pi = 2.0
term = 0
num_sqrts = 1

while term != 1:
    bottom_term = 0
    for x in range(num_sqrts):
        bottom_term = sqrt(2+bottom_term)

    num_sqrts += 1
    term = 2.0/bottom_term

    pi *= term

print("Approximation of pi: ",round(pi,3),sep='')
r = eval(input("Enter the radius:\n"))

area = pi*(r*r)

print("Area: ",round(area,3),sep='')