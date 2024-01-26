lines = [x.strip().split() for x in open("anagram.txt", "r").readlines()]

# A
# ile = 0
# for i in lines:
#     ok = True
#     for k in range(len(i)-1):
#         if len(i[k])!=len(i[k+1]):
#             ok = False
#             break
#     if ok:
#         ile +=1
#         print(i)
# print(ile)

# # B
for x in lines:
    q = True
    for a in range(len(x)-1):
        if sorted(x[0])!=sorted(x[a+1]):
            q = False
            break
    if q:
        print(x)