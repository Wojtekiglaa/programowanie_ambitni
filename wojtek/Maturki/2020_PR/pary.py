pary = [x.split() for x in open("pary.txt", "r").readlines()]
print(pary)
tesame = False
# for x in pary:
#     a = x[1]
#     for b in len(a)+1:
#         if a[b] == a[b+1]:
#             tesame = True
#         else:
#             tesame = False
def longest_substring(strng):
    len_substring=0
    longest=0
    for i in range(len(strng)):
        if i > 0:
            if strng[i] != strng[i-1]:
                len_substring = 0
        len_substring += 1
        if len_substring > longest:
            longest = len_substring
    return longest
for x in pary:
    print(longest_substring(x[1]))