filename = "../Data/stop_words.txt"
reader = open(filename)
stop_words = []
for line in reader:
    stop_words.append(line.strip())
print(stop_words[3])
