arr = []
def print_arr(arr):
    for i in arr:
        print(i, end=" ")
while True:
    print("Podaj liczbe, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj x: ")
    if str(x.lower()) == "stop":
        print_arr(arr)
        break
    else:
        arr.append(int(x))