cyfry = open("cyfry.txt", "r").readlines()
sex = cyfry
cyfry = [x.strip() for x in cyfry]
parzyste = 0
for i in range(len(cyfry)):
    if int(cyfry[i]) % 2 == 0:
        parzyste += 1
print(f"Parzyste: {parzyste}")
#---------------------------------------------------
smax = 0
smin = 0
suma = 0
lmin = ""
lmax = ""
for cyfra in cyfry:
    for i in range(len(cyfra)-1):
        suma += int(cyfra[i])
        if suma > smax:
            smax = suma
            lmax = cyfra
        else:
            smin = suma
            lmin = cyfra
    suma = 0
print(f"Suma: {smax, smin, lmax,lmin}") # najmniejsza nie działa xd
#---------------------------------------------------
count = 0
for i in sex:
    for a in range(len(cyfry)-1):
        if i[a] < i[a+1]:
            count += 1
            if(count == len(i[a])):
                print(i[a])
                count = 0 #czemu nie dzial xd