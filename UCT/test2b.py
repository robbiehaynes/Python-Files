#Rob Haynes
#12 May 2021

n = int(eval(input("Enter the length of the sequence:\n")))
words = []

for i in range(n):
    word = input(f"Enter word {i+1}:\n")
    words.append(word)

flag = False

for x in range(len(words)):
    if (x+1) < len(words):
        if words[x] >= words[x+1]:
            flag = True
        else:
            flag = False
            break

if flag == False:
    print("The words are not in reverse alphabetical order.")
else:
    print("The words are in reverse alphabetical order.")