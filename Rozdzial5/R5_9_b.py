arr=[]
count = []
def najczesciej(arr):
    for i in arr:
        count.append(len(i))
    return max(set(count), key=arr.count)
while True:
    print("Podaj tekst, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        arr.sort()
        print(najczesciej(arr))
        break
    else:
        arr.append(str(x))