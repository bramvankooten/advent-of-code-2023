import re

file = open('data/day1_1.in', 'r')

lines = [l.strip() for l in file.readlines()]

total = 0

for line in lines:
    digits = [d for d in re.findall(r'\d', line)]
    num = int(digits[0] + digits[-1])
    total += num
    
print(total)