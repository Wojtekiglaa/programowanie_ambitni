arr=[]
count = []
def znakslow(arr):
    for i in arr: #co 2 element
        # print(i+" "+str(arr.index(i)))
        if arr.index(i) % 2 == 0:
            count.append(i[1:3])
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