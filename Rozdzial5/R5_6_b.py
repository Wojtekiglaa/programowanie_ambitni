def znajdz_pierwsza(arr):
    c = 0
    for x in range(0, len(arr) + 1):
        if (arr[x] % arr[x] == 0):
            c += 1
    if (c == 2):
        return arr[x]
    else:
        print("Liczba nie jest pierwsza")
arr = []
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        znajdz_pierwsza(arr)
        break
    else:
        arr.append(int(x))
#nie wiem jakos tak