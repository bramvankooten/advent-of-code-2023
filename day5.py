import numpy as np
import operator

# file = open('data/day5_1.test', 'r')
file = open('data/day5.in', 'r')

lines = [l.strip() for l in file.readlines()]

seperators = []

for i, line in enumerate(lines):
    if not line:
        seperators.append(i)
seperators.append(len(lines))

seeds_part_one = [int(s) for s in lines[0].split(': ')[1].split()]

for i in range(len(seperators) - 1):
    constraints = [list(map(int, c)) for c in [l.split() for l in lines[seperators[i]+2:seperators[i+1]]]]
    for j, s in enumerate(seeds_part_one):
        for c in constraints:
            if c[1] <= s <= c[1]+c[2]:
                seeds_part_one[j] = c[0] + s - c[1]
                break

print('Part one:', min(seeds_part_one))


def convert_to_new_ranges(original, overlapping_ranges):
    new_ranges = []

    indices = []

    for o in overlapping_ranges:
        start, end = o[0]
        indices.append((start, end, o[1]))
        # indices.append((end, o[1]))

    indices.sort(key=operator.itemgetter(0))
    
    if indices[0][0] != original[0]:
        new_ranges.append((original[0], indices[0][0] - 1))
    
    for i in range(0,len(indices)):
        new_ranges.append((indices[i][0] + indices[i][2], indices[i][1] + indices[i][2]))


    if indices[-1][1] != original[1]:
        new_ranges.append((indices[-1][1] + 1, original[1]))

    return new_ranges



seed_range_values = [int(s) for s in lines[0].split(': ')[1].split()]
seeds_part_two = []

seed_ranges = []

for i in range(int(len(seed_range_values)/2)):
    seed_ranges.append((seed_range_values[i*2],seed_range_values[i*2]+seed_range_values[i*2+1]))

for i in range(len(seperators) - 1):
    constraints = [list(map(int, c)) for c in [l.split() for l in lines[seperators[i]+2:seperators[i+1]]]]
    new_ranges = []
    for r in seed_ranges:
        overlapping_ranges = []
        for c in constraints:
            cons = (c[1], c[1]+c[2])
            if r[0] <= cons[1] and r[1] >= cons[0]:
                overlap = ((max(r[0], cons[0]), min(r[1], cons[1])), c[0]-c[1])
                overlapping_ranges.append(overlap)
                break
        if overlapping_ranges:
            new_ranges.extend(convert_to_new_ranges(r,overlapping_ranges))
        else:
            new_ranges.append(r)
    seed_ranges = new_ranges

distances = [d[0] for d in seed_ranges]

print('Part two:', min(distances))