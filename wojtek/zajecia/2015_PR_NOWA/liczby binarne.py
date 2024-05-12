liczby =[x.strip() for x in open("liczby.txt","r").readlines()]
count = 0
for liczba in liczby:
    if liczba.count("0") > liczba.count("1"):
        count += 1
print(count)
#-----------------------
p2=0
p8=0
p28 = 0
for liczba in liczby:
    if int(liczba,2) % 2 == 0:
        p2 +=1
    if int(liczba,2) % 8 == 0:
        p8 +=1
    if int(liczba, 2) % 8 == 0 and int(liczba,2) % 2 == 0:
        p28 += 1
print(p2,p8)
#-----------------------
liczbyarr = []
for liczba in liczby:
    liczbyarr.append(int(liczba,2))
print(max(liczbyarr),min(liczbyarr))
print(liczby.index(bin(max(liczbyarr))[2:])+1) #bo numer wiersza nie index !!! numery wiersza nie leca od 0
print(liczby.index(bin(min(liczbyarr))[2:])+1)