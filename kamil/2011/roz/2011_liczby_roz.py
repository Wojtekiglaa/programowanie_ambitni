l = open("liczby1.txt", "r").readlines()
l = [x.strip() for x in l]

# # A
# count = 0
# for x in l:
#     if int(x)%2==0:
#         count += 1
# print(count)

# # B
# max_10 = 0
# max_2 = 0
# for x in l:
#     if int(x, 2) > max_10:
#         max_10 = int(x, 2)
#         max_2 = x
# print(max_2,max_10)


# C
count = 0
suma = 0
for x in l:
    if len(x)==9:
        count += 1
        suma += int(x, 2)
print(count,bin(suma)[2:])


