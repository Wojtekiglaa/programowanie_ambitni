slowa = open("slowa.txt", "r").readlines()
slowa = [x.strip() for x in slowa]
nowe = open("nowe.txt", "r").readlines()
nowe = [x.strip() for x in nowe]
#---------------------------------------------------
count = 0
slowacount = 0
for x in range(1,13):
    for slowo in slowa:
        if(len(slowo) == x):
            count += 1
    print(f"{x}: {count}")
    count = 0
#---------------------------------------------------
for slowo in nowe:
    if slowo in slowa:
        slowacount = slowa.count(slowo)
    print(slowo,slowacount)
    slowacount = 0
#---------------------------------------------------
print("\nLustrzane odbicie:\n")
for slowo in nowe:
    if slowo in slowa:
        slowacount = slowa.count(slowo[::-1])
    print(slowo,slowacount)
    slowacount = 0
# cos jest nie tak w tych krotkich ale reszta jest g