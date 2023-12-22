x = 6
for a in range(1,x+1):
    if(a<2 or a==x):
        print(a*"V")
    else:
        print("V"+" "*(a-2)+"V")