import math

x = int(input("Podaj liczbe x: "))
print("najmniejsza liczba bitow wynosi: " +str(int(math.log2(x))+1))
#moglbym nie zamieniac na inta ale wtedy bym mial z przecinkami
# nwm o co mi chodzilo jest funkcja round()