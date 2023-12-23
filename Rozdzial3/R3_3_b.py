liczby = int(input("Podaj liczbe a: ")), int(input("Podaj liczbe b: "))
def nwd(a, b):
    while a!= b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print(nwd(liczby[0], liczby[1]))
#nie kumam
#koniec na dzisiaj jutro wigilia czas na odpoczynek
#todo: jak dodac .idea do gitignore
