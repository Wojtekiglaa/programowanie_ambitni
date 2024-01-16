h = int(input("Podaj wysokosc trojkata: "))
for x in range(1,h+1):
    if(x==1 or x==h):
        print(" "*(h-x)+"*"*(2*x-1))
    else:
        print(" "*(h-x)+"*"+" "*(2*x-3)+"*")