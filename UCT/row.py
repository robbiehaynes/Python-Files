#Rob Haynes
#02/04/2021

num = int(eval(input("Enter the start number:\n")))

for x in range(0,7):
    if num < 10 and num >= 0:
        print(f" {num} ", end='')
    else:
        print(f"{num} ", end='')
    num += 1