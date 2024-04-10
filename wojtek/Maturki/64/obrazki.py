obrazki = open("obrazki.txt", "r").readlines()
obrazki = [x.strip().split() for x in obrazki]
# print(obrazki)
obrazkiogolne = []
obrazek = []
for x in obrazki:
    if len(x) >0:
        obrazek.append(x)
    else:
        obrazkiogolne.append(obrazek)
        obrazek = []
obrazki.append(obrazek)
# print(obrazkiogolne)
#------------------------------------------
rewcount = 0
for x in obrazkiogolne:
    for y in x:
        # y = y[:-1]
        y = str(y)
        if(y.count("1") > y.count("0")):
            rewcount += 1
print(rewcount)
#------------------------------------------