with open("Document.txt",'r') as f:
    words = [word for line in f
             for word in line.strip().split()]
print(f"Number of words: {len(words)}")
#dobra jest g