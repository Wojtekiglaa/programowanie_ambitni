trojki = open("trojki.txt", "r").readlines()
trojki = [x.strip().split() for x in trojki]
def suma_cyfr(liczba):
    suma = 0
    while liczba > 0: # na intach
        suma += liczba % 10 # (*)
        liczba //= 10 # (**)
    return suma
# def suma_cyfr(liczba):
#     suma = 0
#     for cyfra in liczba: na stringa
#         suma += ord(cyfra) - 48  # pobieram kod ASCII danej cyfry i pomniejszam go o 48
#     return suma
for x in trojki:
    if suma_cyfr(int(x[0])) + suma_cyfr(int(x[1])) == suma_cyfr(int(x[2])):
        print(*x)
print("-----")
#--------------------------------------------------
def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for x in trojki:
    if pierwsza(int(x[0])) and pierwsza(int(x[1])) and int(x[2]) == int(x[0]) * int(x[1]):
        print(*x)
#-------------------------------------------------- 2 git
print("-----")
def pitagolas(x):
    if int(x[0])**2 + int(x[1])**2 == int(x[2])**2:
        return True
for x in range(len(trojki)):
    if pitagolas(trojki[x]) and pitagolas(trojki[x+1]):
        print(trojki[x],trojki[x+1])
#-------------------------------------------------- tu jest cos pojebane
licz = 0
for x in trojki:
    bez = x
    bez = [int(x) for x in bez]
    x = [int(x) for x in x]
    bez.remove(max(bez))
    if(int(max(x))<int(sum(bez))):
        licz+=1
print(licz)
#604 jest git ale ciag zrobic