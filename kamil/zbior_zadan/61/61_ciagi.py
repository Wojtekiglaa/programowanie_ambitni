ciagi = open("ciagi.txt", "r").readlines()
ciagi = [x.split() for x in ciagi]
bledne = open("bledne.txt", "r").readlines()
bledne = [x.split() for x in bledne]

tylkociagi = []
for x in ciagi:
    if len(x) == 1:
        continue
    else:
        tylkociagi.append(x)
ile = 0

for x in tylkociagi:
    roznica = int(x[1]) - int(x[0])

    if int(x[1]) - int(x[0]) == int(x[2]) - int(x[1]) and int(x[2]) - int(x[1]) == int(x[3]) - int(x[2]):
        ile += 1
print(ile)