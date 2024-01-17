import re
import numpy as np

file = open('data/day10_1.test', 'r')
file = open('data/day10_2.test', 'r')
file = open('data/day10.in', 'r')

lines = [list(l.strip()) for l in file.readlines()]

stored_grid = np.zeros((len(lines), len(lines[0])), dtype=str)

constraints = {
    'left': ['-', 'L', 'F', 'S'],
    'right': ['-', '7', 'J', 'S'],
    'bottom': ['|', 'L', 'J', 'S'],
    'top': ['|', '7', 'F', 'S']
}

for i in range(len(lines)):
    for j in range(len(lines[i])):
        stored_grid[i][j] = lines[i][j]

def replace_s(grid, x, y):
    if x == 0:
        if y == 0:
            if grid[x+1][y] in constraints['bottom'] and grid[x][y+1] in constraints['right']:
                return 'F'
        elif y == len(grid[x]) - 1:
            if grid[x+1][y] in constraints['bottom'] and grid[x][y-1] in constraints['left']:
                return '7'
        else:
            if grid[x+1][y] in constraints['bottom'] and grid[x][y+1] in constraints['right']:
                return 'F'
            elif grid[x+1][y] in constraints['bottom'] and grid[x][y-1] in constraints['left']:
                return '7'
            elif grid[x][y+1] in constraints['right'] and grid[x][y-1] in constraints['left']:
                return '-'
    elif x == (len(grid[i]) - 1):
        if y == 0:
            if grid[x-1][y] in constraints['top'] and grid[x][y+1] in constraints['right']:
                return 'L'
        elif y == len(grid[x]) - 1:
            if grid[x-1][y] in constraints['top'] and grid[x][y-1] in constraints['left']:
                return 'J'
        else:
            if grid[x-1][y] in constraints['top'] and grid[x][y+1] in constraints['right']:
                return 'L'
            elif grid[x-1][y] in constraints['top'] and grid[x][y-1] in constraints['left']:
                return 'J'
            elif grid[x][y+1] in constraints['right'] and grid[x][y-1] in constraints['left']:
                return '-'
    elif y == 0:
        if grid[x+1][y] in constraints['bottom'] and grid[x][y+1] in constraints['right']:
            return 'F'
        elif grid[x-1][y] in constraints['top'] and grid[x][y+1] in constraints['right']:
            return 'L'
        elif grid[x+1][y] in constraints['bottom'] and grid[x-1][y] in constraints['top']:
            return '|'
    elif y == len(grid) - 1:
        if grid[x+1][y] in constraints['bottom'] and grid[x][y-1] in constraints['left']:
            return '7'
        elif grid[x-1][y] in constraints['top'] and grid[x][y-1] in constraints['left']:
            return 'J'
        elif grid[x+1][y] in constraints['bottom'] and grid[x-1][y] in constraints['top']:
            return '|'
    else:
        if grid[x+1][y] in constraints['bottom'] and grid[x][y-1] in constraints['left']:
            return '7'
        elif grid[x-1][y] in constraints['top'] and grid[x][y-1] in constraints['left']:
            return 'J'
        elif grid[x+1][y] in constraints['bottom'] and grid[x-1][y] in constraints['top']:
            return '|'
        elif grid[x+1][y] in constraints['bottom'] and grid[x][y+1] in constraints['right']:
            return 'F'
        elif grid[x-1][y] in constraints['top'] and grid[x][y+1] in constraints['right']:
            return 'L'
        elif grid[x][y+1] in constraints['right'] and grid[x][y-1] in constraints['left']:
            return '-'
        
start = None

def update_grid(input, start):
    grid = input.copy()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            token = grid[i][j]
            if token == '.':
                grid[i][j] = token
            elif token == 'S':
                grid[i][j] = replace_s(grid, i, j)
                start = (i,j)
            elif i == 0:
                if token in ['|', 'L', 'J']:
                    grid[i][j] = '.'
                elif token == '-' and 0 < j < (len(grid[i]) - 1):
                    if grid[i][j-1] in constraints['left'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'F' and j < (len(grid[i]) - 1):
                    if grid[i+1][j] in constraints['bottom'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == '7' and j > 0:
                    if grid[i][j-1] in constraints['left'] and grid[i+1][j] in constraints['bottom']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                else:
                    grid[i][j] = '.'
            elif i == (len(grid) - 1):
                if token in ['|', 'F', '7']:
                    grid[i][j] = '.'
                elif token == '-' and 0 < j < (len(grid[i]) - 1):
                    if grid[i][j-1] in constraints['left'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'L' and j < (len(grid[i]) - 1):
                    if grid[i-1][j] in constraints['top'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'J' and j > 0:
                    if grid[i][j-1] in constraints['left'] and grid[i-1][j] in constraints['top']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                else:
                    grid[i][j] = '.'
            elif j == 0:
                if token in ['-', '7', 'J']:
                    grid[i][j] = '.'
                elif token == '|':
                    if grid[i+1][j] in constraints['bottom'] and grid[i-1][j] in constraints['top']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'L':
                    if grid[i-1][j] in constraints['top'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'F':
                    if grid[i+1][j] in constraints['bottom'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                else:
                    grid[i][j] = token
            elif j == (len(grid[i]) - 1):
                if token in ['-', 'L', 'F']:
                    grid[i][j] = '.'
                elif token == '|':
                    if grid[i+1][j] in constraints['bottom'] and grid[i-1][j] in constraints['top']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'J':
                    if grid[i-1][j] in constraints['top'] and grid[i][j-1] in constraints['left']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == '7':
                    if grid[i+1][j] in constraints['bottom'] and grid[i][j-1] in constraints['left']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                else:
                    grid[i][j] = token
            else:
                if token == '-':
                    if grid[i][j-1] in constraints['left'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == '|':
                    if grid[i+1][j] in constraints['bottom'] and grid[i-1][j] in constraints['top']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'L':
                    if grid[i-1][j] in constraints['top'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'F':
                    if grid[i+1][j] in constraints['bottom'] and grid[i][j+1] in constraints['right']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == 'J':
                    if grid[i-1][j] in constraints['top'] and grid[i][j-1] in constraints['left']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                elif token == '7' and j > 0:
                    if grid[i][j-1] in constraints['left'] and grid[i+1][j] in constraints['bottom']:
                        grid[i][j] = token
                    else:
                        grid[i][j] = '.'
                else:
                    grid[i][j] = '.'
    return grid, start

updated_grid, start = update_grid(stored_grid, start)

while not np.array_equal(updated_grid, stored_grid):
    stored_grid = updated_grid
    updated_grid, _ = update_grid(stored_grid, start)

# np.savetxt('test.txt', updated_grid, fmt='%s')

moves = {
    '|': ((-1,0),(1,0)),
    '-': ((0,-1),(0,1)),
    'F': ((1,0),(0,1)),
    'L': ((-1,0),(0,1)),
    'J': ((-1,0),(0,-1)),
    '7': ((1,0),(0,-1))
}

initial_moves = moves[updated_grid[start[0]][start[1]]]
side_one = [start, (start[0] + initial_moves[0][0], start[1] + initial_moves[0][1])]
side_two = [start, (start[0] + initial_moves[1][0], start[1] + initial_moves[1][1])]

run = True

while run:
    if side_one[-1] in side_two:
        run = False
        break
    else:
        # side one
        c = side_one[-1]
        char = updated_grid[c[0]][c[1]]
        move1, move2 = moves[char]
        c1, c2 = (c[0] + move1[0], c[1] + move1[1]), (c[0] + move2[0], c[1] + move2[1])
        if c1 in side_one:
            side_one.append(c2)
        else:
            side_one.append(c1)

        #side two
        c = side_two[-1]
        char = updated_grid[c[0]][c[1]]
        move1, move2 = moves[char]
        c1, c2 = (c[0] + move1[0], c[1] + move1[1]), (c[0] + move2[0], c[1] + move2[1])
        if c1 in side_two:
            side_two.append(c2)
        else:
            side_two.append(c1)

print('Part one:', len(side_one) - 1)

grid_two = np.empty_like(updated_grid)
grid_two[:][:] = '.'
for x,y in side_one:
    grid_two[x][y] = updated_grid[x][y]
for x,y in side_two:
    grid_two[x][y] = updated_grid[x][y]

borders = ['|', 'L', 'J'] 

part_two = 0

for line in grid_two:
    within_borders = False
    count = 0
    for char in line:
        if char == '.' and within_borders:
            count += 1
        elif char in borders:
            within_borders = not within_borders
    part_two += count

print('Part two:', part_two)


