import re
import numpy as np

#file = open('data/day11_1.test', 'r')
file = open('data/day11.in', 'r')

lines = [l.strip() for l in file.readlines()]

original_grid = np.zeros((len(lines),len(lines[0])),dtype=str)

for x in range(len(lines)):
    for y in range(len(lines[0])):
        original_grid[x,y] = lines[x][y]

x,y = original_grid.shape

empty_rows = []
for i in range(x):
    if not '#' in original_grid[i,:]:
        empty_rows.append(i)

empty_cols = []
for i in range(y):
    if not '#' in original_grid[:,i]:
        empty_cols.append(i)

grid = np.insert(original_grid,empty_rows,'.', axis=0)
grid = np.insert(grid,empty_cols,'.', axis=1)

galaxies = tuple(zip(*np.where(grid == '#')))

part_one_total = 0

for i in range(len(galaxies)-1):
    for j in range(i+1,len(galaxies)):
        part_one_total += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

print('Part one:', part_one_total)

print('Empty rows:', empty_rows)
print('Empty cols:', empty_cols)

galaxies = tuple(zip(*np.where(original_grid == '#')))
part_two_total = 0

for i in range(len(galaxies)-1):
    for j in range(i+1,len(galaxies)):
        xs = [galaxies[i][0], galaxies[j][0]]
        xs.sort()
        rows = list(filter(lambda x: xs[0] < x < xs[1], empty_rows))
        verti = (xs[1]-xs[0]) + len(rows)*999999
        
        ys = [galaxies[i][1], galaxies[j][1]]
        ys.sort()
        cols = list(filter(lambda y: ys[0] < y < ys[1], empty_cols))
        hori = (ys[1]-ys[0]) + len(cols)*999999
        part_two_total += verti + hori

print('Part two:', part_two_total)
