arr = []
def pwystapienie(arr,cal):
    for i in arr:
        if i == cal:
            return arr.index(i)

while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop, liczbe calkowita wpisz wpisujac liczba")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        #arr.append(int(x))
    else:
        if(str(x.lower()) == "liczba"):
            calkowita = int(input("Podaj liczbe calkowita: "))
            print(pwystapienie(arr,calkowita))
            break
#nwm co jest xd