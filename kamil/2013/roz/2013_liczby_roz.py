liczby = open("dane.txt", "r").readlines()
liczby = [x.strip() for x in liczby]

# A
# ile = 0
# for a in liczby:
#     if a[0] == a[-1]:
#         ile += 1
# print(ile)

# B
# ile = 0
# for x in liczby:
#     if str(int(x,8))[0] == str(int(x,8))[-1]:
#         ile += 1
# print(ile)

# C
for q in liczby:
    for a in range(len(q)-1):
        if
