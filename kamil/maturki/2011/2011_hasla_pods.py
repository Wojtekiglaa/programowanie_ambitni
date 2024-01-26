lines = open("hasla.txt", "r").readlines()
for  i in range(len(lines)):
    lines[i] = lines[i].rstrip()
print(lines)

#  A
# p = 0
# o = 0
# for l in lines:
#     if len(l)%2==0:
#         p += 1
#     else:
#         o += 1
# print("patrzyste: ", p)
# print("nieparzyste: ", o)

# B
# for s in lines:
#     if s == s[::-1]:
#         print(s)


# C
x = 0

for l in lines:
    for i in range(len(l)-1):
        if ord(l[i]) + ord(l[i+1]) == 220:
            x +=1
            print(l)
            break