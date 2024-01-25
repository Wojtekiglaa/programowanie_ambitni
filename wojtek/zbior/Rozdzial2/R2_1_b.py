x = int(input("Podaj liczbe: "))
sum = 0
for a in range(1,x+1):
    if(a%2==0):
        sum += a
sum += x
print(sum)