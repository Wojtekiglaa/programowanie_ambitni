geny = [x.strip().split() for x in open("dane_geny.txt","r").readlines()]
print(geny)
def GenyZlinijki(a):
    a = str(a)
    lista = []
    while "AA" in a and "BB" in a:
        idxAA = a.index("AA") #C
        idxBB = a.index("BB")
        if idxAA<idxBB:
            lista.append(a[idxAA:idxBB + 2])
        a = a[idxBB + 2:]
    return lista