    import math
liczby = open("liczby.txt", "r").readlines()
liczby = [x.strip() for x in liczby]

# 60.1 ---------------------------
# count = 0
# ostatnie = []
# for x in liczby:
#     if int(x)<1000:
#         count += 1
#         ostatnie.append(int(x))
# print(count, ostatnie[-2],ostatnie[-1])

# 60.2 ----------------------------
#
# def dzielniki(n):
#     dzielniki = []
#     for i in range(1,n+1):
#         if n % i ==0:
#             dzielniki.append(i)
#     return [len(dzielniki), dzielniki]
# for x in liczby:
#     x = int(x)
#     if dzielniki(x)[0] == 18:
#         print(f"{x}: {sorted(dzielniki(x)[1])}")

# 60.3 ------------------------------
