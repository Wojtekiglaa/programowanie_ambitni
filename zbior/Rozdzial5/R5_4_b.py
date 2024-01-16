arr = []
def najrzadsza(arr):
    return min(set(arr), key=arr.count)
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        print(najrzadsza(arr))
        break
    else:
        arr.append(int(x))