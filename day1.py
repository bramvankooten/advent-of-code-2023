import re

# file = open('data/day1_2.test', 'r')
file = open('data/day1_1.in', 'r')

lines = file.readlines()

def convert_to_num(string):
    if string == 'one':
        return '1'
    elif string == 'two':
        return '2'
    elif string == 'three':
        return '3'
    elif string == 'four':
        return '4'
    elif string == 'five':
        return '5'
    elif string == 'six':
        return '6'
    elif string == 'seven':
        return '7'
    elif string == 'eight':
        return '8'
    elif string == 'nine':
        return '9'
    else:
        return string
    
total = 0

for line in lines:
    digits = [d for d in re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)]
    num = int(convert_to_num(digits[0]) + convert_to_num(digits[-1]))
    total += num
    
print(total)