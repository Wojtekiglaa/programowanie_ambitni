lines = open("cyfry.txt", "r").readlines()
lines = [x.strip() for x in lines]

# A
# parz = 0
# for i in (cyfry):
#     if int(i)%2==0:
#         parz += 1
#
# print(parz)

# B

smax = 0
smin = 0
suma = 0
lmin = 0
lmax = 0




#  C

# count = 0
# for i in lines:
#     count = 0
#     for a in range(len(i)-1):
#         if int(i[a]) < int(i[a+1]):
#                 count += 1
#     if count == len(i)-1:
#         print(i)