arr = []
count = 0
while True:
    print("Podaj zmienne, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        for i in arr:
            if i == 1:
                count += 1
        if(count == len(arr)):
            print("Prawda")
        break
    else:
        arr.append(int(x))