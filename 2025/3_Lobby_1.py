"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/3

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import numpy as np
import pyperclip

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./3_data.txt') as f :
    data_txt = f.read().strip().split('\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 2 (Computation)

largest_joltage_list = []

for idx_row in range(len(data_txt)) :
    row = np.asarray(list(data_txt[idx_row].strip()))
    for i in range(9, 0, -1) :
        # Note that this cycle go from 9 to 1.
        # Even in the worst-case scenario I don't have a single digit number
        # So in the worst-case I will find 10 as a lowest number
        
        # Check if the digit is in the row
        if str(i) in row :
            digit_1 = i
            idx_digit = int(np.argwhere(row == str(i))[0])
            rest_of_the_row = row[(idx_digit + 1):]

            digit_2_found = False

            # The next digit could be only after the first one
            # So I check the rest of the string
            for j in range(9, -1, -1) :
                if str(j) in rest_of_the_row :
                    digit_2 = j
                    digit_2_found = True
                    break
            
            # If I found the second digit I can break the first loop
            if digit_2_found : break
    
    # Compute largest joltage
    print("Found digits :", digit_1, digit_2)
    largest_joltage = int(str(digit_1) + str(digit_2))
    largest_joltage_list.append(largest_joltage)

# Print results and copy the final result to clipboard
print(f'Sum of largest joltages : {np.sum(largest_joltage_list)}')
pyperclip.copy(np.sum(largest_joltage_list))
