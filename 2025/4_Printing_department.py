"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/4

Solution part 1 : 1516
Solution part 2 : 9122
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./4_data.txt') as f :
    data_txt = f.read().strip().split('\n')

# Convert data in a numpy array of char
data_np_txt = np.asarray([list(row) for row in data_txt])

# Convert data in a numpy array of int
data_np_int = np.zeros(data_np_txt.shape)
data_np_int[data_np_txt == '@'] = 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (computation)

valid_roll = 0

def can_forklift_access_roll(data_np, i, j) :
    count_surroinding_roll = 0
    if i == 0 : # First row
        if j == 0 :
            # Upper left corner
            count_surroinding_roll = data_np[0, 1] + data_np[1, 1] + data_np[1, 0]
        elif j == data_np.shape[1] - 1 :
            # Upper right corner
            count_surroinding_roll = data_np[0, -2] + data_np[1, -2] + data_np[1, -1]
        else :
            # All other position of the first row
            count_surroinding_roll = data_np[0, j - 1] + data_np[0, j + 1] + data_np[1, j - 1] + data_np[1, j] + data_np[1, j + 1]
    elif i == data_np.shape[0] - 1 : # Last row
        if j == 0 :
            # Down left corner
            count_surroinding_roll = data_np[-2, 0] + data_np[-2, 1] + data_np[-1, 1]
        elif j == data_np.shape[1] - 1 :
            # Down right corner
            count_surroinding_roll = data_np[-1, -2] + data_np[-2, -2] + data_np[-2, -1]
        else :
            # All other position of the first row
            count_surroinding_roll = data_np[-1, j - 1] + data_np[-1, j + 1] + data_np[-2, j - 1] + data_np[-2, j] + data_np[-2, j + 1]
    elif j == 0 : # First column
        # Note that the corner were already check in the row first/last row checks
        count_surroinding_roll = data_np[i - 1, 0] + data_np[i - 1, 1] + data_np[i, 1] + data_np[i + 1, 1] + data_np[i + 1, 0]
    elif j == data_np.shape[1] - 1 : # Last column
        # Note that the corner were already check in the row first/last row checks
        count_surroinding_roll = data_np[i - 1, -1] + data_np[i - 1, -2] + data_np[i, -2] + data_np[i + 1, -2] + data_np[i + 1, -1]
    else : # All other position
        count_surroinding_roll += data_np[i - 1, j - 1] + data_np[i - 1, j] + data_np[i - 1, j + 1]
        count_surroinding_roll += data_np[i    , j - 1] + data_np[i    , j + 1]
        count_surroinding_roll += data_np[i + 1, j - 1] + data_np[i + 1, j] + data_np[i + 1, j + 1]

    if count_surroinding_roll < 4 :
        return True
    else :
        return False

for i in range(data_np_int.shape[0]) :
    for j in range(data_np_int.shape[1]) :
        if data_np_int[i, j] == 1 :
            if can_forklift_access_roll(data_np_int, i, j) :
                valid_roll += 1

# Print results
print("The forklift can access {} rolls.".format(valid_roll))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

valid_roll = 0
new_valid_roll = 1
while new_valid_roll > 0 :
    new_valid_roll = 0
    for i in range(data_np_int.shape[0]) :
        for j in range(data_np_int.shape[1]) :
            if data_np_int[i, j] == 1 :
                if can_forklift_access_roll(data_np_int, i, j) :
                    valid_roll += 1
                    new_valid_roll += 1
                    data_np_int[i, j] = 0

print("After removing accessible rolls, the forklift can access {} rolls.".format(valid_roll))
