"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

https://adventofcode.com/2024/day/4

Solution for part 2 : 1864
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

total_MAS_cross_count = 0

# Read data
f = open("4_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

# string_to_analyze = """
#                     MMMSXXMASM
#                     MSAMXMSMSA
#                     AMXSXMAAMM
#                     MSAMASMSMX
#                     XMASAMXAMM
#                     XXAMMXXAMA
#                     SMSMSASXSS
#                     SAXAMASAAA
#                     MAMMMXMMMM
#                     MXMXAXMASX
#                     """

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Convert the string in a numpy array

string_divided_by_line = string_to_analyze.strip().split('\n')

n_rows = len(string_divided_by_line)
n_columns = len(string_divided_by_line[0])

array_to_analyze = np.zeros((n_rows, n_columns), dtype = str)

for i in range(n_rows) :
    for j in range(n_columns) :
        array_to_analyze[i, j] = string_divided_by_line[i][j]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Function to search XMAS word

def search_MAS_cross(array_to_analyze) :
    """
    Search cross formed by the MAS word. 
    The cross are consider up to down, e.g.
    M . M
    . A .
    S . S
    """

    cross_count = 0
    for i in range(array_to_analyze.shape[0]) :
        for j in range(array_to_analyze.shape[1]) :
            # Check if the letter is an M
            if array_to_analyze[i, j] == 'M' :

                # Check if there is enough space for the XMAS word
                if i + 2 < array_to_analyze.shape[0] and j + 2 < array_to_analyze.shape[1] :
                    # Check the first MAS (left to righ)
                    first_MAS_found = False
                    if array_to_analyze[i + 1, j + 1] == 'A' and array_to_analyze[i + 2, j + 2] == 'S' : first_MAS_found = True

                    # Check the second MAS (left to righ)
                    second_MAS_found = False
                    if array_to_analyze[i, j + 2] == 'M' and array_to_analyze[i + 1, j + 1] == 'A' and array_to_analyze[i + 2, j] == 'S' : second_MAS_found = True
                    
                    # Increase cross count
                    if first_MAS_found and second_MAS_found : cross_count += 1

    return cross_count

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count MAS cross

cross_count_1 = search_MAS_cross(array_to_analyze)
cross_count_2 = search_MAS_cross(np.rot90(array_to_analyze))
cross_count_3 = search_MAS_cross(np.rot90(np.rot90(array_to_analyze)))
cross_count_4 = search_MAS_cross(np.rot90(np.rot90(np.rot90(array_to_analyze))))

total_MAS_cross_count = cross_count_1 + cross_count_2 + cross_count_3 + cross_count_4

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Print resulta

print(f"MAS cross count 1 : {cross_count_1}")
print(f"MAS cross count 2 : {cross_count_2}")
print(f"MAS cross count 3 : {cross_count_3}")
print(f"MAS cross count 4 : {cross_count_4}")
print(f"Total MAS cross count : {total_MAS_cross_count}")
