#Practical 1 Test
#HYNROB001 - Rob Haynes
#6 April 2021

i = int(eval(input("Enter the value of i:\n")))
j = int(eval(input("Enter the value of j:\n")))
k = int(eval(input("Enter the value of k:\n")))

if k != 1:
    result = round((i+j)/((k-1)*(k-1)))
    print(f"The answer is {result}.")
else:
    print("The value for k must not be 1.")
