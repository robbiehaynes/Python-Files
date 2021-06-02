#Rob Haynes
#25 May 2021

array = []
print("Enter an array:")

for y in range(9):
    temp_x = []
    row = input()
    for z in range(9):
        num = int(row[z])
        temp_x.append(num)

    array.append(temp_x)

co_ords = input("Enter coordinates:\n").split()
for i in range(len(co_ords)):
    co_ords[i] = int(co_ords[i])

while -1 not in co_ords:
    print("Value = ",array[co_ords[0]][co_ords[1]],sep='')
    co_ords = input("Enter coordinates:\n").split()
    for i in range(len(co_ords)):
        co_ords[i] = int(co_ords[i])

print("DONE")