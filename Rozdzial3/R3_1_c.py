n = int(input("Podaj n(potega): "))
x = int(input("Podaj x(liczba potegowana): "))
p = 1
for i in range(1,n+1):
    p *= x
    print(p)