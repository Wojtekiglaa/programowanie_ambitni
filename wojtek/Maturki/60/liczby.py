import math
liczby = open("liczby.txt", "r").readlines()
liczby = [x.strip() for x in liczby]
count = 0
for x in liczby:
    if int(x) < 1000:
        count += 1
print(count)
#--------------------------------------------------
ostatnie = []
for x in liczby:
    ostatnie.append(int(x)) #????
print(sorted(ostatnie)[-2:]) #dwie ostatnie nie dzialaja reszta git
#--------------------------------------------------
#znajdz liczbe dzielnikow
def dzielniki(n):
    dzielniki = []
    for i in range(1, n+1):
        if n % i == 0:
            dzielniki.append(i)
    return [len(dzielniki), dzielniki]
for x in liczby:
    x = int(x)
    if dzielniki(x)[0] == 18:
        print(f"{x}: {sorted(dzielniki(x)[1])}")
#--------------------------------------------------
liczby = [int(x.strip()) for x in liczby]
def gcd(a, b):
    return math.gcd(a, b)
# Iterate over the numbers in descending order
for x in sorted(liczby, reverse=True):
    # Check if x is relatively prime to all other numbers
    if all(gcd(x, y) == 1 for y in liczby if y != x):
        # If it is, print it and break the loop
        print(x)
        break
#colpilot to napisal kurwa co sie odpuerdala