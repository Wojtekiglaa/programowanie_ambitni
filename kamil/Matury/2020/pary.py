pary = open('pary.txt','r').readlines()
pary = [x.strip().split(' ') for x in pary]

#ZAD 1
def czy_pierwsza(liczba):
    n = 2
    while (n <= liczba / 2):
        if liczba % n == 0:
            return False
        n += 1
    return True

for x in pary:
    if int(pary[0])%2==0:
        for n in range(2,)
