#Rob Haynes
#8 April 2021

month = input("Enter the month ('January', ..., 'December'):\n")
day  = input("Enter the start day ('Monday', ..., 'Sunday'):\n")
numdays = 0
gaps = 0
gap_counter = 0

thirty_one_set = {"January","March","May","July","August","October","December"}
thirty_set = {"April","June","September","November"}

print(f"{month}\nMo Tu We Th Fr Sa Su\n",end='')

if month == "February":
    numdays = 28
elif month in thirty_one_set:
    numdays = 31
elif month in thirty_set:
    numdays = 30

if day == "Tuesday":
    gaps = 1
elif day == "Wednesday":
    gaps = 2
elif day == "Thursday":
    gaps = 3
elif day == "Friday":
    gaps = 4
elif day == "Saturday":
    gaps = 5
elif day == "Sunday":
    gaps = 6

day_count = 1

for y in range(6):
    for x in range(7):
        if gap_counter != gaps:
            print("   ",end='')
            gap_counter += 1
        elif day_count <= numdays:
            if day_count < 10:
                print(f" {day_count} ",end='')
            else:
                print(f"{day_count} ",end='')
            day_count += 1
    print("")
