"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/10

Solution for part 1 : 
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
# from numba import jit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("10_data.txt", "r")
string_to_analyze = f.read().strip()
f.close()


string_divided_by_line = string_to_analyze.strip().split('\n')

n_rows = len(string_divided_by_line)
n_columns = len(string_divided_by_line[0])

trails_map = np.zeros((n_rows, n_columns), dtype = int)

for i in range(n_rows) :
    for j in range(n_columns) :
        trails_map[i, j] = int(string_divided_by_line[i][j])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Functions

def get_starting_position(trails_map) :

    trails_start_position = []
    for i in range(trails_map.shape[0]) :
        for j in range(trails_map.shape[1]) :
            if trails_map[i, j] == 0 :
                trails_start_position.append([i, j])


    return trails_start_position

def get_tops_coord_for_starting_position(current_i : int, current_j : int, trails_map) :
    """

    @param current_i (int) : current position on the trail (row)
    @param current_j (int) : current position on the trail (column)
    @param trails_map (numpy array) : map of all trails (as defined in the file 10_data.txt)
    """

    actual_height = trails_map[current_i, current_j]
    # print(" " * actual_height, actual_height)
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
        # print(" " * actual_height, current_i, current_j)
        if current_i > 0 :
            new_i, new_j = current_i - 1, current_j
            new_height = trails_map[new_i, new_j]
            if new_height == actual_height + 1 : positions_trails_height_up = get_tops_coord_for_starting_position(new_i, new_j, trails_map)
            else : positions_trails_height_up = []
        else :
            positions_trails_height_up = []
        
        # Check position DOWN
        # print(" " * actual_height, current_i, current_j)
        if current_i < trails_map.shape[1] - 1 :
            new_i, new_j = current_i + 1, current_j
            new_height = trails_map[new_i, new_j]
            if new_height == actual_height + 1 : positions_trails_height_down = get_tops_coord_for_starting_position(new_i, new_j, trails_map)
            else : positions_trails_height_down = []
        else :
            positions_trails_height_down = []

        # Check position LEFT
        # print(" " * actual_height, current_i, current_j)
        if current_j > 0 :
            new_i, new_j = current_i, current_j - 1
            new_height = trails_map[new_i, new_j]
            if new_height == actual_height + 1 : positions_trails_height_left = get_tops_coord_for_starting_position(new_i, new_j, trails_map)
            else : positions_trails_height_left = []
        else :
            positions_trails_height_left = []

        # Check position RIGHT 
        # print(" " * actual_height, current_i, current_j)
        if current_j < trails_map.shape[1] - 1 :
            new_i, new_j = current_i, current_j + 1
            new_height = trails_map[new_i, new_j]
            if new_height == actual_height + 1 : positions_trails_height_right = get_tops_coord_for_starting_position(new_i, new_j, trails_map)
            else : positions_trails_height_right = []
        else :
            positions_trails_height_right = []

        # Count unique positions
        all_positions_trails_end = positions_trails_height_up + positions_trails_height_down + positions_trails_height_left + positions_trails_height_right
        
        return all_positions_trails_end

def clear_list_of_trails_end(trail_ends : list) :
    tmp_clear_trails_end = set(tuple(end) for end in trail_ends)
    trail_ends = list(list(end) for end in tmp_clear_trails_end)
    return trail_ends

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Get trails start
trails_start_position = get_starting_position(trails_map)

# Get list of unique ends for each start
trials_ends_per_each_start = []
n_path_for_each_start = []
for idx in range(len(trails_start_position)) :
    i_start, j_start = trails_start_position[idx]
    
    # For each start get the position of trails ends that reach maximum height (9)
    tmp_results = get_tops_coord_for_starting_position(i_start, j_start, trails_map)
    
    # Clear each list of ends from duplicates
    tmp_results_clean = clear_list_of_trails_end(tmp_results)
    trials_ends_per_each_start.append(tmp_results_clean)

    # Get the number of path per each start
    n_path_for_each_start.append(len(tmp_results))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute score (Solution part 1)
total_score = 0
for trial_ends in trials_ends_per_each_start : total_score += len(trial_ends)
print("Total score is ", total_score)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute rating (Solution part 2)
print("Total rating ", np.sum(n_path_for_each_start))

