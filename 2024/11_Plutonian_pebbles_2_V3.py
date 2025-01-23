"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/11

Solution part 2 :

Recursive version. Still too slow to reach 75
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("11_data.txt", "r")
string_to_analyze = f.read().strip().split(' ')
list_of_stones = np.asarray([int(i) for i in string_to_analyze])
list_of_stones = np.asarray([0])

n_blinks = 75

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def evaluate_n_blink(actual_stone, current_blink, n_blinks_total, cached_value, print_var = False) :
    # if print_var : print(" " * (current_blink + 1), "Current blink = {}\tActual stone = {}".format(current_blink, actual_stone))
    print(len(cached_value))
    actual_stone = int(actual_stone)
    if actual_stone in cached_value : return cached_value[actual_stone]

    if current_blink == n_blinks_total :
        return 1
    if actual_stone == 0 :
        n_stones = evaluate_n_blink(1, current_blink + 1, n_blinks_total, cached_value, print_var)
        if actual_stone not in cached_value and current_blink == n_blinks_total : cached_value[actual_stone] = n_stones
        return n_stones
    elif len(str(actual_stone)) % 2 == 1 :
        n_stones = evaluate_n_blink(actual_stone * 2024, current_blink + 1, n_blinks_total, cached_value, print_var)
        if actual_stone not in cached_value and current_blink == n_blinks_total: cached_value[actual_stone] = n_stones
        return n_stones
    else :
        actual_stone_string = str(actual_stone)
        half_idx = int(len(actual_stone_string) / 2)

        left_number = int(actual_stone_string[0:half_idx])
        left_number_of_stones = evaluate_n_blink(left_number, current_blink + 1, n_blinks_total, cached_value, print_var)
        if left_number not in cached_value and current_blink == n_blinks_total: cached_value[left_number] = left_number_of_stones

        right_number = int(actual_stone_string[half_idx:])
        righ_number_of_stones = evaluate_n_blink(right_number, current_blink + 1, n_blinks_total,cached_value, total_length)
        if right_number not in cached_value and current_blink == n_blinks_total: cached_value[right_number] = righ_number_of_stones

        return left_number_of_stones + righ_number_of_stones


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

total_length = 0
cached_value = dict()
for i in range(len(list_of_stones)) :
    actual_stone = list_of_stones[i]
    total_n_of_stones = evaluate_n_blink(actual_stone, 0, n_blinks, cached_value, True)
    total_length += total_n_of_stones 

    print("i = {}\tActual stone = {}\t Total stones generated = {}\t({}%)".format(i, actual_stone, total_n_of_stones, np.round((i + 1) / len(list_of_stones) * 100, 2)))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("After {} blinks you have {} stones".format(n_blinks, total_length))

