"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/9

Solution for part 2 : 6389911791746
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

def get_empty_space_list(disk_map_extended) :
    map_empty_space_position = []
    map_empty_space_size = []

    gap_found = False
    gap_size = 0
    for i in range(len(disk_map_extended)) :
        if disk_map_extended[i] == -1 :
            # Save only the initial position of the gap
            if not gap_found : map_empty_space_position.append(i)
            
            # Start to measure  the gap size
            gap_found = True
            gap_size += 1
        else :
            # In this case the current block is a file
            # But if gap_found is True it means that the previous block was the last of an empy gap
            # So I save the gap size
            if gap_found :
                gap_found = False
                map_empty_space_size.append(gap_size)
                gap_size = 0
    
    # If the cycle end and gap found is still True it means that all the last part of the disk is empty
    if gap_found : map_empty_space_size.append(gap_size)

    return map_empty_space_position, map_empty_space_size

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

for i in range(len(disk_map_compact)) :
    tmp_n_blocks = int(disk_map_compact[i])
    if i < 4 : print(i, tmp_n_blocks)

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


for i in range(len(map_file_size)) :
    # Get the empty space positions in the current moment
    map_empty_space_position, map_empty_space_size = get_empty_space_list(disk_map_extended)

    # Get info for file I want to move
    position_of_file_to_move = map_file_position[-(i + 1)]
    size_of_file_to_move = map_file_size[-(i + 1)]
    id_file_to_move = disk_map_extended[position_of_file_to_move]
    print("Analyze file {} ({}% of file analyzed)".format(int(id_file_to_move), np.round(100 * i / len(map_file_size) ,2)))

    for j in range(len(map_empty_space_position)) :
        position_of_empty_space = map_empty_space_position[j]
        size_empty_space = map_empty_space_size[j]
        
        # Interrupt the cycle if the empty space is to the right of the file I want to move
        if position_of_empty_space >= position_of_file_to_move : break
        
        # If the gap is big enough move the file
        if size_empty_space >= size_of_file_to_move :
            for k in range(size_of_file_to_move) :
                # Move the file
                disk_map_extended[position_of_empty_space + k] = id_file_to_move

                # Delete the from the original position
                disk_map_extended[position_of_file_to_move + k] = -1

            break       

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute checksum

disk_map_extended[disk_map_extended == -1] = 0
idx_array = np.arange(len(disk_map_extended))

checksum_array = disk_map_extended * idx_array

print("The checksum of the fragmented disk is {}".format(int(np.sum(checksum_array))))


