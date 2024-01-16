h = int(input("Podaj wysokosc trojkata: "))
c = 1
for x in range(1,h):
    for a in range(1,x+1):#przy x+1 jedna linijka za duzo(???)
        print(c, end=" ")
        c+=1
    print()