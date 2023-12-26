x = int(input("Podaj liczbe: "))
sum = 0
for a in range(1,x+1):
    if(a%1==0):
        sum += a
print(sum)
# n poczatkowych czyli powiedzmy n jest 5 to bierzemy 2 4 6 8 10??