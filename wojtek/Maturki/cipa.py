def dzielniki(x): #definiujemy funkcje do późniejszego użycia
    for i in range(1, int(x/2) + 1): # iterujemy od jedynki, do polowy liczby x - dzielenie przez wiecej niz polowe nie da calkowitego wyniku
        if x % i == 0: #jezeli liczba i  jest dzielnikiem liczby x
            print(str(i) + " "), #wypisz ja
    print(x), #na koniec wypisujemy liczbe x - ona tez jest swoim dzielnikiem


print("Program znajdujacy dzielniki liczby")
print("Podaj liczbę: ")
a = int(input())
dzielniki(a)