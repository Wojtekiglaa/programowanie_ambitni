arr = []
count = 0
while True:
    print("Podaj zmienne, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        for i in arr:
            if i == 0:
                count += 1
        if(count == len(arr)):
            print("Jest nieprawda")
        break
    else:
        arr.append(int(x))
#xdd nie wiem czy jest logicznie ale chb tak