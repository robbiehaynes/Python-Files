#Rob Haynes
#25 May 2021

word = input("Enter strings (end with DONE):\n")
words = []

while word != "DONE":
    if word not in words:
        words.append(word)
    word = input("")

print("\nUnique list:")
for x in words:
    print(x)