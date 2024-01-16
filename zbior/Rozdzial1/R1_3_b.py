s = int(input("Podaj szerokosc: "))
w = int(input("Podaj wysokosc: "))
for x in range(0,w):
    if(x==0 or x==w-1):
        print("#"*s)
    else:
        print("#"+" "*(s-2)+"#")