arr = []
def najczestsza(arr):
    return max(set(arr), key=arr.count)
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        print(najczestsza(arr))
        break
    else:
        arr.append(int(x))