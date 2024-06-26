lines = open("dane_geny.txt", "r").readlines()
lines = [x.strip() for x in lines]
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
for x in lines:
    gen = GetGeny(x)
    for x in gen:
        if "BCDDC" in x:
            countmutacja += 1
print(countmutacja)
#--------------------------------------------------
dlugosci = []
dlugoscigenow = []
for x in lines:
    gen = GetGeny(x)
    for x in gen:
        dlugoscigenow.append(len(x))
    dlugosci.append(len(gen))
print(max(dlugosci),max(dlugoscigenow))
#--------------------------------------------------
liczba_gatunkow = 0
max_liczba_osobnikow = 0
genotypy_do_dlugosci = {}
for genotyp in lines:
    dlugosc = len(genotyp)
    if dlugosc not in genotypy_do_dlugosci:
      liczba_gatunkow += 1
      genotypy_do_dlugosci[dlugosc] = 0
    genotypy_do_dlugosci[dlugosc] += 1
    max_liczba_osobnikow = max(max_liczba_osobnikow, genotypy_do_dlugosci[dlugosc])
print(liczba_gatunkow, max_liczba_osobnikow)
#--------------------------------------------------
odporny = 0
silnieodporny = 0
for x in lines:
    if x == x[::-1]:
        silnieodporny += 1
for x in lines:
    gen = GetGeny(x)
    if gen == gen[::-1]:
        odporny += 1
print(odporny,silnieodporny)
#--------------------------------------------------
lengatunkow = []
ilegatunkow = 0
for x in lines:
    lengatunkow.append(len(x))
    if len(x) not in lengatunkow:
        ilegatunkow += 1
print(ilegatunkow)