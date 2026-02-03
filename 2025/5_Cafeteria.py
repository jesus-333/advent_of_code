"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/5

Solution part 2 : 577

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import numpy as np
import pyperclip

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./5_data_1.txt') as f :
    list_fresh_id_range = f.read().strip().split('\n')

with open('./5_data_2.txt') as f :
    list_available_id = f.read().strip().split('\n')

# Convert range to numpy array
list_fresh_id_range_np = np.zeros((len(list_fresh_id_range), 2))
for i in range(len(list_fresh_id_range)) :
    current_range = list_fresh_id_range[i].split('-')
    list_fresh_id_range_np[i, 0] = int(current_range[0])
    list_fresh_id_range_np[i, 1] = int(current_range[1])

# Sort range
idx_sorted = list_fresh_id_range_np[:, 0].argsort()
list_fresh_id_range_np = list_fresh_id_range_np[idx_sorted]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Computation)

map_available_id = np.zeros(list_fresh_id_range_np.shape)
count_fresh_available_ingredient = 0
for i in range(len(list_available_id)) :
    available_id = int(list_available_id[i])
    
    # Check if the id is bigger of the first column (start of the range)
    map_available_id[:, 0] = list_fresh_id_range_np[:, 0] <= available_id

    # Check if the id is lower of the second column (end of the range)
    map_available_id[:, 1] = list_fresh_id_range_np[:, 1] >= available_id

    if 2 in  map_available_id.sum(1) : count_fresh_available_ingredient += 1
    
    # print("{:.14e}".format(np.int64(available_id)))
    # print(np.concat([map_available_id, list_fresh_id_range_np], 1))

print(f"Number of fresh available ingredient ID : {count_fresh_available_ingredient}")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 2 (Computation)

previous_range = list_fresh_id_range_np[0]
total_valid_ingredient = list_fresh_id_range_np[0, 1] - list_fresh_id_range_np[0, 0] + 1
for i in range(1, len(list_fresh_id_range_np)) :
    actual_range = list_fresh_id_range_np[i]

    if actual_range[0] == actual_range[1] :
        # Some range start and end with the same element.
        total_valid_ingredient += 1
        continue
    elif (actual_range[0] == previous_range[0]) and (actual_range[1] == previous_range[1]) :
        # In some case the we have identical ranges
        continue
    else :
        pass




