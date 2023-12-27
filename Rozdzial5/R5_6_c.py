arr = []
def morethanmax(arr):
    avg = sum(arr) / len(arr)
    for i in arr:
        if i > avg:
            return i
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        arr.sort()
        if(morethanmax(arr) != None):
            print(morethanmax(arr))
        else:
            print("Nie ma takiej!!")
        break
    else:
        arr.append(int(x))