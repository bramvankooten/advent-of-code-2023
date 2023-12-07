import re
import numpy as np

# file = open('data/day7_1.test', 'r')
file = open('data/day7.in', 'r')

lines = [l.strip().split() for l in file.readlines()]

def all_same(items):
    return all(x == items[0] for x in items)

SORT_ORDER = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}

def find_hand_type(hand):
    score = int(hand[1])
    chars = list(hand[0])
    chars.sort(key=lambda val: SORT_ORDER[val])
    if all_same(chars):
        return ('five', hand[0], score)
    elif all_same(chars[:4]) or all_same(chars[1:]):
        return ('four', hand[0], score)
    elif all_same(chars[:3]):
        if all_same(chars[3:]):
            return ('full', hand[0], score)
        else:
            return ('three', hand[0], score)
    elif all_same(chars[1:4]):
        return ('three', hand[0], score)
    elif all_same(chars[2:]):
        if all_same(chars[:2]):
            return ('full', hand[0], score)
        else:
            return ('three', hand[0], score)
    elif all_same(chars[:2]) or all_same(chars[1:3]):
        if all_same(chars[2:4]) or all_same(chars[3:]):
            return ('two', hand[0], score)
        else:
            return ('one', hand[0], score)
    elif all_same(chars[2:4]) or all_same(chars[3:]):
        return ('one', hand[0], score)
    else:
        return ('high', hand[0], score)


HAND_ORDER = {'five': 0, 'four': 1, 'full': 2, 'three': 3, 'two': 4, 'one': 5, 'high': 6}

hands = [find_hand_type(line) for line in lines]
hands.sort(key=lambda x: (HAND_ORDER[x[0]], SORT_ORDER[x[1][0]], SORT_ORDER[x[1][1]], SORT_ORDER[x[1][2]], SORT_ORDER[x[1][3]], SORT_ORDER[x[1][4]]), reverse=True)
# print(hands)

total_part_one = 0

for i in range(len(hands)):
    total_part_one += (hands[i][2] * (i+1))

print('Part one:', total_part_one)

def adapt_jokers(hand):
    rank, string, score, jokers = hand
    if jokers == 0:
        return hand
    elif jokers == 1:
        if rank == 'high':
            return ('one', string, score, jokers)
        elif rank == 'one':
            return ('three', string, score, jokers)
        elif rank == 'two':
            return ('full', string, score, jokers)
        elif rank == 'three':
            return ('four', string, score, jokers)
        elif rank == 'four':
            return ('five', string, score, jokers)
    elif jokers == 2:
        if rank == 'one':
            return ('three', string, score, jokers)
        elif rank == 'two':
            return ('four', string, score, jokers)
        elif rank == 'full':
            return ('five', string, score, jokers)
    elif jokers == 3:
        if rank == 'three':
            return ('four', string, score, jokers)
        elif rank == 'full':
            return ('five', string, score, jokers)
    elif jokers == 4:
        return ('five', string, score, jokers)
    elif jokers == 5:
        return ('five', string, score, jokers)

        
def find_hand_type_two(hand):
    score = int(hand[1])
    chars = list(hand[0])
    jokers = chars.count('J')

    chars.sort(key=lambda val: SORT_ORDER[val])
    if all_same(chars):
        return ('five', hand[0], score, jokers)
    elif all_same(chars[:4]) or all_same(chars[1:]):
        return ('four', hand[0], score, jokers)
    elif all_same(chars[:3]):
        if all_same(chars[3:]):
            return ('full', hand[0], score, jokers)
        else:
            return ('three', hand[0], score, jokers)
    elif all_same(chars[1:4]):
        return ('three', hand[0], score, jokers)
    elif all_same(chars[2:]):
        if all_same(chars[:2]):
            return ('full', hand[0], score, jokers)
        else:
            return ('three', hand[0], score, jokers)
    elif all_same(chars[:2]) or all_same(chars[1:3]):
        if all_same(chars[2:4]) or all_same(chars[3:]):
            return ('two', hand[0], score, jokers)
        else:
            return ('one', hand[0], score, jokers)
    elif all_same(chars[2:4]) or all_same(chars[3:]):
        return ('one', hand[0], score, jokers)
    else:
        return ('high', hand[0], score, jokers)

SORT_ORDER_TWO = {'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}
    
hands = [adapt_jokers(find_hand_type_two(line)) for line in lines]
hands.sort(key=lambda x: (HAND_ORDER[x[0]], SORT_ORDER_TWO[x[1][0]], SORT_ORDER_TWO[x[1][1]], SORT_ORDER_TWO[x[1][2]], SORT_ORDER_TWO[x[1][3]], SORT_ORDER_TWO[x[1][4]]), reverse=True)
total_part_two = 0

for i in range(len(hands)):
    total_part_two += (hands[i][2] * (i+1))

print('Part two:', total_part_two)