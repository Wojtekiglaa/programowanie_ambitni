arr=[]
count = []
def znakslow(arr):
    for i in arr:
        # print(i+" "+str(arr.index(i)))
        if arr.index(i) % 2 == 0:
            count.append(i[1]+i[2])
        return count
while True:
    print("Podaj tekst, jesli chcesz zakonczyc wpisz stop")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        print(znakslow(arr))
        break
    else:
        arr.append(str(x))
#nie wiem czemu nie dziala xd