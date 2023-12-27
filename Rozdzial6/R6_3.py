import random
n = int(input("Podaj n: "))
arr = [[0]*n]*n
for x in range(0,n):
    for y in range(0,n):
        if(x>y):
            arr[x][y] = x
        else:
            arr[x][y] = y
print(arr)
#nwm xd
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/
#naprawiamgithub