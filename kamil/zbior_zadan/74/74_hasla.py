# hasla = open("hasla.txt", "r").readlines()
# hasla = [x.split() for x in hasla]
#
# #74.1 ------------------------------------
# # num = 0
# # for x in hasla:
# #     for y in x:
# #         if y.isdigit():
# #             num += 1
# # print(num)
#
# # # 74.2 -------------------------------------
# # litery = []
# # a = []
# # for x in hasla:
# #     if hasla.count(x) > 1:
# #         litery.append(x)
# # for i in litery:
# #     if i not in a:
# #         a.append(i)
# # a.sort()
# # print(a)
#
# # 74.3 ------------------------------------------
# # ile = 0
# # male = []
# # duze = []
#
#
# def Fib(n):
#     a = 1
#     b = 1
#     for i in range(n):
#         b = b + a
#         a = b - a
#     return b
# n = int(input('podaj dlugosc ciagu: '))
# print(Fib(n))
# def Fibo(n):
#     a , b = 1, 1
#     for i in range(n - 1):
#         b += a
#         a = b - a
#     return a
# n = int(input("Podaj nr liczby z ciągu Fibonacciego: "))
#
# print(Fibo(n))

# tab = [5, 3, 8, 2, 1, 7]
# n = len(tab)
# for i in range(n - 1):
#     for j in range(n - 1):
#         if tab[j] > tab[j + 1]:
#             zmienna = tab[j]
#             tab[j] = tab[j + 1]
#             tab[j + 1] = zmienna
# for x in tab:
#     print(x, end=" ")

def prime(x):
    for n in range(2, x):
        if x%n==0:
            return False
        return True
def jd(x):
    num = []
    for n in range(2, x):
        if (n%2 != 0 and prime(n)):
            num.append(n)
    for a in num:
        for b in num:
            if a+b == x:
                return a,b
print(jd(20))

