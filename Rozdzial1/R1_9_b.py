h = int(input("Podaj wysokosc trojkata: "))
c = 1
for x in range(1,h+1):
    for a in range(1,x):#przy x+1 jedna linijka za duzo(???)
        print(c, end=" ")
        c+=1
    print("\n")