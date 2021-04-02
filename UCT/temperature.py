# This program accepts a temperature given in Fahrenheit and 
# prints the equivalent in Celsius and in Kelvin.
# Name: Robbie Haynes
# 17th March 2021

input_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit_value = eval(input_str)

#Calculate equivalent Celsius value
Celsius_Value = (fahrenheit_value - 32)*(5/9)

# Calculate equivalent Kelvin value
kelvin_value = Celsius_Value+273.15

print("The temperature in Celsius is:", Celsius_Value)
print("The temperature in Kelvin is:", kelvin_value) 