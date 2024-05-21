instrukcje = [x.strip().split() for x in open("instrukcje.txt","r").readlines()]
dnapisu = 0
for napis in instrukcje:
    if napis[0] == "DOPISZ":
        dnapisu +=1
    if napis[0] == "USUN":
        dnapisu -= 1
print(dnapisu)
#----------------------------
dopisane = []
for napis in instrukcje: #pop,del,remove - usuwanie
    if napis[0] == "DOPISZ":
        dopisane.append(napis[1])
xd = max(set(dopisane),key=dopisane.count)
print(xd,dopisane.count(xd))
#----------------------------
licz = 0
max = 0
r = ''
for x in range(len(instrukcje)-1):
    if instrukcje[x][0] == instrukcje[x+1][0]:
        licz +=1
        if licz > max:
            max = licz
            r = instrukcje[x][0]
    else:
        licz = 1
print(max,r)
#----------------------------
wyraz = []
for slowo in instrukcje:
    if slowo[0] == "DOPISZ":
        wyraz.append(slowo[1])
    if slowo[0] == "USUN":
        wyraz.pop()
    if slowo[0] == "ZMIEN":
        wyraz.pop()
        wyraz.append(slowo[1])
    if slowo[0] == "PRZESUN":
        if slowo[1] == "Z" and slowo[1] in wyraz:
            wyraz[wyraz.index(slowo[1])] = "A"
        elif slowo[1] in wyraz:
            wyraz[wyraz.index(slowo[1])] = chr(ord(slowo[1]) + 1)
        else:
            continue
print(*wyraz)