from collections import defaultdict

left = []
right = []

with open('inputs/1.txt') as file:
    for line in file:
        left_num, right_num = line.split()
        left.append(int(left_num))
        right.append(int(right_num))

freqs = defaultdict(lambda: 0)
for num in right:
    freqs[num] += 1

similarity_score = 0
for num in left:
    similarity_score += num * freqs[num]

print(similarity_score)
