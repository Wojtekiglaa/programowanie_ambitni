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
# def czyRos(x):
#     for i in range(len(x)-1):
#         if ord(x[i]) >= ord(x[i+1]):
#             return False
#     return True
# def znajdz_wyrazy_rosnace(napisy):
#     for line in napisy:
#         line = line.strip()
#         if czyRos(line):
#             print(line)
# znajdz_wyrazy_rosnace(napisy)

# C ----------------------------
def znajdz_pow(napisy):
    with open("NAPIS.txt", "r") as file:
        napisy = file.read().splitlines()

    licznik ={}
    powtorzenia = set()
    for napis in napisy:
        if napis in licznik:
            licznik[napis] += 1
        else:
            licznik[napis] = 1
    for powtorzenie in powtorzenia:
        print(powtorzenia)
znajdz_pow(napisy)
