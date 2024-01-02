x = int(input("Podaj liczbe: "))
sum = 0
# for a in range(x+1):
#     if(a%2==0): tak tez git ale range n*2
#         sum += a
# print(sum)
# n poczatkowych czyli powiedzmy n jest 5 to bierzemy 2 4 6 8 10??
for i in range(0,x*2,2):
    sum += i
print(sum)