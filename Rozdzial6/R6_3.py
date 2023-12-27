import random
n = int(input("Podaj n: "))
arr = [[n]*n]*n
for x in arr:
    for y in x:
        print(f'({x},{y})')
        # if(x>y):
        #     arr[x][y] = x
        # else:
        #     arr[x][y] = y
#nwm xd
#https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/