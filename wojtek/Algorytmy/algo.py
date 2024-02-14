#liczba dzielnikow
def dzielniki(n):
    dzielniki = []
    for i in range(1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    return [len(dzielniki), dzielniki]
#