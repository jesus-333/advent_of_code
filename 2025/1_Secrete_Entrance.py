"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/1

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./1_data.txt') as f :
    data_txt = f.read().strip().split('\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Computation)

dial_value = 50
count_zero = 0

for i in range(len(data_txt)) :
    dial_move = data_txt[i]

    dial_move_side = dial_move[0]
    dial_move_value = int(dial_move[1:])

    if dial_move_side == 'L' :
        dial_value = (dial_value - dial_move_value) % 100
    elif dial_move_side == 'R' :
        dial_value = (dial_value + dial_move_value) % 100
    else :
        raise ValueError(f"Wrong value for dial_move_side. Get {dial_move_side}")

    if dial_value == 0 : count_zero += 1

print(f'Final dial value : {dial_value}')
print(f'Number of times dial was at 0 : {count_zero}')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 2 (Computation)

dial_value = 50
count_zero = 0

for i in range(len(data_txt)) :
    dial_move = data_txt[i]

    dial_move_side = dial_move[0]
    dial_move_value = int(dial_move[1:])

    if dial_move_side == 'L' :
        dial_value = dial_value - dial_move_value

        if dial_value < 0 :
            count_zero += (np.floor(np.abs(dial_value / 100)) + 1)

    elif dial_move_side == 'R' :
        dial_value = dial_value + dial_move_value

        if dial_value > 100 : count_zero += np.floor(dial_value / 100)
    else :
        raise ValueError(f"Wrong value for dial_move_side. Get {dial_move_side}")

    dial_value = dial_value % 100

    if dial_value == 0 : count_zero += 1
    print(i, dial_move_side, dial_move_value, dial_value, count_zero)

print(f'Final dial value : {dial_value}')
print(f'Number of times dial was at 0 : {count_zero}')
