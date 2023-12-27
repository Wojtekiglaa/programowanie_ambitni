liczby = []
znaki = []
cl = 0
cz = 0

def zlacz(liczby, znaki):
    operacje = ""
    for i in liczby:
        operacje += str(i)
    return operacje

while True:
    if cl <= 10:
        liczby.append(int(input("Podaj liczbe: ")))
        cl += 1
    elif cz <= 9:
        znaki.append(input("Podaj znak: "))
        cz += 1
    if(cl == 10 and cz == 9):
        print(zlacz(liczby, znaki))
        break
# jakos tak