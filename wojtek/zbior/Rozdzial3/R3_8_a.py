import math

n = int(input("Podaj n: "))
gorna = (1+math.sqrt(5))**n-(1-math.sqrt(5))**n
dolna = 2**n*math.sqrt(5)
print(int(gorna/dolna))
# ze wzoru