instrukcje = [x.strip() for x in open("instrukcje.txt","r").readlines()]
print(instrukcje)
startowy = 0,0
waz = 0,0
for instrukcja in instrukcje:
    if instrukcja == "P":
        print("Przod")
    if instrukcja == "L":
        print("lewo")
    if instrukcja == "P":
        print("prawo")
    if instrukcja == "J":
        print("jedz")
print()