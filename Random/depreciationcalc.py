#Rob Haynes
#Reducing Balance Depreciation Calculator
#6 April 2021

value = eval(input("Enter the value of the asset before depreciation:\nR"))
dep = eval(input("Enter the rate of depreciation in %:\n"))/100
n = eval(input("Enter the number of years:\n"))

for x in range(n):
    value = value - (value*dep)

print(f"The value of the asset after {n} years is R{value}")