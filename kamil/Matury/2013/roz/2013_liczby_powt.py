liczby = open('dane.txt','r').readlines()
liczby = [x.strip() for x in liczby]

#6.1 ------------------------------------
# ile = 0
# for x in liczby:
#     if x[0]==x[-1]:
#         ile +=1
# print(ile)

#6.2--------------------------------------
# ile = 0
# for x in liczby:
#     if str(int(x,8))[0] == str(int(x,8))[-1]:
#         ile += 1
# print(ile)

# 6.3 ------------------------------------
pasuje =[]
for x in liczby:
    ile = 0
    for a in range(len(x)-1):
        if str(int(x))[a] <= str(int(x))[a+1]:
            ile += 1
    if ile == len(x)-1:
        pasuje.append(int(x))
print(len(pasuje), min(pasuje), max(pasuje))