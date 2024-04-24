sygnaly =  open("sygnaly.txt", "r").readlines()
# print(sygnaly)
# for a in range(40,len(sygnaly)-1,40):
#     print(str(sygnaly[a])[9],end="")
for x in sygnaly:
    if sygnaly.index(x)%40==39:
        print(x[9],end="")

# #--------------------------------------------------
# wiadomosc = ''
# for i, line in enumerate(sygnaly):
#     if i%40 == 0 and len(line) >=10:
#         wiadomosc += line[9]
#
# print(wiadomosc)

# res = ' '.join(i[9] for i in sygnaly[39::40])
# print(res)