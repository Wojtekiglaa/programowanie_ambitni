slowa = open("slowa.txt", "r").readlines()
count = 0
for slowo in slowa:
    if (slowo.count("0") > slowo.count("1")):
        count += 1
print(count)
# --------------------
bloki = 1
licznik = 0
for slowo in slowa:
    if slowo[0] == "0":
        for x in range(len(slowo) - 1):
            if (slowo[x] != slowo[x + 1]):
                bloki += 1
            if bloki > 2:
                licznik += 1
        bloki = 1
        # if (slowo[x] == "0"):
        #     if(zero and slowo):
        #         niepuste.append(slowo[x])
        #     zero = True
        # else:
        #     if(zero and slowo):
        #         niepuste.append(slowo[x])
        #     jeden = True
print(licznik)
# --------------------
xd = 0
for x in slowa:
    if x.count("01") == 1 and x.count("10") == 0:
        xd += 1
print(xd)
# ------------
arr = []
najdluzdzy = 0
obecny = 0
jeden = False
for slowo in slowa:
    # for litera in slowo:
    #     for x in range(len(slowo)):
    #         if x >0:
    #             if slowo[litera][x]
    print(len(max(slowo,"0")))
    print(len(max(slowo,"1")))