arr=[]
def najdluzszy(arr):
    for i in arr:
        if len(i) > len(arr[0]):
            return i
while True:
    print("Podaj tekst, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        arr.sort()
        print(max(len(arr)))
        break
    else:
        arr.append(str(x))
#boze nwm ide zw