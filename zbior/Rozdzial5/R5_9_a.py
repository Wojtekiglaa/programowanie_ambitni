arr=[]
count = []
def najdluzszy(arr):
    for i in arr:
        count.append(len(i))
    return max(count)
while True:
    print("Podaj tekst, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        arr.sort()
        print(najdluzszy(arr))
        break
    else:
        arr.append(str(x))