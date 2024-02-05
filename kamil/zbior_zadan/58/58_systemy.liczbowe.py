stacja1 = open("dane_systemy1.txt", "r").readlines()
stacja1 = [x.strip().split(' ') for x in stacja1]

stacja2 = open("dane_systemy2.txt", "r").readlines()
stacja2 = [r.strip().split(' ') for r in stacja2]

stacja3 = open("dane_systemy3.txt", "r").readlines()
stacja3 = [a.strip().split(' ') for a in stacja3]

# 58.1 ----------------------------
temp1,temp2,temp3 = [],[],[]
godz1,godz2,godz3 = [],[],[]
for x in stacja1:
    temp1.append(int(x[1], 2))
    godz1.append(int(x[0], 2))
for r in stacja1:
    temp2.append(int(x[1], 4))
    godz2.append(int(x[0], 4))
for a in stacja1:
    temp3.append(int(x[1], 8))
    godz3.append(int(x[0], 8))
print(min(temp1),min(temp2),min(temp3))

