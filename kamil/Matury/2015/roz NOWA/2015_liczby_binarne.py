liczby = open('liczby.txt','r').readlines()
liczby = [ x.strip() for x in liczby]

#4.1 ----------------------------
# ile = 0
# for x in liczby:
#     if x.count('0') >x.count('1'):
#         ile += 1
# print(ile)

# 4.2 ---------------------------
# przez2 = 0
# przez8 = 0
# for x in liczby:
#     if x[len(x)-1] == '0':
#         przez2 += 1
#     if len(x) >= 3:
#         if x[-3:].count('0') == 3:
#             przez8 += 1
# print(przez2, przez8)

# 4.3 ---------------------------
arr =[]
for x in liczby:
    arr.append(int(x,2))
print(max(arr),min(arr))
print(liczby.index(bin(max(arr))[2:])+1)
print(liczby.index(bin(min(arr))[2:])+1)
