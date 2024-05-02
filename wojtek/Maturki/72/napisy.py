import difflib
napisy = [x.strip().split() for x in open("napisy.txt", "r").readlines()]
count = 0
for napis in napisy:
    if len(napis[0])*3 <= len(napis[-1]) or len(napis[-1])*3 <= len(napis[0]):
        count +=1
print(count)
#x.starts/endswith
for napis in napisy:
    if napis[-1].startswith(napis[0]):
        print(napis[0],napis[-1],napis[-1][len(napis[0]):]) #!!!!!
#--------------------------------------------------
def koncowka(a,b):
    ad = len(a)
    bd = len(b)
    k = 0
    while  k< ad and k < bd and a[ad-k-1] == b[bd-k-1]:
        k += 1
    return k
dlugosc = 0
for napis in napisy:
    wspolna = koncowka(napis[0],napis[-1])
    if wspolna > dlugosc:
        dlugosc = wspolna
    if wspolna == dlugosc:
        print(napis[0],napis[-1])

print(dlugosc)