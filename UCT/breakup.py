#Converts a sentence into a comma-separated list of lowercase words
#Rob Haynes
#14 April 2021

sentence = input("Enter a sentence:\n")
location = 0
print("The word list: ",end='')

while location != -1:
    location = sentence.find(" ")
    if location == -1:
        print(f"{sentence[0:len(sentence)].lower()}.",end='')
    else:
        print(f"{sentence[0:location].lower()}, ",end='')
    sentence = sentence[(location+1):len(sentence)]