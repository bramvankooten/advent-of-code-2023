import re

# file = open('data/day3_1.test', 'r')
file = open('data/day3.in', 'r')



lines = file.readlines()
digits = []
symbols = []

def digit_near_symbol(start, end, digit_range):
    for i in range(start,end+1):
        intersect = list(set(digit_range) & set(symbols[i]))
        if intersect:
            return True
    return False

for line in lines:
    line = line.strip()
    digit = [(m.start(0), m.end(0)) for m in re.finditer('\d+', line)]
    digits.append(digit)
    symbol = [m.start(0) for m in re.finditer('[^\w.]', line)]
    symbols.append(symbol)

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

print('Part one:',total_part_one)