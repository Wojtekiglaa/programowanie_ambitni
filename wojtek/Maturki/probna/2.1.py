instrukcje = [x.split() for x in open("instrukcje_przyklad.txt","r").readlines()]
print(instrukcje)
startowy = 0,0
waz = 0,0
for x in instrukcje:
    if x == "P":
        print("Przod")
    # if instrukcje[x] == "L":
    #
    # if instrukcje[x] == "P":
    #
    # if instrukcje[x] == "J":