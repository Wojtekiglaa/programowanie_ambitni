dane = open("piksele.txt", "r").readlines()
# dane = open("przyklad.txt", "r").readlines()
dane = [x.strip().split() for x in dane]
dane = [[int(y) for y in x] for x in dane] # ma to sens aha
x = []
y = []
for x in dane:
    x.append(max(x))
    y.append(min(x))
print(x,y)
print(max(x),min(y)) #skad kurwa sie 10 wzielo
#--------------------------------------------------
