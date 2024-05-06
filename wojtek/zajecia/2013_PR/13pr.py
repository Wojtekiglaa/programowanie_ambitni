liczby = [x.strip() for x in open("dane.txt","r").readlines()]
count1 = 0
for liczba in liczby:
    if liczba[0] == liczba[-1]:
        count1 += 1
print(count1)
#-------------------------------
count2 = 0
for liczba in liczby:
    a = str(int(liczba,8))
    if a[0] == a[-1]:
        count2 += 1
print(count2)
#-------------------------------
aaa = []
for liczba in liczby:
    count3 = 0
    for litera in range(0,len(liczba)-1):
        if str(int(liczba[litera])) <= str(int(liczba[litera+1])):
            count3 += 1
    if count3 == len(liczba)-1:
        aaa.append(int(liczba))
print(len(aaa),max(aaa),min(aaa))