#Program to plot a graph
#Rob Haynes
#20 May 2021

import math

function = input("Enter a function f(x):\n")

for y in range(10,-11,-1):
    for x in range(-10,11):
        func_y = round(eval(function))
        if  func_y == y:
            print("*", end='')
        else:
            if x == 0 and y == 0:
                print("+", end='')
            elif x == 0 and not y == 0:
                print("|",end='')
            elif y == 0 and not x == 0:
                print("-",end='')
            else:
                print(" ",end='')
    print("\n",end='')