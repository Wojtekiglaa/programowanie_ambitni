liczby = open("dane.txt", "r").readlines()
liczby = [x.strip() for x in liczby]
count = 0
count2 = 0
for a in liczby:
    if(a[0] == a[-1]):
        count += 1
print(count)
#--------------------------------------------------
licz = 0
for x in liczby:
    if str(int(x,8))[0] == str(int(x,8))[-1]:
        licz +=1
print(licz)
#--------------------------------------------------
pasujace = []
for b in liczby:
    count2 = 0
    for a in range(len(b)-1):
        if str(int(b))[a] <= str(int(b))[a+1]:
            count2 += 1
    if count2 == len(b)-1:
        pasujace.append(int(b))
print(len(pasujace), max(pasujace), min(pasujace))