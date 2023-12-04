import re

# file = open('data/day3_1.test', 'r')
file = open('data/day3.in', 'r')



lines = file.readlines()
digits = []
symbols = []
stars = []

def digit_near_symbol(start, end, digit_range):
    for i in range(start,end+1):
        intersect = list(set(digit_range) & set(symbols[i]))
        if intersect:
            return True
    return False

def find_gears(start, end, star):
    gears = []
    for i in range(start,end+1):
        for d in digits[i]:
            digit_range = list(range(d[0]-1,d[1]+1))
            if star in digit_range:
                gears.append(int(lines[i][d[0]:d[1]]))

    if len(gears) == 2:
        return gears[0] * gears[1]
    else:
        return 0


for line in lines:
    line = line.strip()
    digit = [(m.start(0), m.end(0)) for m in re.finditer('\d+', line)]
    digits.append(digit)
    symbol = [m.start(0) for m in re.finditer('[^\w.]', line)]
    symbols.append(symbol)
    star = [m.start(0) for m in re.finditer('\*', line)]
    stars.append(star)


total_part_one = 0

for i, line in enumerate(lines):
    for d in digits[i]:

        digit_range = list(range(d[0]-1,d[1]+1))
        if i == 0:
            near = digit_near_symbol(i,i+1, digit_range)
        elif i == len(lines) - 1:
            near = digit_near_symbol(i-1,i, digit_range)
        else:
            near = digit_near_symbol(i-1, i+1, digit_range)

        if near:
            total_part_one += int(line[d[0]:d[1]])

print('Part one:', total_part_one)

total_part_two = 0

for i, line in enumerate(lines):
    for s in stars[i]:
        if i == 0:
            gear_value = find_gears(i,i+1, s)
        elif i == len(lines) - 1:
            gear_value = find_gears(i-1,i, s)
        else:
            gear_value = find_gears(i-1, i+1, s)
        total_part_two += gear_value

print('Part two:', total_part_two)
