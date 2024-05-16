sygnaly = [x.strip() for x in open("sygnaly.txt","r").readlines()]
slowo = ''
for x in range(39,len(sygnaly),40):
    slowo += sygnaly[x][9]
# for x in slowo:
#     print(x[9])
print(slowo)
#---------------------------------
maxy = []
slowka = []
for x in sygnaly:
    maxy.append(set(x))
    slowka.append(x)
print(len(max(maxy))) #jak ostatni - odwrocic liste i wtedy index!! - sliceing
print(maxy.index(max(maxy))) #index - pierwsze wystapnienie, reverse przy sortowaniu
print(slowka[74]) #funckaj list()!
#jak reversed to spowrotem na liste
#sorted(,reverse=True)
#-------------------------------- kody ascii
roznice = []
for slowo in sygnaly:
    for i in range(0,len(slowo)-1):
        roznica = ord(slowo[i+1]) - ord(slowo[i])
        if roznica <= 10:
            if(sorted(slowo)[0] == sorted(slowo)[-1]):
                roznice.append(slowo)
# print(set(roznice))
# a = set(roznice)
# a = sorted(a,key=str.ca)
# for x in a:
#     print(x)
print(roznice)