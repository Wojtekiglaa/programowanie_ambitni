instrukcje = open('instrukcje.txt','r').readlines()
instrukcje = [x.strip().split(' ') for x in instrukcje]

# 4.1 -----------------------------
# ile = 0
# for x in instrukcje:
#     if x[0] == 'DOPISZ':
#         ile += 1
#     elif x[0] == 'USUN':
#         ile -= 1
# print(ile)

# 4.2 ---------------------------
# temp = 1
# max_ciag = 1
# rodzaj = ''
# for x in range(len(instrukcje)-1):
#     if instrukcje[x][0] == instrukcje[x+1][0]:
#         temp += 1
#         if temp > max_ciag:
#             max_ciag = temp
#             rodzaj = instrukcje[x][0]
#     else:
#         temp = 1
# print(rodzaj,max_ciag)

# 4.3 -----------------------------------------
# litery = []
# for x in instrukcje:
#     if x[0] == 'DOPISZ':
#         litery.append(x[1])
# naj = max(set(litery), key = litery.count)
# print(naj)
# print(litery.count('Z'))

# 4.4 ------------------------------------------
slowo = []
for x in instrukcje:
    if x[0] == 'DOPISZ':
        slowo.append(x[1])
    if x[0] == 'USUN':
        slowo = slowo[:-1:]
    if x[0] == 'ZMIEN':
        slowo.pop()
        slowo.append(x[1])
    if x[0] == 'PRZESUN':
        if x[1] == 'Z' and x[1] in slowo:
            slowo[slowo.index(x[1])] = 'A'
        elif x[1] in slowo:
            slowo[slowo.index(x[1])] = chr(ord(x[1])+1)
        else:
            continue
print(slowo)
print(''.join(slowo))
