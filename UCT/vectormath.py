#Rob Haynes
#25 March 2021
from math import sqrt

vector_a = []
vector_b = []

vector_a = input("Enter vector A:\n").split()
for x in range(3):
    vector_a[x] = int(vector_a[x])

vector_b = input("Enter vector B:\n").split()
for x in range(3):
    vector_b[x] = int(vector_b[x])

add = []
dot, norm_a, norm_b, num_to_sqrt_a, num_to_sqrt_b = 0,0,0,0,0

for i in range(3):
    add.append(vector_a[i]+vector_b[i])
    dot += (vector_a[i]*vector_b[i])
    num_to_sqrt_a += vector_a[i]**2
    num_to_sqrt_b += vector_b[i]**2

print("A+B = ",add,sep='')
print("A.B = ",dot,sep='')
print("|A| = ","{:.2f}".format(sqrt(num_to_sqrt_a)),sep='')
print("|B| = ","{:.2f}".format(sqrt(num_to_sqrt_b)),sep='')