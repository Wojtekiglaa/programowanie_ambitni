arr = []
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        print(max(arr))
        break
    else:
        arr.append(int(x))