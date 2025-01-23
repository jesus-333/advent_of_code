"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/11

Solution part 2 :

Precomputation used for the initial idea of version 4. 
I later change version 4 to work in another way.
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
import pickle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("11_data.txt", "r")
string_to_analyze = f.read().strip().split(' ')
list_of_stones = np.asarray([int(i) for i in string_to_analyze])
f.close()

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Check the evolution after enough steps
# In this way I can obtain all the values that appears more often

n_blinks = 35
list_of_stones = compute_n_blinks(list_of_stones, n_blinks)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Check which values appears more often

# Get unique values of stones
stones_values = np.unique(list_of_stones)

# Count the number of element for each values
n_stones_per_value = np.zeros(len(stones_values), dtype = int)
for i in range(len(n_stones_per_value)) :
    current_value = stones_values[i]
    n_stones_per_value[i] = np.sum(list_of_stones == current_value)

# Get the most common values
common_stones_values = stones_values[n_stones_per_value > 10]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Precompute the evolution of the most common values
n_blinks_to_precompute = 5
precomputed_list_per_value = dict()
for i in range(len(common_stones_values)) :
    current_value = int(common_stones_values[i])
    precomputed_list = compute_n_blinks(np.asarray([current_value]), n_blinks_to_precompute)
    precomputed_list_per_value[current_value] = [int(value) for value in precomputed_list]
    
# Save precomputed values
with open('11_precomputed_values.pkl', 'wb') as f:
    pickle.dump(precomputed_list_per_value, f)


