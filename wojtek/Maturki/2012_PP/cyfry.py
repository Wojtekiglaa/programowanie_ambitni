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
smin = float("inf")
suma = 0
lmin = ""
lmax = ""
for cyfra in cyfry:
    suma = sum(int(c) for c in cyfra)  # copilot naprawil
    if suma > smax:                    # ej dobre to ten sposob
        smax = suma
        lmax = cyfra
    if suma < smin:
        smin = suma
        lmin = cyfra
print(f"Suma: {smax, smin, lmax, lmin}")
#---------------------------------------------------
count = 0
for i in cyfry:
    count = 0
    for a in range(len(i)-1):
        if int(i[a]) < int(i[a+1]):
            count += 1
    if(count == len(i)-1):
        print(i)#czemu nie dziala xd