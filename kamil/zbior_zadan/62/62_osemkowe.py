liczby1 = open("liczby1.txt", "r").readlines()
liczby2 = open("liczby2.txt", "r").readlines()
liczby1 = [x.strip() for x in liczby1]
liczby2 = [x.strip() for x in liczby2]
liczby2 = [int(x) for x in liczby2]
liczby1 = [int(x, 8) for x in liczby1]
liczby3 = open("liczby1.txt", "r").readlines()
liczby3 = [x.strip() for x in liczby3]
print(liczby1)
#--------------------------------------------------
print(oct(max(liczby1))[2:], oct(min(liczby1))[2:]) #dobrze sa w decu
# #--------------------------------------------------
# ilosci = []
# pelementy = []
# count = 0
# for x in range(len(liczby2)):
#     if(liczby2[x] <= liczby2[x+1]):
#         pelement = liczby2[x]
#         count += 1
#     else:
#         ilosci.append(count)
#         break
# print(ilosci)
#--------------------------------------------------
# licz = 0
# for x in range(len(liczby1)):
#     if(liczby3[x] == oct(liczby2[x])[2:]):
#         licz += 1
#         break
# print(licz)