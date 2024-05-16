syngaly = open('sygnaly.txt','r').readlines()
syngaly = [x.strip() for x in syngaly]

# 4.1 -------------------------------------
slowo = ''
for x in range(39,100,40):
    slowo+=syngaly[x][9]
print(slowo)

# 4.2 ------------------------------------
# max = 0
# slowo = str()
# for x in syngaly:
#     x = x.rstrip()
#     if len(set(x))>max:
#         slowo = x
#         max = len(set(x))
# print(max,slowo)

# 4.3 --------------------------------------
