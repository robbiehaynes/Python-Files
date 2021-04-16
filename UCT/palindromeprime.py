#Rob Haynes
#8 April 2021

n = int(eval(input("Enter the start point N:\n")))
m = int(eval(input("Enter the end point M:\n")))
n += 1

print("The palindromic primes are:")

def isPrime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i += 6

    return True

for x in range(n,m):
    string = str(x)
    char_sta = 0
    char_end = len(string) - 1

    flag = False

    if isPrime(x):
        while char_sta != char_end:
            if string[char_sta] != string[char_end]:
                flag = True
            char_end -= 1
            if char_end != 0:
                char_sta += 1
    else:
        flag = True
    
    if not flag:
        print(string)