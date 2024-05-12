slowa = [x.strip() for x in open("slowa.txt","r").readlines()]
count1 = 0
for slowo in slowa:
    if slowo.count("0") > slowo.count("1"):
        count1 +=1
print(count1)
count2 = 0
for slowo in slowa:
    rozne = 0
    for x in range(0,len(slowo)-1):
        if slowo[x] != slowo[x+1]:
            # print(rozne)
            rozne +=1
    if rozne == 1:
        if slowo[0] == "0":
            count2 +=1
print(count2)
#--------------------------------------------
najdluzszy_blok = max(len(max(slowo.split('1'))) for slowo in slowa)
for slowo in slowa:
    if len(max(slowo.split('1'))) == najdluzszy_blok:
        print(slowo)
print(najdluzszy_blok)