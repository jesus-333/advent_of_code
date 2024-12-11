"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.
(and for this problem the solution was particularly inefficient)

Original problem https://adventofcode.com/2024/day/6

Solution for part 2 : 1951
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np
from numba import jit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("6_data.txt", "r")
guard_path_string = f.read()
f.close()

starting_guard_position = '^'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Convert data

string_divided_by_line = guard_path_string.strip().split("\n")

n_rows = len(string_divided_by_line)
n_columns = len(string_divided_by_line[0])
array_to_analyze = np.zeros((n_rows, n_columns), dtype = str)

for i in range(n_rows) :
    for j in range(n_columns) :
        array_to_analyze[i, j] = string_divided_by_line[i][j]

starting_coord = list(list(zip(*np.where(array_to_analyze == starting_guard_position)))[0])
array_to_analyze_numeric = np.zeros(array_to_analyze.shape)
array_to_analyze_numeric[array_to_analyze == '.'] = 0
array_to_analyze_numeric[array_to_analyze == '#'] = 1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Evaluate guard path

@jit(nopython=True)
def simulation_obstacle(array_to_analyze, starting_coord) :
    array_to_analyze_backup = array_to_analyze.copy()

    i, j = starting_coord
    n_elements = len(array_to_analyze_backup.flatten())
    max_step = n_elements
    possible_position_for_obstacle = 0

    for idx_row in range(n_rows) :
        for idx_columns in range(n_columns) :
            # Add obstacle (only on free location)
            array_to_analyze = array_to_analyze_backup.copy()
            if array_to_analyze[idx_row, idx_columns] == 0 or (idx_row != starting_coord[0] and idx_columns != starting_coord[1]):
                array_to_analyze[idx_row, idx_columns] = 1
            else :
               continue 
            
            array_to_analyze_previous_step = array_to_analyze.copy()
            current_status = '^'
            continue_cycle = True
            count_if_map_is_the_same = 0
            end_cause = -1
            i, j = starting_coord
            while(continue_cycle) :
                # Evaluate guard new position
                if current_status == '^' :
                    new_i = i - 1
                    new_j = j
                elif current_status == '<' :
                    new_i = i
                    new_j = j - 1
                elif current_status == '>' :
                    new_i = i
                    new_j = j + 1
                elif current_status == 'v' :
                    new_i = i + 1
                    new_j = j
                else :
                    # raise ValueError("ERROR in the position at {},{}".format(i, j))
                    raise ValueError("ERROR in the position at ", i, " ", j)
                
                # Check if i position is inside mapped area
                if new_i >= 0 and new_i < array_to_analyze.shape[0] : i_coord_ok = True
                else : i_coord_ok = False

                # Check if j position is inside mapped area
                if new_j >= 0 and new_j < array_to_analyze.shape[1] : j_coord_ok = True
                else : j_coord_ok = False

                # print(i, j, current_status)
                # print("i_coord_ok ", i_coord_ok)
                # print("j_coord_ok ", j_coord_ok)
                if i_coord_ok and j_coord_ok :
                    # Inside tha mapped area
                    # if array_to_analyze[new_i, new_j] == '.' or array_to_analyze[new_i, new_j] == 'X' :
                    if array_to_analyze[new_i, new_j] == 0 or array_to_analyze[new_i, new_j] == 2 :
                        # The path in front of the guard is free
                        array_to_analyze[i, j] = 2

                        # Update coordinate
                        i, j = new_i, new_j
                    elif array_to_analyze[new_i, new_j] == 1 :
                        # The path in fron of the guard is blocked

                        # Change the current direction
                        if current_status == '^' : current_status = '>'
                        elif current_status  == '>' : current_status  = 'v'
                        elif current_status  == 'v' : current_status  = '<'
                        elif current_status  == '<' : current_status  = '^'

                        # In this case I don't need to update coordinate because I only rotate
                    
                    # Check if the map is the same of the previous step
                    if np.all(array_to_analyze == array_to_analyze_previous_step) :
                        count_if_map_is_the_same += 1
                    else :
                        count_if_map_is_the_same = 0

                    # Checks whether the map has remained the same for max_step iterations
                    if count_if_map_is_the_same >= max_step :
                        continue_cycle = False
                        end_cause = 2
                    
                    # Copy the map of this iteration
                    array_to_analyze_previous_step = array_to_analyze.copy()
                else :
                    # Guard is outside mapped area
                    continue_cycle = False
                    end_cause = 1

            # Check if I end the cycle foor a loop in the path caused by new obstacle
            if end_cause == 2 : possible_position_for_obstacle += 1

            # print("Test idx_row = {} idx_columns = {} ({}% of total elements). Obstacle position discovered = {}".format(idx_row, idx_columns, np.round(100 * (idx_row * n_rows + idx_columns) / n_elements, 2), possible_position_for_obstacle))
            print("Test idx_row = ", idx_row, " idx_columns = ", idx_columns)
            print("Percentage of position analized = ", np.round(100 * (idx_row * n_rows + idx_columns) / n_elements, 2), "%")
            print("Obstacle found = ", possible_position_for_obstacle)
            # print("end_cause = ", end_cause)
            # print("")

            # print(array_to_analyze)
            # raise ValueError("")

    return possible_position_for_obstacle

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count distinct position

possible_position_for_obstacle = simulation_obstacle(array_to_analyze_numeric, starting_coord)
print("The number of possible positions for obstacle is {}".format(possible_position_for_obstacle))

