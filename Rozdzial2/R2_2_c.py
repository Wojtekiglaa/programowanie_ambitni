x = int(input("Podaj liczbe: "))
sum = 0
for a in range(1,x+1):
    if(a%1==0):
        sum += a
print(sum)
# 3 to poprostu z modulo zabawa a reszta to ostatnie to left(x) o ile jest cos takiego w pyhong