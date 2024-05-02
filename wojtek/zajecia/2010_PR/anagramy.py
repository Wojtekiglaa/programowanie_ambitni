slowa = [x.strip().split() for x in open("anagram.txt","r").readlines()]
for slowo in slowa:
    for x in range(len(slowo)):
        if len(slowo[x] == len(slowo[x+1])):

