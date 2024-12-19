left = []
right = []

with open('inputs/1-1.txt') as file:
    for line in file:
        left_num, right_num = line.split()
        left.append(int(left_num))
        right.append(int(right_num))

total_distance = sum(abs(r - l) for l, r in zip(sorted(left), sorted(right)))

print(total_distance)
