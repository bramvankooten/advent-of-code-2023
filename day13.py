import re
import numpy as np

# file = open('data/day13_1.test', 'r')
file = open('data/day13.in', 'r')

grids = []
grid = []

num_smudges = 1

for l in file.readlines():
    if not l.strip():
        grids.append(grid)
        grid = []
    else:
        grid.append(l.strip())
grids.append(grid)

def check_mirrored(valley, index, smudge):
    left = np.flip(valley[:index])
    right = valley[index:]
    zipped = zip(left, right)
    if smudge:
        global num_smudges
        different = sum(list(map(lambda x: 0 if x[0] == x[1] else 1, zipped)))
        if different == 0:
            return True
        elif different == 1:
            if num_smudges == 1:
                num_smudges = 0
                return True
            else:
                return False
        else:
            return False
    else:
        for (a,b) in zipped:
            if a != b:
                return False
        return True

def vertical_mirrors(grid, smudge):
    for i in range(1,len(grid[0,:])):
        global num_smudges
        num_smudges = 1
        if check_mirrored(grid[0,:], i, smudge):
            for j in range(1,len(grid[:,0])):
                if check_mirrored(grid[j,:], i, smudge):
                    continue
                break
            else:
                if not smudge:
                    return i
                else:
                    if num_smudges == 0:
                        return i

def horizontal_mirrors(grid, smudge):
    for i in range(1,len(grid[:,0])):
        global num_smudges
        num_smudges = 1
        if check_mirrored(grid[:,0], i, smudge):
            for j in range(1,len(grid[0,:])):
                if check_mirrored(grid[:,j], i, smudge):
                    continue
                break
            else:
                if not smudge:
                    return i
                else:
                    if num_smudges == 0:
                        return i

part_one_result = 0

for g in grids:
    grid = np.array(list(map(lambda x: np.array(list(x)), g)))

    vert = vertical_mirrors(grid, False)
    if vert:
        part_one_result += vert

    hori = horizontal_mirrors(grid, False)
    if hori:
        part_one_result += 100*hori

print('Part one:', part_one_result)

part_two_result = 0

for g in grids:
    num_smudges = 1
    grid = np.array(list(map(lambda x: np.array(list(x)), g)))

    vert = vertical_mirrors(grid, True)
    if vert:
        part_two_result += vert

    hori = horizontal_mirrors(grid, True)
    if hori:
        part_two_result += 100*hori

print('Part two:', part_two_result)