#Rob Haynes
#02/04/2021

num = int(eval(input("Enter the start number:\n")))

for y in range(6):
    for x in range(7):
        if num < 10 and num >= 0:
            print(f" {num} ", end='')
        else:
            print(f"{num} ",end='')
        num += 1
    print("")
