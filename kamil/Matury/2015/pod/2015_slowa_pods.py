slowa = open('slowa.txt','r').readlines()
slowa = [x.strip() for x in slowa]
nowe = open('nowe.txt','r').readlines()
nowe = [x.strip() for x in nowe]

#5.1 -----------------------
# ile = 0
# for a in range(1,13):
#     for x in slowa:
#         if len(x)==a:
#             ile += 1
#     print(f"{a}: {ile}")
#     ile = 0

#5.2 -------------------------
for s in nowe:
    if s in slowa:
        count = slowa.count(s)
    if s[::-1] in slowa:
        licz = slowa.count(s[::-1])
    print(s,count,licz)
    count = 0
    licz = 0