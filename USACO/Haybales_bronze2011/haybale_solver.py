reader = open("I.4")
data = []
for line in reader:
    data.append(int(line))

num_piles = data[0]
bales = data[1:]
print(num_piles)
print(bales)

total_bales = sum(bales)

num_per_pile = total_bales / num_piles

num_to_move = 0
for b in bales:
    diff = b - num_per_pile
    if diff > 0:
        num_to_move += diff
num_to_move = int(num_to_move)

writer = open("answer.4", "w")
writer.write(str(num_to_move))
writer.close()
