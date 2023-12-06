import re
import numpy as np

# file = open('data/day6_1.test', 'r')
file = open('data/day6.in', 'r')

lines = [l.strip() for l in file.readlines()]

time = [int(d) for d in re.findall(r'\d+', lines[0])]
distance = [int(d) for d in re.findall(r'\d+', lines[1])]

total_part_one = 1

for i in range(len(time)):
    distance_reached = lambda x: ((time[i]-x)*x > distance[i]).astype(int)
    reached = distance_reached(np.array(list(range(time[i]))))
    total_part_one *= sum(reached)

print('Part one:', total_part_one)


time = int(''.join(re.findall(r'\d+', lines[0])))
distance = int(''.join(re.findall(r'\d+', lines[1])))

total_part_two = 1

distance_reached = lambda x: ((time-x)*x > distance).astype(int)
reached = distance_reached(np.array(list(range(time))))
total_part_two *= sum(reached)

print('Part two:', total_part_two)