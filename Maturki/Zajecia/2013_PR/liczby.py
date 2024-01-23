liczby = open("dane.txt","r").readlines()
liczby = [x.strip() for x in liczby]
count = 0
licz = 0
count2 = 0
pasujace = []
for a in liczby:
    if(a[0] == a[-1]):
        count += 1
print(count)
#--------------------------------------------------
for x in liczby:
    if str(int(x,8))[0] == str(int(x,8))[-1]:
        licz +=1
print(licz)
for b in liczby:
    for a in range(len(b)-1):
        print(b[a],b[a+1])
        if not int(b[a]) <= int(b[a+1]):
            count2 += 1
print(count2)