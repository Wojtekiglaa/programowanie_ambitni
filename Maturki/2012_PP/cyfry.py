cyfry = open("cyfry.txt", "r").readlines()
test = cyfry
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
    suma = 0
    for i in range(len(cyfra)-1):
        suma += int(cyfra[i])
        if suma > smax:
            smax = suma
            lmax = cyfra
        else:
            smin = suma #zobaczyc co jest nie tak
            lmin = cyfra
print(f"Suma: {smax, smin, lmax,lmin}") # najmniejsza nie działa xd
#---------------------------------------------------
count = 0
for i in cyfry:
    count = 0
    for a in range(len(i)-1):
        if int(i[a]) < int(i[a+1]):
            count += 1
    if(count == len(i)-1):
        print(i)#czemu nie dziala xd