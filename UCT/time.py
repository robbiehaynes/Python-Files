#Robbie Haynes
#24 March 2021
#Change V2.0

hours = int(eval(input("Enter the hours: ")))
minutes = int(eval(input("Enter the minutes: ")))
seconds = int(eval(input("Enter the seconds: ")))

if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
