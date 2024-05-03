#kody ascii czyli -65
#ord?
#https://www.w3schools.com/python/ref_func_ord.asp
#szyfr cezara?
klucze1 = [x.strip() for x in open("klucze1.txt","r").readlines()]
klucze2 = [x.strip() for x in open("klucze2.txt","r").readlines()]
sz = [x.strip() for x in open("sz.txt","r").readlines()] #split jak kilka w 1 lini po spacji
tj = [x.strip() for x in open("tj.txt","r").readlines()]
print(klucze1)