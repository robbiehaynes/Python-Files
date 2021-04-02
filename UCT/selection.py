#Robbie Haynes
#24 March 2021
import random

num1 = random.randint(0,200)
num2 = random.randint(0,200)
num3 = random.randint(0,200)
num4 = random.randint(0,200)

print("Values:\nnum1: ",num1)
print("num2: ",num2)
print("num3: ",num3)
print("num4: ",num4)

if num1 < num2:
    print("Smallest number is num1: ", num1)
elif num2 < num3:
    print("Smallest number is num2: ", num2)
elif num3 < num4:
    print("Smallest number is num3: ", num3)
else:
    print("Smallest number is num4: ", num4)

