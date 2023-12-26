# tak samo jak w a ale trzeba jakos zamienic xd
# https://doubleroot.in/lessons/straight-line/general-form/

import math

n = int(input("Podaj n: "))
gorna = (1+math.sqrt(5))**n-(1-math.sqrt(5))**n
dolna = 2**n*math.sqrt(5)
print(int(gorna/dolna))
# ze wzoru