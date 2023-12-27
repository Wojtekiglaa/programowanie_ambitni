arr = []
def znajdz_podzielna(arr):
    for i in arr:
        if i % 7 == 0:
            return i
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        if(znajdz_podzielna(arr) != None):
            print(znajdz_podzielna(arr))
        else:
            print("Nie ma takiej!!")
        break
    else:
        arr.append(int(x))