lines = open('dane.txt','r').readlines()
lines = [x.strip().split() for x in lines]
lines = [[int(y) for y in x] for x in lines]

#6.1 -------------------------------
# x = []
# y = []
# for x in lines:
#     x.append(max(x))
#     y.append(min(x))
# print(max(x),min(y))


#6.2 ---------------------------------
# ile = 0
# for x in range(200):
#     if lines[x] != lines[x][::-1]:
#         ile += 1
# print(ile)

#6.4 ---------------------------------
max = 0
for y in range(0, 320):
    ile = 1
    for x in range(1,200):
        if lines[x-1][y] == lines[x][y]:
            ile + 1
        else:
            if ile > max:
                max = ile
            ile = 1
print(max)