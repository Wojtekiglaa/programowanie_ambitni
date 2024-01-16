cyfry = open("cyfry.txt", "r").readlines()
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
for cyfra in cyfry:
    for i in range(len(cyfra)-1):
        suma += int(cyfra[i])
        if suma > smax:
            smax = suma
        else:
            smin = suma
    suma = 0
print(f"Suma: {smax, smin}") # nie wiem kirwa
#---------------------------------------------------
count = 0
for i in range(len(cyfry)):
    for a in range(len(cyfry[i])-1):
        if cyfry[i][a] < cyfry[i][a+1]:
            count += 1
            if(count == len(cyfry[i])):
                print(cyfry[i])
                count = 0 #czemu nie dzial xd