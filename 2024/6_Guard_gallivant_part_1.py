"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/6

Solution for part 2
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Evaluate guard path

i, j = starting_coord

while(True) :
    # Get actual position
    actual_position = array_to_analyze[i, j]
    
    # Evaluate guard new position
    if actual_position == '^' :
        new_i = i - 1
        new_j = j
    elif actual_position == '<' :
        new_i = i
        new_j = j - 1
    elif actual_position == '>' :
        new_i = i
        new_j = j + 1
    elif actual_position == 'v' :
        new_i = i + 1
        new_j = j
    else :
        raise ValueError("ERROR in the position at {},{}".format(i, j))
    
    # Check if i position is inside mapped area
    if i >= 0 and i < array_to_analyze.shape[0] : i_coord_ok = True
    else : i_coord_ok = False

    # Check if j position is inside mapped area
    if j >= 0 and j < array_to_analyze.shape[1] : j_coord_ok = True
    else : j_coord_ok = False

    if i_coord_ok and j_coord_ok :
        # Inside tha mapped area
        if array_to_analyze[new_i, new_j] == '.' or array_to_analyze[new_i, new_j] == 'X' :
            # The path in front of the guard is free
            array_to_analyze[new_i, new_j] = actual_position
            array_to_analyze[i, j] = "X"

            # Update coordinate
            i, j = new_i, new_j
        elif array_to_analyze[new_i, new_j] == '#' :
            # The path in fron of the guard is blocked
            if actual_position == '^' : new_position = '>'
            elif actual_position == '>' : new_position  = 'v'
            elif actual_position == 'v' : new_position  = '<'
            elif actual_position == '<' : new_position  = '^'
            
            # Change guard direction
            array_to_analyze[i, j] = new_position

            # In this case I don't need to update coordinate because I only rotate
    else :
        # Guard is outside mapped area
        break

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count distinct position

count_distinct_position = np.sum(array_to_analyze == 'X')
print("The number of distinct position visited is : {}".format(count_distinct_position))

