hasla = open("hasla.txt", "r").readlines()
hasla = [x.split() for x in hasla]

# #74.1 ------------------------------------
# # num = 0
# # for x in hasla:
# #     for y in x:
# #         if y.isdigit():
# #             num += 1
# # print(num)
#
# # # 74.2 -------------------------------------
litery = []
a = []
for x in hasla:
    if hasla.count(x) > 1:
        litery.append(x)
for i in litery:
    if i not in a:
        a.append(i)
a.sort()
print(a)
#
# # 74.3 ------------------------------------------
# # ile = 0
# # male = []
# # duze = []
