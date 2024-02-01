stacja1 = open("dane_systemy1.txt", "r").readlines()
stacja1 = [x.strip().split(' ') for x in stacja1]
stacja2 = open("dane_systemy2.txt", "r").readlines()
stacja2 = [r.strip().split(' ') for r in stacja2]
stacja3 = open("dane_systemy3.txt", "r").readlines()
stacja3 = [a.strip().split(' ') for a in stacja3]
temp1,temp2,temp3 = [],[],[]
godziny1,godziny2,godziny3 = [],[],[]
for x in stacja1:
    temp1.append(int(x[1],2))
    godziny1.append(int(x[0],2))
for x in stacja2:
    temp2.append(int(x[1],4))
    godziny2.append(int(x[0],4))
for x in stacja3:
    temp3.append(int(x[1],8))
    godziny3.append(int(x[0],8))
print(min(temp1),min(temp2),min(temp3))
#--------------------------------------------------
a = 12
count = 0
for x in range(len(godziny1)):
    if godziny1[x] != a and godziny2[x] != a and godziny3[x] != a:
        count += 1
    a += 24
print(count)
#--------------------------------------------------
# reszta jest jakas pojebana zrobie to pozniej xd