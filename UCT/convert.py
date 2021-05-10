#Converts date and time format from a compact version into a long form 12-hour format
#Rob Haynes
#14 April 2021

dt_in = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

month = int(dt_in[5:7])
day = int(dt_in[8:10])
time = dt_in[11:16]
hour = int(str(time)[0:2])

if hour >= 12:
    time_unit = "pm"
    hour -= 12
else:
    time_unit = "am"

if hour == 0:
    hour = 12

if day == 1 or day == 21 or day == 31:
    day_suffix = "st"
elif day == 2 or day == 22:
    day_suffix = "nd"
elif day == 3 or day == 23:
    day_suffix = "rd"
else:
    day_suffix = "th"

if month == 1:
    month_out = "January"
elif month == 2:
    month_out = "February"
elif month == 3:
    month_out = "March"
elif month == 4:
    month_out = "April"
elif month == 5:
    month_out = "May"
elif month == 6:
    month_out = "June"
elif month == 7:
    month_out = "July"
elif month == 8:
    month_out = "August"
elif month == 9:
    month_out = "September"
elif month == 10:
    month_out = "October"
elif month == 11:
    month_out = "November"
else:
    month_out = "December"

print(f"{hour}{time[2:5]} {time_unit} on the {day}{day_suffix} of {month_out} \'{dt_in[2:4]}")