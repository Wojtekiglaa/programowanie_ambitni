arr = []
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        print(arr[2])
        break
    else:
        arr.append(int(x))