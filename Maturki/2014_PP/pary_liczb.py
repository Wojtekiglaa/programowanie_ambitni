liczby = open("paryliczb.txt", "r").readlines()
liczby = [x.strip() for x in liczby]
liczby2 = [x.split() for x in liczby]
count = 0
def suma_cyfr(n):
    if n > 0:
        s = (n-1) // 9
        return n-9*s
    return 0
for x in liczby2:
    for a in x:
        for liczba in a:
            if liczba*2 in x[1]:
                count += 1 #aha xd
print(count)
#----------------- drugiego nawet nie zaczynam xd jakies nienormalne
licz = 0
for x in liczby2:
    for a in x:
        if suma_cyfr(int(x[0])) == suma_cyfr(int(x[1])):
            licz += 1
print(licz) #nie wiem xd