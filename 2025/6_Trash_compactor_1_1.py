"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/6


"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

import numpy as np
import re
import pyperclip

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./6_data.txt') as f :
    data_txt = f.read().strip().split('\n')

# Create a matrix to save the data
# The numbero of rows was computed from the file
data_np = np.zeros((4, 1000))

# Convert the first 4 lines of the file (numerical data) to numpy array
for i in range(4) : data_np[i] = np.asarray(re.sub(' +', ' ', data_txt[i]).strip().split(' '), dtype = int)

# Get the operatio of perform
operation = np.asarray(re.sub(' +', ' ', data_txt[4]).strip().split(' '))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Computation)

# Get the sum of the summation part
plus_sum = int(np.sum(data_np[:, operation == '+']))

# Get the data required in the multiplication part
data_to_multiply = data_np[:, operation == '*']

# Compute multiplication
tmp_mult = np.ones(data_to_multiply.shape[1])
for i in range(4) : tmp_mult = np.multiply(tmp_mult, data_to_multiply[i])

# Get the sum of the multiplication part
mult_sum = int(np.sum(tmp_mult))

# Get the final result and print it
final_result = plus_sum + mult_sum
print(f'Sum of summation part      : {plus_sum}')
print(f'Sum of multiplication part : {mult_sum}')
print(f'Final result               : {final_result}')

# Copy the final result to clipboard
pyperclip.copy(final_result)
