arr = []
def morethanmax(arr):
    avg = sum(arr) / len(arr)
    #return min(collection,key=lambda x:abs(x-num))
    #jakos tak?? idk
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