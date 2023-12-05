import numpy as np

# file = open('data/day4_1.test', 'r')
file = open('data/day4.in', 'r')

lines = [l.strip().split(': ')[1].split(' | ') for l in file.readlines()]

total_part_one = 0

for line in lines:
    winning = line[0].split()
    numbers = line[1].split()

    intersect = list(set(winning) & set(numbers))
    if intersect:
        total_part_one += 2**(len(intersect)-1)

print('Part one:', total_part_one)


num_cards = np.ones(len(lines))

for i, line in enumerate(lines):
    winning = line[0].split()
    numbers = line[1].split()

    intersect = list(set(winning) & set(numbers))
    if intersect:
        num_cards[i+1:i+len(intersect)+1] += num_cards[i]

print('Part one:', int(sum(num_cards)))