arr,arr2 = [],[]
a,b = 0,0
def wylicz(arr,a,b):
    for i in arr:
        if i >= a and i <= b:
            arr2.append(i) #pewnie tu sie dalo bez tej drugiej tablicy ale nie wiem czy jest taka funkcja na podmianke wartosci
        else:
            if(i < a):
                i = a
                arr2.append(i)
            elif(i > b):
                i = b
                arr2.append(i)
    return arr2
while True:
    print("Podaj liczby, jesli chcesz zakonczyc wpisz stop, aby wpisac a i b wpisz ab")
    x = input("Podaj tekst: ")
    if str(x.lower()) == "stop":
        break
    else:
        if(str(x.lower()) == "ab"):
            a,b = int(input("Podaj a: ")),int(input("Podaj b: "))
            print(wylicz(arr,a,b))
            break
        else:
            arr.append(int(x))
#ESSSSSSSSSSSSA