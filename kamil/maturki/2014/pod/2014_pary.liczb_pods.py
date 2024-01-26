c = open("PARY_LICZB.TXT", "r").readlines()
c = [x.strip() for x in c]

# A)
# def wielo(c):
#     count = 0
#     for x in c:
#         cyfry = list(map(int, x.split()))
#         if cyfry[0] % cyfry[1] == 0 or cyfry[1] % cyfry[0] == 0:
#             count += 1
#     return count
# result = wielo(c)
# print(result)


# B
count = 0
def suma_cyfr(c):
    return sum(map(int, str(c)))

def czyrowne(c):
