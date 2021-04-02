#Rob Haynes
#24 March 2021

name = input("Enter runner's name:\n")

day = input("Enter day of month:\n")
month = input("Enter month of year:\n")
year = input("Enter year:\n")

date = day+"/"+month+"/"+year

time = eval(input("Enter completion time (in mins):\n"))
prize = eval(input("Enter prize money (in rand):\n"))

time_per_kilometer = time/42.195

print("\n",name," completed the race on ",date," in ",time," minutes.\nThe runner wins R",prize,".\nAverage time per kilometer was ",time_per_kilometer," minutes.", sep='')