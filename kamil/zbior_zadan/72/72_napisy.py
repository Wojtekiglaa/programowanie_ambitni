napisy = open("napisy.txt", "r").readlines()
napisy = [x.strip().split() for x in napisy]

#72.1 ---------------------------
count = 0
for x in napisy:
    if len(x[0])*3 < len(x[-1]) or len(x[-1])*3 < len(x[0]):
        count += 1
print(count)