liczby1 = open("liczby1.txt","r").readlines()
liczby1 = [x.split() for x in liczby1]
liczby2 = open("liczby2.txt","r").readlines()
liczby2 = [x.split() for x in liczby2]

#62.1 ------------------------------
najwieksza = []
for x in liczby1:
    najwieksza.append(x)
print(max(x))