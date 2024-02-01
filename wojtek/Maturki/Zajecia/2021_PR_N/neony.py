# instrukcje = open("przyklad.txt","r").readlines()
instrukcje = open("instrukcje.txt","r").readlines()
instrukcje = [x.strip().split() for x in instrukcje]
# print(instrukcje)
dcount = 0
ucount = 0
dlugosc = 0
for x in instrukcje:
    if x[0] == "DOPISZ":
        dlugosc +=1
    if x[0] == "USUN":
        dlugosc -=1
print(dlugosc)
#----------------------
dopisywane = []
for x in instrukcje:
    if x[0] == "DOPISZ":
        dopisywane.append(x[1])
max = max(set(dopisywane), key = dopisywane.count)
print(max,dopisywane.count(max))
#---------------------
wyraz = []
for x in instrukcje:
    if x[0] == "DOPISZ":
        wyraz.append(x[1])
    if x[0] == "USUN":
        wyraz.pop()
    if x[0] == "ZMIEN":
        wyraz.pop()
        wyraz.append(x[1])
    if x[0] == "PRZESUN":
        if (x[1] == "Z" and x[1] in wyraz):
            if x[1] in wyraz:
                wyraz[wyraz.index(x[1])] = "A"
        elif x[1] in wyraz:
            wyraz[wyraz.index(x[1])] = chr(ord(x[1])+1)
        else:
            continue

print(*wyraz)
#------------------------