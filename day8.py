import re
import numpy as np

# file = open('data/day8_1.test', 'r')
# file = open('data/day8_2.test', 'r')
# file = open('data/day8_3.test', 'r')
file = open('data/day8.in', 'r')

lines = [l.strip() for l in file.readlines()]

instructions = list(lines[0])
coordinates = [re.findall(r'\w+', line) for line in lines[2:]]
coords_dict = {}

for c in coordinates:
    coords_dict[c[0]] = {
        'L': c[1],
        'R': c[2]
    }

found = False
current_node = 'AAA'
part_one_steps = 0

while not found:
    for i in instructions:
        part_one_steps += 1
        next_node = coords_dict[current_node][i]
        if next_node == 'ZZZ':
            found = True
            break
        current_node = next_node

print('Part one:', part_one_steps)


current_nodes = list(filter(lambda x: x.endswith('A'), coords_dict.keys()))
factors = []

for node in current_nodes:
    num_steps = 0
    found = False
    current_node = node

    while not found:
        for i in instructions:
            num_steps += 1
            next_node = coords_dict[current_node][i]
            if next_node.endswith('Z'):
                found = True
                factors.append(num_steps)
                break
            current_node = next_node

print('Part Two:', np.lcm.reduce(factors))