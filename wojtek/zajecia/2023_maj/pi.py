pi = [x.strip() for x in open("pi_przyklad.txt","r").readlines()]
fragmenty = []
for x in range(0,len(pi)-1):
    fragmenty.append(str(pi[x])+str(pi[x+1]))
print(fragmenty)
count = 0
for fragment in fragmenty:
    if int(fragment) > 90:
        count +=1
print(count)
#--------------------
sorted = sorted(fragmenty)
wystapienia = []
fragmentywystapien = []
# for fragment in sorted:
#     if fragment[0] and fragment[1] in pi:
#         wystapienia.append(pi.count(fragment[0]))
#         fragmentywystapien.append(fragment)
# print(max(wystapienia),min(wystapienia))
#-------------------------------
#zrobic petle co leci po kazdym z pi i jak pi[x] == fragment[0]
# i tak samo z drugim to wtedy count w gore?
for x in range(0,len(pi)-1):
    for y in fragmenty:
        if pi[x] == fragmenty[0] and pi[x+1] == fragmenty[1]:
            wystapienia.append()
print(fragmenty)