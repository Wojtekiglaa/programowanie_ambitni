napisy = open('NAPIS.txt','r').readlines()
napisy = [x.strip() for x in napisy]

# 5.1 -----------------------------------
# def pierwsza(liczba):
#     n = int(liczba/2)
#     while n > 1:
#         if liczba % n == 0:
#             return False
#         n -= 1
#     return True
#
# ile = 0
# for x in napisy:
#     suma = 0
#     for a in x.rstrip():
#         suma += ord(a)
#     if pierwsza(suma):
#         ile += 1
# print(ile)

# 5.2 ---------------------------
# def czyros(x):
#     for a in range(len(x)-1):
#         if ord(x[a]) >= ord(x[a+1]):
#             return False
#     return True
#
# def znajdzros(napisy):
#     for i in napisy:
#         i = i.strip()
#         if czyros(i):
#             print(i)
#
# znajdzros(napisy)

# 5.3 ----------------------------
