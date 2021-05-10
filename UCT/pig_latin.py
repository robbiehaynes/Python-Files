#Convert English to Pig Latin
#Rob Haynes
#14 April 2021

sentence = input("Enter a sentence:\n")
location = 0

#Converts word into pig latin
def convert_to_pig(word_in):
    if word_in[0] in 'aeiou':
        new_word = word_in + "way"
    else:
        consonants = ""
        i = 0
        while (i < len(word_in)) and (word_in[i] not in 'aeiou'):
            consonants = consonants + word_in[i]
            i += 1
        new_word = word_in[i:len(word_in)]+"a"+consonants+"ay"
    return new_word

#Splits the sentence into single words by searching for spaces
while location != -1:
    location = sentence.find(" ")
    if location == -1:
        word = sentence[0:len(sentence)].lower()
        print(f"{convert_to_pig(word)}",end='')
    else:
        word = sentence[0:location].lower()
        print(f"{convert_to_pig(word)} ",end='')
        
    sentence = sentence[(location+1):len(sentence)]