napisy = open("NAPIS.txt", "r").readlines()
napisy = [x.strip() for x in napisy]

# # A -------------------
# def czyPier(liczby):
#     n = int(liczby / 2 + 1)
#     while n > 1:
#         if liczby % n == 0:
#             return False
#         n -= 1
#     return True
# ile = 0
# for napis in napisy:
#     temp = 0
#     for i in napis.rstrip():
#         temp += ord(i)
#     if czyPier(temp):
#         ile += 1
# print(ile)


# B ---------------------------
ile = 0
for i in napisy:
    for a in range(len(i.rstrip()-1)):
        if x[a] < x[a+]:
