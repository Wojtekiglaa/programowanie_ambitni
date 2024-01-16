napisy = open("napisy.txt", "r").readlines()
napisy = [x.strip() for x in napisy]
#---------------------------------------------------
count = 0
for x in napisy:
    if(len(x) % 2 == 0):
        count += 1
print(f"Parzyste: {count}")
#---------------------------------------------------
jedynki = 0
zera = 0
takiesame = 0
for x in napisy:
    for a in range(len(x)):
        if(x[a] == "1"):
            jedynki += 1
        else:
            zera += 1
    if(jedynki == zera):
        takiesame += 1
        jedynki = 0
        zera = 0
print(f"taka sama liczba: {takiesame}")
# moze nie stripowac ???? zeby wiedziec kiedy zresetowac counter