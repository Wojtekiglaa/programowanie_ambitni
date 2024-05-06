napisy = open('napisy.txt', 'r').readlines()
napisy = [x.strip() for x in napisy]

# 4.1 -------------------------------
# ile = 0
# for x in napisy:
#     if len(x)%2==0:
#         ile += 1
# print(ile)
#

#4.2 --------------------------------
# j = 0
# z = 0
# ile = 0
# for x in napisy:
#     for a in range(len(x)):
#         if x[a] == "1":
#             j += 1
#         else:
#             z += 1
#     if j == z:
#         ile += 1
#     j = 0
#     z = 0
# print(ile)

#4.3 -----------------------------------
# zjed = 0
# zzer = 0
# j = 0
# z = 0
# for x in napisy:
#     for a in range(len(x)):
#         if x[a] == "1":
#             j += 1
#         else:
#             z += 1
#     if len(x)==j:
#         zjed += 1
#     elif len(x)==z:
#         zzer += 1
#     j = 0
#     z = 0
# print(f"z jedynek, z zer: {zjed,zzer}")

#4.4 --------------------------------
ile = 0
for a in range(2,17):
    for x in napisy:
        if len(x)==a:
            ile += 1
    print(f"{a}: {ile}")
    ile = 0