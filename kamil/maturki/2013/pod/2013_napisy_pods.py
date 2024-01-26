n = open("napisy.txt", "r").readlines()
n = [x.strip() for x in n]

# A)
# count = 0
# for x in n:
#     if len(x)%2==0:
#         count += 1
# print(count)

# # B)
# j = 0
# z = 0
# ile = 0
# for x in n:
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

# C
# zjed = 0
# zzer = 0
# j = 0
# z = 0
# for x in n:
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


# D
count = 0
for a in range(2,17):
    for x in n:
        if len(x)==a:
            count += 1
    print(f"{a}: {count}")
    count = 0