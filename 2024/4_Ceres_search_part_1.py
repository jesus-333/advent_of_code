"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

https://adventofcode.com/2024/day/4

Solution for part 1 : 2468
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

total_xmas_count = 0

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

def find_horizontal_xmas(array_to_analyze : np.array) :
    """
    Given an array of char search the word XMAS on each line
    """
    horizontal_XMAS_count = 0
    for i in range(array_to_analyze.shape[0]) :
        for j in range(array_to_analyze.shape[1]) :
            # Check if the we find an X letter and there is enough space on the line for the the XMAS word
            # Note that the current idx for X char is at position j...so I need 3 other char aftere that to create the XMAS word
            if array_to_analyze[i, j] == 'X' and j + 3 < array_to_analyze.shape[1]:

                # Check if there is the XMAS word
                if array_to_analyze[i, j + 1] == 'M' and array_to_analyze[i, j + 2] == 'A' and array_to_analyze[i, j + 3] == 'S' :
                    horizontal_XMAS_count += 1

    return horizontal_XMAS_count

def find_diagonal_xmas(array_to_analyze : np.array) :
    """
    Given an array of char search the word XMAS on each diagonal.
    The diagonal is consider from left to right and from up to down
    """
    diagonal_XMAS_count = 0
    for i in range(array_to_analyze.shape[0]) :
        for j in range(array_to_analyze.shape[1]) :
            # Check if the letter is an X
            if array_to_analyze[i, j] == 'X' :

                # Check if there is enough space for the XMAS word
                if i + 3 < array_to_analyze.shape[0] and j + 3 < array_to_analyze.shape[1] :
                    # Check if there is the XMAS word
                    if array_to_analyze[i + 1, j + 1] == 'M' and array_to_analyze[i + 2, j + 2] == 'A' and array_to_analyze[i + 3, j + 3] == 'S' :
                        diagonal_XMAS_count += 1

    return diagonal_XMAS_count  

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count horizontal and vertical word

# Horizontal
horizontal_XMAS_count = find_horizontal_xmas(array_to_analyze)
horizontal_reverse_XMAS_count = find_horizontal_xmas(np.flip(array_to_analyze, 1))

# Vertical
vertical_XMAS_count = find_horizontal_xmas(np.rot90(array_to_analyze))
vertical_reverse_XMAS_count = find_horizontal_xmas(np.flip(np.rot90(array_to_analyze), 1))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count diagonal

# Left to right and up to down
diagonal_1_XMAS_count = find_diagonal_xmas(array_to_analyze)

# Left to right and down to up
diagonal_2_XMAS_count = find_diagonal_xmas(np.flip(np.flip(array_to_analyze, 0), 1))

# Right to left and up to down
diagonal_3_XMAS_count = find_diagonal_xmas(np.flip(array_to_analyze, 1))

# Righ to left and down to up
diagonal_4_XMAS_count = find_diagonal_xmas(np.flip(array_to_analyze, 0))

# Sum all the XMAS count (split operation in multiple lines to make it more readable)
total_xmas_count = horizontal_XMAS_count + horizontal_reverse_XMAS_count + \
    vertical_XMAS_count + vertical_reverse_XMAS_count + \
    diagonal_1_XMAS_count + diagonal_2_XMAS_count + diagonal_3_XMAS_count + diagonal_4_XMAS_count

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Print results

print(f"Horizontal XMAS count                           : {horizontal_XMAS_count}")
print(f"Horizontal reverse XMAS count                   : {horizontal_reverse_XMAS_count}")
print(f"Vertical XMAS count                             : {vertical_XMAS_count}") 
print(f"Vertical reverse XMAS count                     : {vertical_reverse_XMAS_count}")
print(f"Diagonal 1 (left-->right, up-->down) XMAS count : {diagonal_1_XMAS_count}")
print(f"Diagonal 2 (left-->right, down-->up) XMAS count : {diagonal_2_XMAS_count}")
print(f"Diagonal 3 (right-->left, up-->down) XMAS count : {diagonal_3_XMAS_count}")
print(f"Diagonal 4 (right-->left, down-->up) XMAS count : {diagonal_4_XMAS_count}")
print(f"Total XMAS count                                : {total_xmas_count}")











