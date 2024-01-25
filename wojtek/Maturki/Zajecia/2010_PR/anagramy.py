znaki = open("anagram.txt", "r").readlines()
znaki = [x.strip().split() for x in znaki]
g = True
c = 0
wiersze = []
for znak in znaki:
    g = True
    for count in range(len(znak)-1):
        if len(znak[count])!=len(znak[count+1]):
            g = False
            wiersze.append(znak)
            break
    if g:
        print(znak)
print("\nZad 2\n")
for znak in znaki:
    g = True
    for count in range(len(znak)-1):
        if sorted(znak[0])!=sorted(znak[count+1]):
            g = False
            break
    if g:
        print(znak)