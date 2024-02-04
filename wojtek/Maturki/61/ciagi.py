#dobra to jest w miare es
ciagi = open("ciagi.txt", "r").readlines()
ciagi = [x.split() for x in ciagi]
bledne = open("bledne.txt", "r").readlines()
bledne = [x.split() for x in bledne]
# jakos trzeba tego import zrobic
sameciagi = []
for x in ciagi:
    if len(x) == 1:
        continue
    else:
        sameciagi.append(x)
#---------------------
count = 0
for x in sameciagi:
    roznica = int(x[1]) - int(x[0])

    if int(x[1]) - int(x[0]) == int(x[2]) - int(x[1]):
        count += 1
print(count)