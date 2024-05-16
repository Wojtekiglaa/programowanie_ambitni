dane1 = [x.strip().split() for x in open("dane1.txt","r").readlines()]
dane2 = [x.strip().split() for x in open("dane2.txt","r").readlines()]
takiesame = 0
print(dane1)
# for a,b in dane1,dane2:
    # if a[len(a-1)] == b[len(b-1)]