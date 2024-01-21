napisy = open("napisy.txt", "r").readlines()
n = napisy
napisy = [x.strip() for x in napisy]
#---------------------------------------------------
count = 0
for x in napisy:
    if(len(x) % 2 == 0):
        count += 1
print(f"Parzyste: {count}")
#---------------------------------------------------
jedynki = 0
zera = 0
takiesame = 0
for x in napisy:
    for a in range(len(x)):
        if(x[a] == "1"):
            jedynki += 1
        else:
            zera += 1
    if(jedynki == zera):
        takiesame += 1
    jedynki = 0
    zera = 0
print(f"taka sama liczba: {takiesame}")
#---------------------------------------------------
j = 0
z = 0
jt = 0
zt = 0
for x in napisy:
    for a in range(len(x)):
        if(x[a] == "1"):
            j += 1
        else:
            z += 1
    if(j == len(x)):
        jt += 1
    elif(z == len(x)):
        zt += 1
    j = 0
    z = 0
print(f"nie pamietam co tam bylo: {jt, zt}")
#---------------------------------------------------
# nie robie to funkcjami bo te zmienne mi sie beda pierdolic
licz = 0
for a in range(2,16+1):
    for x in napisy:
        if(len(x) == a):
            licz += 1
    print(f"{a}: {licz}")
    licz = 0