napisy = [x.strip() for x in open("napisy.txt", "r").readlines()]
count = 0
for x in napisy:
    if len(x) % 2 == 0:
        count += 1
print(count)
#---------------------------
jedynki = 0
zera = 0
te_same = 0
for napis in napisy:
    for litera in napis:
        if litera == "0":
            zera +=1
        else: #mozna countem!!!!!
            jedynki +=1
    if zera == jedynki:
        te_same +=1
    else:
        jedynki = 0
        zera = 0
print(te_same)
#----------------------
samezera = 0
samejedynki = 0
for napis in napisy:
    if napis.count("1") == len(napis): #albo sprawdzenie czy liczba zer jest rowna zero!
        samejedynki +=1
    if napis.count("0") == len(napis):
        samezera += 1
print(f"Jedynki: {samejedynki}, zera: {samezera}")
#---------------------
policz = 0
for dlugosc in range(2,17):
    for napis in napisy:
        if dlugosc == len(napis):
            policz +=1
    print(f"{dlugosc}: {policz}")
    policz = 0