"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/10

Solution for part 1 : 
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
from numba import jit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("10_data.txt", "r")
string_to_analyze = f.read().strip()
f.close()


string_divided_by_line = string_to_analyze.strip().split('\n')

n_rows = len(string_divided_by_line)
n_columns = len(string_divided_by_line[0])

trails_map = np.zeros((n_rows, n_columns), dtype = str)

for i in range(n_rows) :
    for j in range(n_columns) :
        trails_map[i, j] = string_divided_by_line[i][j]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Functions

def get_starting_position(trails_map) :
    trails_start_bool = trails_map == 0
    trails_start_position = np.where(np.any(trails_start_bool))

    return trails_start_position

def get_tops_coord_for_starting_position(current_i : int, current_j : int, trails_map) :
    """

    @param current_i (int) : current position on the trail (row)
    @param current_j (int) : current position on the trail (column)
    @param trails_map (numpy array) : map of all trails (as defined in the file 10_data.txt)
    """

    top_positions = []
    actual_height = trails_map[current_i, current_j]
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    # Check position

    # Row position
    if current_i < 0 or current_i >= trails_map.shape[0] : return []
    
    # Column position
    if current_j < 0 or current_j >= trails_map.shape[1] : return []

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    if actual_height == 9 : # Reach the top of the trail
        return [[current_i, current_j]]
    else :
        # Check position UP
        new_i, new_j = current_i - 1, current_j
        new_height = trails_map[new_i, new_j]
        if new_height == actual_height + 1 : positions_trails_height_up = get_tops_coord_for_starting_position(new_i, new_j)
        else : positions_trails_height_up = []
        
        # Check position DOWN
        new_i, new_j = current_i + 1, current_j
        new_height = trails_map[new_i, new_j]
        if new_height == actual_height + 1 : positions_trails_height_down = get_tops_coord_for_starting_position(new_i, new_j)
        else : score_dowpositions_trails_height_down = []

        # Check position LEFT
        new_i, new_j = current_i, current_j - 1
        new_height = trails_map[new_i, new_j]
        if new_height == actual_height + 1 : positions_trails_height_left = get_tops_coord_for_starting_position(new_i, new_j)
        else : positions_trails_height_left = []

        # Check position RIGHT 
        new_i, new_j = current_i, current_j + 1
        new_height = trails_map[new_i, new_j]
        if new_height == actual_height + 1 : positions_trails_height_right = get_tops_coord_for_starting_position(new_i, new_j)
        else : positions_trails_height_right = []

        # Count unique positions
        all_positions = [positions_trails_height_up, positions_trails_height_down, positions_trails_height_left, positions_trails_height_right]
        
        return all_positions
        

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

trails_start_position = get_starting_position(trails_map)

