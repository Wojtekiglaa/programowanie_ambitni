instrukcje = open("instrukcje.txt","r").readlines()
instrukcje = [x.strip().split(' ') for x in instrukcje]

# A -----------------------
# dlu = 0
# for x in instrukcje:
#     if x[0] =='DOPISZ':
#         dlu += 1
#     if x[0] == 'USUN':
#         dlu -= 1
# print(dlu)


# B -----------------------------------------------
# temp = 1
# max_len = 1
# rodzaj = ''
# for i in range(len(instrukcje)-1):
#     if instrukcje[i][0] == instrukcje[i + 1][0]:
#         temp += 1
#         if temp > max_len:
#             max_len = temp
#             rodzaj = instrukcje[i][0]
#     else:
#         temp = 1
# print(max_len,rodzaj)

# C ---------------------------------------
# litery = []
# for i in instrukcje:
#     if i[0] == 'DOPISZ':
#         litery.append(i[1])
# naj = max(set(litery), key = litery.count)
# print(naj)
# print(litery.count('Z'))

# D -----------------------
slowo = []
for i in instrukcje:
    if i[0] == 'DOPISZ':
        slowo.append(x[1])
    if i[0] == 'USUN':
        slowo.pop(i[1])
    if i[0] == 'ZMIEN':
        slowo.pop()
        slowo.append(i[1])
    if i[0] == 'PRZESUN' and i[1] == 'Z':


