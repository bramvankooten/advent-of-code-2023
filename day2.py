import re

# file = open('data/day2_1.test', 'r')
file = open('data/day2.in', 'r')

constraints = {
    'red': 12,
    'green': 13,
    'blue': 14
}

lines = file.readlines()

total = 0

for i, line in enumerate(lines):
    num_cubes = [l.split(' ') for l in re.findall(r'\d+ \w+', line)]
    valid = True
    for cubes in num_cubes:

        if int(cubes[0]) > constraints[cubes[1]]:
            valid = False
            break
    if valid:
        total += i + 1
    

print(total)