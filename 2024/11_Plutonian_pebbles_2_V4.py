"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/11

Solution part 2 : 220357186726677

Smart count version
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
import pickle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

# Starting list
f = open("11_data.txt", "r")
string_to_analyze = f.read().strip().split(' ')
list_of_stones = np.asarray([int(i) for i in string_to_analyze])
list_of_stones = [int(i) for i in string_to_analyze]
f.close()

# Load precomputed values
f = open("11_precomputed_values.pkl", "rb")
precomputed_values = pickle.load(f)
f.close()

n_blinks = 75

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def compute_n_blinks(list_of_stones, n_blinks) :
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

    return list_of_stones

def count_stones_per_values(list_of_stones) :
    """
    Count the number of stones per each unique values
    """
    # Get unique values of stones
    stones_values = np.unique(list_of_stones)

    # Count the number of element for each values
    n_stones_per_value = np.zeros(len(stones_values), dtype = int)
    for i in range(len(n_stones_per_value)) :
        current_value = stones_values[i]
        n_stones_per_value[i] = np.sum(list_of_stones == current_value)

    return stones_values, n_stones_per_value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Check the evolution after enough steps
# In this way I can obtain all the values that appears more often

n_step_with_precomputed_value = n_blinks // 5
n_step_classic = n_blinks % 5

# Create the initial dictionary
stones_count_per_value = dict()
stones_values, n_stones_per_value = count_stones_per_values(list_of_stones)
for i in range(len(stones_values)) : stones_count_per_value[stones_values[i]] = n_stones_per_value[i]

for i in range(n_step_with_precomputed_value) :

    tmp_stones_count_per_value = dict()
    # for j in range(len(stones_values)) :
    for current_value_analyzed in stones_count_per_value :
        # Get the current value
        # current_value_analyzed = int(stones_values[j])
        
        # Get the numbero of stones with that values in the list
        if current_value_analyzed not in stones_count_per_value :
            # stones_count_per_value[current_value_analyzed] = 1
            n_stones_per_current_value_analyzed = 1
        else :
            n_stones_per_current_value_analyzed = stones_count_per_value[current_value_analyzed]
        
        # Compute 5 steps
        tmp_list = list(compute_n_blinks(np.asarray([current_value_analyzed]), 5))
        
        # Count the new generated values and save them
        for k in range(len(tmp_list)) :
            tmp_stone_value_generated = tmp_list[k]

            if tmp_stone_value_generated not in tmp_stones_count_per_value :
                tmp_stones_count_per_value[tmp_stone_value_generated] = n_stones_per_current_value_analyzed
            else :
                tmp_stones_count_per_value[tmp_stone_value_generated] += n_stones_per_current_value_analyzed

    # Update the original count
    stones_count_per_value = tmp_stones_count_per_value

    print("i = {}\t{}%".format(i, np.round(((i + 1) * 5) / n_blinks * 100, 2)))

# Compute the final length of the list
total_n_of_stones = 0
for stone_value in stones_count_per_value : total_n_of_stones += stones_count_per_value[stone_value]

print("After {} blinks you have {} stones".format(n_blinks, total_n_of_stones))
