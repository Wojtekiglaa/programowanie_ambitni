arr = []
while True:
    print("Podaj liczby, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        print(arr)
        break
    else:
        try:
            arr.append(int(x)) #typeof nie dziala bo to string przeciez
        except ValueError:
            continue