hasla = open("hasla.txt", "r").readlines()
hasla = [x.split() for x in hasla]
# print(hasla)
#--------------------------------------------------
numeryczne = 0
for x in hasla:
    for y in x:
        if y.isdigit():
            numeryczne += 1
print(numeryczne)
#--------------------------------------------------
litery = []
xd = []
for x in hasla:
    if hasla.count(x) > 1:
        litery.append(x) #nwm czemu 2 razy appenduje xddddd
for i in litery:
    if i not in xd:
        xd.append(i)
xd.sort()
print(xd)
#--------------------------------------------------
# for x in hasla:
#     for y in x:
#         if ord(y): sprawdza czy da sie orda, jak da sie to po indexach leci po 3 nastepne
licz = 0
for x in hasla:
    for i in range(len(x[0]) - 3):  # assuming each element in hasla is a list of single string
        # Get ASCII values of current character and next three characters
        ascii_values = sorted([ord(x[0][i]), ord(x[0][i+1]), ord(x[0][i+2]), ord(x[0][i+3])])
        # Check if they form a sequence
        if ascii_values[0] + 1 == ascii_values[1] and ascii_values[1] + 1 == ascii_values[2] and ascii_values[2] + 1 == ascii_values[3]:
            licz += 1
            break  # Move to next password
print(licz)
#--------------------------------------------------
haslo = 0
mala = False
duza = False
numeryczne = False
for x in hasla:
    mala = False
    duza = False
    numeryczne = False
    for y in x[0]: #??????????
        if y.islower():
            mala = True
        if y.isupper():
            duza = True
        if y.isdigit():
            numeryczne = True
    if mala and duza and numeryczne:
        haslo += 1
print(haslo)