import re
import numpy as np

# file = open('data/day14_1.test', 'r')
file = open('data/day14.in', 'r')

grid = []

for l in file.readlines():
    grid.append(np.array(list(l.strip())))

grid = np.array(grid)

part_one_total = 0

for i in range(len(grid[0,:])):
    line = ''.join(grid[:,i])
    length = len(line)
    for s in line.split('#'):
        count = s.count('O')
        section_sum = sum(list(range(length, length-count, -1)))
        part_one_total += section_sum
        length -= (len(s) + 1)


print('Part One:', part_one_total)

