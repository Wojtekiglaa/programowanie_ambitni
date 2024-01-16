arr = []
xd = ""
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop, liczbe calkowita wpisz wpisujac liczba")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        xd += str(arr)
    else:
        if(str(x.lower()) == "liczba"):
            calkowita = int(input("Podaj liczbe calkowita: "))
            print(str(xd).find(str(calkowita)))
            break
#nwm co jest xd