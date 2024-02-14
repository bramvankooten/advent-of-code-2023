import re
import numpy as np

# file = open('data/day12_1.test', 'r')
file = open('data/day12.in', 'r')

lines = [l.strip().split(' ') for l in file.readlines()]
lines = list(map(lambda x: [x[0], tuple(map(lambda y: int(y), x[1].split(',')))], lines))

part_two_lines = lines.copy()

cache = {}

def count(conf, nums):
    if conf == "":
        return 1 if nums == () else 0
    
    if nums == ():
        return 0 if '#' in conf else 1
    
    key = (conf, nums)

    if key in cache:
        return cache[key]

    result = 0

    if conf[0] in '.?':
        result += count(conf[1:], nums)

    if conf[0] in '#?':
        if nums[0] <= len(conf) and '.' not in conf[:nums[0]] and (nums[0] == len(conf) or conf[nums[0]] != '#'):
            result += count(conf[nums[0] + 1:], nums[1:])

    cache[key] = result

    return result

part_one_total = 0

for line in lines:
    part_one_total += count(line[0],line[1])

print('Part one:', part_one_total)

part_two_total = 0

for line in part_two_lines:
    part_two_total += count('?'.join([line[0]] * 5), line[1]*5)

print(part_two_total)