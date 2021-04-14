# Rob Haynes
# 02/04/2021

num = int(eval(input("Enter a number: \n")))
display = num

for x in range(num,num+41, 7):
    if display < 10 and display >= 0:
        print(f" {display}")
    else:
        print(f"{display}")
    display += 7