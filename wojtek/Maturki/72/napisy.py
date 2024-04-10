import difflib
napisy = [x.strip().split() for x in open("napisy.txt", "r").readlines()]
count = 0
for napis in napisy:
    if len(napis[0])*3 <= len(napis[-1]) or len(napis[-1])*3 <= len(napis[0]):
        count +=1
print(count)
#x.starts/endswith
for napis in napisy:
    if napis[-1].startswith(napis[0]):
        print(napis[0],napis[-1],napis[-1][len(napis[0]):])