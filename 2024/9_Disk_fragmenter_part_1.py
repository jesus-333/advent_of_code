"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/9

Solution for part 1 : 6356833654075
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

for i in range(len(disk_map_compact)) :
    tmp_n_blocks = int(disk_map_compact[i])

    for j in range(tmp_n_blocks) :
        # Write in the extended map if the current block is a file (specific numerical id) or free memory (-1)
        if analyze_file :
            disk_map_extended[current_idx_extended] = current_id
        else :
            disk_map_extended[current_idx_extended] = -1
        
        current_idx_extended += 1
    
    # Switch between file and free memory
    if analyze_file :
        analyze_file = False
        current_id += 1
    else :
        analyze_file = True
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Fill empty gaps

# Get the idx of the first non empty block (from the end)
idx_last_used_block = -1 # I check that the last element is a file

# Fill empty gaps
for i in range(len(disk_map_extended)) : 
    # If the current space is empty
    if disk_map_extended[i] == -1 :
        remaining_disk = disk_map_extended[i:]
        if np.all(remaining_disk == -1) : break

        # Put the last used block in the current empty space
        disk_map_extended[i] = disk_map_extended[idx_last_used_block]

        # Clean last used block
        disk_map_extended[idx_last_used_block] = -1

        # Decrease idx last used block
        while (disk_map_extended[idx_last_used_block] == -1) :
            idx_last_used_block -= 1
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute checksum

disk_map_extended[disk_map_extended == -1] = 0
idx_array = np.arange(len(disk_map_extended))

checksum_array = disk_map_extended * idx_array

print("The checksum of the fragmented disk is {}".format(int(np.sum(checksum_array))))


