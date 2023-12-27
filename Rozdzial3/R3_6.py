#ej wsm bez tego r3 moge pisac xd
# https://pl.wikipedia.org/wiki/Metody_obliczania_pierwiastka_kwadratowego
# metoda kurwa srabilonska
# albo do 1/2 potegi
# 2**0.5
n = float(input("Podaj n(potega): "))
x = float(input("Podaj x(liczba potegowana): "))
p = 1
for i in range(1,int(n)+1):
    p *= x
print(p)
# nie wiem co jest nie mozliwe ze pan z stackoverflow nie umie
#https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module