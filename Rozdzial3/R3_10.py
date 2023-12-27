a = int(input("Podaj x: "))
c = 0
arr = []
for y in range(1,a+1):
    for x in range(1,a+1):
        if(a%x == 0):
            c+=1
        if(c == 2):
            arr.append(x)
        c = 0
# ok to jakos inaczej trzeba
#chyba ze ja nie umiem xd