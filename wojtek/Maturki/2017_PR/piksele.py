dane = open("piksele.txt", "r").readlines()
# dane = open("przyklad.txt", "r").readlines()
dane = [x.strip().split() for x in dane]
dane = [[int(y) for y in x] for x in dane]
a = []
b = []
for c in dane:
    a.append(max(c))
    b.append(min(c))
print(a,b)
print(max(a),min(b))
#--------------------------------------------------
nie_pasuje = 0
wiersze = []
for x in range(len(dane)//2):
    if dane[x] != dane[x][::-1]:
        nie_pasuje +=1
    wiersze.append(nie_pasuje)
print(min(wiersze))
#--------------------------------------------------
nlinia = 1
cmax = []
for y in range(len(dane[0])):
    for x in range(len(dane)-1):#dkugosc konkretnego wiersza
        if dane[x][y] == dane[x+1][y]:
            nlinia +=1
        else:
            cmax.append(nlinia)
            nlinia = 1#!!!!!!!!
print(max(cmax))
#--------------------------------------------------
