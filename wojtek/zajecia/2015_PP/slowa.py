slowa = [x.strip() for x in open("slowa.txt", "r").readlines()]
nowe = [x.strip() for x in open("nowe.txt", "r").readlines()]
count = 0
for x in range(1,13):
    for slowo in slowa:
        if len(slowo) == x:
            count +=1
    print(f"{x}: {count}")
    count = 0
#--------------------
for slowo in nowe:
    if slowo in slowa:
        count = slowa.count(slowo)
    if slowo[::-1] in slowa: #bez ifa mozna
        licz = slowa.count(slowo[::-1])
    print(slowo,count,licz)
    count = 0
    licz = 0
#-------------------