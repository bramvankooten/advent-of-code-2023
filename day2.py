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
    requirements = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    num_cubes = [l.split(' ') for l in re.findall(r'\d+ \w+', line)]
    for cubes in num_cubes:
        if int(cubes[0]) > requirements[cubes[1]]:
            requirements[cubes[1]] = int(cubes[0])

    total += (requirements['red'] * requirements['green'] * requirements['blue'])
    

print(total)