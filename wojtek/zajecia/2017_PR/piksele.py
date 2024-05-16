piksele = [x.strip().split() for x in open("piksele.txt","r").readlines()]
piksele = [[int(x) for x in y] for y in piksele]
x = []
y = []
for linia in piksele:
    x.append(max(linia))
    y.append(min(linia))
print(max(x),min(y))
#---------------------------------
#tablice dwuwymiarowe pocwiczyc
# for linia in piksele:
#     # print(linia)