geny = open("dane_geny.txt", "r").readlines()
geny = [x.strip() for x in geny]
# for x in geny:
#     idpoczatek = x.index("AA")
#     idkoniec = x.index("BB")
#     gen = x[idpoczatek+2:idkoniec]
#     print(gen)
def GetGeny(a):
    a = str(a)
    lista = []
    while "AA" in a and "BB" in a:
        idxAA = a.index("AA") #C
        idxBB = a.index("BB")
        if idxAA<idxBB:
            lista.append(a[idxAA:idxBB + 2])
        a = a[idxBB + 2:]
    return lista
#--------------------------------------------------
countmutacja = 0
for x in geny:
    gen = GetGeny(x)
    for x in gen:
        if "BCDDC" in x:
            countmutacja += 1
print(countmutacja)
#--------------------------------------------------
dlugosci = []
dlugoscigenow = []
for x in geny:
    gen = GetGeny(x)
    for x in gen:
        dlugoscigenow.append(len(x))
    dlugosci.append(len(gen))
print(max(dlugosci),max(dlugoscigenow))
#--------------------------------------------------
countgatunki = 0
for x in geny:
    countgatunki += 1
print(countgatunki)