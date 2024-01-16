dane = open("hasla.txt", "r").readlines()
parzyste = 0
nieparzyste = 0
dane = [x.strip() for x in dane]
for i in range(len(dane)):
    znaki = len(dane[i])
    if(znaki % 2 == 0):
        parzyste += 1
    else:
        nieparzyste += 1
print(f"Parzyste: {str(parzyste)} \nNieparzyste: {str(nieparzyste)}")

for i in range(len(dane)):
    x = dane[i]
    if(x == x[::-1]):
        print(dane[i])

for i in range(len(dane)):
    for a in range(len(dane[i])-1):
        if(ord(dane[i][a]) + ord(dane[i][a+1])) == 220:
            print(dane[i])
            break #zeby wiecej w slowie nie szukalo juz