w = int(input("Podaj wysokosc: "))
s = int(input("Podaj szerokosc: "))
g = int(input("Podaj grubosc: "))
for x in range(0,w):
    if(x>=w-3):
        print("#"*s)
    else:
        print("#"*g)