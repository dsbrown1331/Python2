import string
reader = open("../Data/test.txt")

for line in reader:
    print("-"*10)   
    print(line)
    line = line.strip()
    print(line)
    line = line.translate(line.maketrans('', '', string.punctuation))
    print(line)
    line = line.lower()
    print(line)
    words = line.split()
    print(words)
