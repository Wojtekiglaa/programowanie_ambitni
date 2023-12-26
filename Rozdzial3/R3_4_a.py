liczby = int(input("Podaj liczbe a: ")), int(input("Podaj liczbe b: "))
def nwd(a, b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print(liczby[0]*liczby[1])/nwd(liczby[0], liczby[1])