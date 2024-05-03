slowa = [x.strip().split() for x in open("anagram.txt","r").readlines()]
takiesame = True
same = []
for slowo in slowa:
    takiesame = True
    for x in range(len(slowo)-1):
        if len(slowo[x]) != len(slowo[x+1]):
            takiesame = False
            same.append(slowo)
            break
    if takiesame:
        print(slowo)
#----------------------------
print("---------------------")
for slowo in slowa:
    takiesame = True
    for x in range(len(slowo)-1):
        if sorted(slowo[0]) != sorted(slowo[x+1]):
            takiesame = False
    if takiesame:
        print(slowo)