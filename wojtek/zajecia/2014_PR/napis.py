liczby = [x.strip() for x in open("NAPIS.txt","r").readlines()]
# print(liczby)
suma = 0
countPierwsze = 0
def czyPierwsza(liczba):
    for i in range(2,(liczba//2)+1):
        if(liczba%i == 0):
            return True
#---------------------------------
for liczba in liczby:
    suma = 0
    for litery in liczba:
        suma += int(ord(litery))
    if not czyPierwsza(suma): #albo !=true
        countPierwsze +=1
print(countPierwsze)
#--------------------------------
rosnace = []
for liczba in liczby:
    litery = 0
    for x in range(0,len(liczba)-1):
        if ord(liczba[x]) < ord(liczba[x+1]):
            litery +=1
    if litery == len(liczba)-1:
        rosnace.append(liczba)
print(rosnace)
#-------------------------------
wieksze = []
for liczba in liczby:
    if liczby.count(liczba) > 1:
        if liczba not in wieksze:
            wieksze.append(liczba)
        else:
            continue
print(wieksze)