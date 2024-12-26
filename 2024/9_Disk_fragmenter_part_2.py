"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/9

Solution for part 1 : 
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
from numba import jit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("9_data.txt", "r")
disk_map_compact = f.read().strip()
f.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute n. of blocks of memory
n_blocks_total = 0
for i in range(len(disk_map_compact)) : n_blocks_total += int(disk_map_compact[i])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Create extended map of the disk

disk_map_extended = np.zeros(n_blocks_total)

current_id = 0
current_idx_extended = 0
analyze_file = True
save_info = True

map_file_position = []
map_file_size = []
map_empty_space_position = []
map_empty_space_size = []

for i in range(len(disk_map_compact)) :
    tmp_n_blocks = int(disk_map_compact[i])

    for j in range(tmp_n_blocks) :
        # Write in the extended map if the current block is a file (specific numerical id) or free memory (-1)
        if analyze_file :
            disk_map_extended[current_idx_extended] = current_id

            if save_info : 
                map_file_position.append(current_idx_extended)
                map_file_size.append(tmp_n_blocks)
                save_info = False
            
        else :
            disk_map_extended[current_idx_extended] = -1

            if save_info : 
                map_empty_space_position.append(current_idx_extended)
                map_empty_space_size.append(tmp_n_blocks)
                save_info = False
        
        current_idx_extended += 1
    
    # Switch between file and free memory
    if analyze_file :
        analyze_file = False
        current_id += 1
    else :
        analyze_file = True

    save_info = True
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Fill empty gaps

idx_gap = 0

for i in range(1, len(map_file_size)) :
    position_of_file_to_move = map_file_position[-i]
    size_of_file_to_move = map_file_size[-i]

    if map_empty_space_size[idx_gap] >= size_of_file_to_move :
        pass
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute checksum

disk_map_extended[disk_map_extended == -1] = 0
idx_array = np.arange(len(disk_map_extended))

checksum_array = disk_map_extended * idx_array

print("The checksum of the fragmented disk is {}".format(int(np.sum(checksum_array))))


