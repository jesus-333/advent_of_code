"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/11

Solution part 1 :
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("11_data.txt", "r")
string_to_analyze = f.read().strip().split(' ')
list_of_stones = [int(i) for i in string_to_analyze]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

n_blinks = 25

for i in range(n_blinks) :
    new_list_of_stones = []

    for j in range(len(list_of_stones)) :

        actual_stone = list_of_stones[j]

        if actual_stone == 0 :
            new_list_of_stones.append(1)
        elif len(str(actual_stone)) % 2 == 0 :
            actual_stone_string = str(actual_stone)
            half_idx = int(len(actual_stone_string) / 2)
            left_number = int(actual_stone_string[0:half_idx])
            right_number = int(actual_stone_string[half_idx:])

            new_list_of_stones.append(left_number)
            new_list_of_stones.append(right_number)
        else :
            new_list_of_stones.append(actual_stone * 2024)

    list_of_stones = new_list_of_stones.copy()
    print("n_blinks = {}\tn. of stones = {}\t\t({}%)".format(i + 1, len(list_of_stones), np.round((i + 1) / n_blinks * 100, 2)))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("After {} blinks you have {} stones".format(n_blinks, len(list_of_stones)))
