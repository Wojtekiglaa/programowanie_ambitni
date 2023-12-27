import math
arr = []
n = int(input("Podaj n: "))
for x in range(1,n+1):
    gorna = (1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n
    dolna = 2 ** n * math.sqrt(5)
    arr.append(int(gorna/dolna))
if(n in arr):
    print("TAK")
else:
    print("NIE")
#idk