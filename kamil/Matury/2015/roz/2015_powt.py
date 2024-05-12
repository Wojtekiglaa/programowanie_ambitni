slowa = open('slowa.txt','r').readlines()
slowa = [x.strip() for x in slowa]

#4.1 -------------------------------
# ile = 0
# for x in slowa:
#     if x.count("0") > x.count("1"):
#         ile += 1
# print(ile)

# 4.2 ------------------------------
# d = 0
# for x in slowa:
#     if x.count("01") == 1 and x.count("10") == 0:
#         d += 1
# print(d)

# 4.3 ---------------------------------
