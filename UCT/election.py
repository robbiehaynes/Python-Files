#Rob Haynes
#25 May 2021

print("Independent Electoral Commission\n--------------------------------")
votes = {}
parties = []

party = input("Enter the names of parties (terminated by DONE):\n")
while party != "DONE":
    if party not in votes:
        votes[party] = 1
        parties.append(party)
    else:
        votes.update({party:votes[party]+1})

    party = input()

parties = sorted(parties)
parties.sort()
print("\nVote counts:")

for i in range(len(parties)):
    print(parties[i],end='')
    for x in range(11-len(parties[i])):
        print(" ",end='')
    print(f"- {votes[parties[i]]}")