import re
import numpy as np

# file = open('data/day9_1.test', 'r')
file = open('data/day9.in', 'r')

lines = [list(map(int, l.strip().split())) for l in file.readlines()]

part_one_total = 0

for line in lines:
    differences = [line]
    current_line = line
    while not sum(current_line) == 0:
        next_line = []
        for i in range(len(current_line) - 1):
            next_line.append(current_line[i+1] - current_line[i])
        differences.append(next_line)
        current_line = next_line
    for d in reversed(differences):
        if d:
            part_one_total += d[-1]

print('Part one:', part_one_total)


part_two_total = 0

for line in lines:
    differences = [line]
    current_line = line
    while not sum(current_line) == 0:
        next_line = []
        for i in range(len(current_line) - 1):
            next_line.append(current_line[i+1] - current_line[i])
        differences.append(next_line)
        current_line = next_line

    diff = 0
    for d in reversed(differences):
        if d:
            diff = d[0] - diff
    part_two_total += diff

print('Part two:', part_two_total)