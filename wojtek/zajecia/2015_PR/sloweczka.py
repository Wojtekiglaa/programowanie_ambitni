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