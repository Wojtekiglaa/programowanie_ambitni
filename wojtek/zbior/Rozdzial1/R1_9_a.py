h = int(input("Podaj wysokosc trojkata: "))
for x in range(1,h+1):
    c = 0
    for a in range(1,x+1):
        print(c+a,end=" ")
    print()