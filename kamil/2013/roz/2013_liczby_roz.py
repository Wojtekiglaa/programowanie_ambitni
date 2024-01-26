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
git = []
for x in liczby:
    count = 0
    for a in range(len(x)-1):
        if str(int(x))[a] <= str(int(x))[a+1]:
            count += 1
    if count == len(x)-1:
        git.append(int(x))
print(len(git), max(git), min(git))



