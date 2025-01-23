"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/11

Solution part 2 :

Single item computation. Still too slow to reach 75
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

def evaluate_n_blink(stone_number, n_blinks, print_var = False) :
    list_of_stones = np.asarray([stone_number])

    for i in range(n_blinks) :
        new_list_of_stones = []
        
        # Check which number shoud be split in two
        n_digits_per_stones = np.int32(np.log10(list_of_stones)) + 1
        n_digits_per_stones[list_of_stones == 0] = 1
        idx_to_split = n_digits_per_stones % 2 == 0
        
        # Array used to compute the stones values after split
        pow_array = n_digits_per_stones[idx_to_split] / 2
        divisor_array = np.pow(np.ones(len(pow_array)) * 10, pow_array)

        # Get the new stones after the split
        left_stones = np.int64(list_of_stones[idx_to_split] // divisor_array)
        right_stones = np.int64(list_of_stones[idx_to_split] % divisor_array)
        
        # Get the new stones that don't split
        list_of_stones[np.logical_not(idx_to_split)] = list_of_stones[np.logical_not(idx_to_split)] * 2024
        list_of_stones[list_of_stones == 0] = 1
        other_stones = list_of_stones[np.logical_not(idx_to_split)]

        # Create the new array to save the stones
        n_of_new_stones = np.sum(idx_to_split) * 2 +  np.sum(np.logical_not(idx_to_split))
        new_list_of_stones = np.zeros(n_of_new_stones, dtype = int)
        
        # Indices to save stones
        idx_1 = len(left_stones)
        idx_2 = len(left_stones) + len(right_stones)
        
        # Save stones
        new_list_of_stones[0:idx_1] = left_stones
        new_list_of_stones[idx_1:idx_2] = right_stones
        new_list_of_stones[idx_2:] = other_stones
        list_of_stones = new_list_of_stones
        
        if print_var : print("\tn_blinks = {}\tn. of stones = {}\t\t({}%)".format(i + 1, len(list_of_stones), np.round((i + 1) / n_blinks * 100, 2)))

    return list_of_stones

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Precomputer values for number between 0 and 10 (included)
precomputed_values = dict()

total_length = 0
for i in range(len(list_of_stones)) :
    actual_stone = list_of_stones[i]

    if actual_stone in precomputed_values :
        total_length += precomputed_values[actual_stone]
    else :
        final_list_for_actual_stones = evaluate_n_blink(actual_stone, n_blinks, True)
        total_length += len(final_list_for_actual_stones)

    print("i = {}\tActual stone = {}\t Total stones generated = {}\t({}%)".format(i, actual_stone, len(final_list_for_actual_stones), np.round((i + 1) / len(list_of_stones) * 100, 2)))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("After {} blinks you have {} stones".format(n_blinks, total_length))

