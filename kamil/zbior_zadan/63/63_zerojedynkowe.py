ciagi = open("ciagi.txt", "r").readlines()
ciagi = [x.split() for x in ciagi]
dwuc = []
for x in ciagi:
    midpoint = len(x) // 2
    if(len(x) % 2 == 0):
        if x == x[::-1]:
            dwuc.append(x)
        # if x[:midpoint] == x[midpoint:]:
        #     dwuc.append(x)
        # else:
        #     continue
print(dwuc)
#---------------------
ciongi = []
liczbacount = 0
for x in ciagi:
    for liczba in x:
        if "11" not in liczba:
            liczbacount += 1
print(liczbacount)
#---------------------
ciagi = [str(x) for x in ciagi]
ciagi = [int(x,2) for x in ciagi]
print(ciagi)
