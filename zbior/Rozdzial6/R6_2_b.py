arr = []
while True:
    print("Podaj liczby, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        for i in arr:
            if ord(i) % 2 == 0: #ascii
                print(i, end=" ")
        break
    else:
        arr.append(x)