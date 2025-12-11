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
# Part 2 (Preprocess)

# Read txt files
with open('./6_data.txt') as f :
    data_txt = f.read().split('\n')


# Get the operatio of perform
operation = np.asarray(list(data_txt[4]))

# Convert the row in list where each character is an element of the list
row_0 = list(data_txt[0])
row_1 = list(data_txt[1])
row_2 = list(data_txt[2])
row_3 = list(data_txt[3])

# Convert the numerical part of the data in a matrix. Each cell is a character of the original string.
# Note tha each row of the original string has the same length
data_txt_matrix = np.asarray([row_0, row_1, row_2, row_3])
# data_txt_matrix = np.asarray([row_0, row_1, row_2])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Computation)

# Variables to store resutls
plus_sum = 0
mult_sum = 0

# Variables for the cycle
current_operation = ''
i = 0
start_block_idx, end_block_idx = -1, -1

while i < len(operation) - 1 :
    # Get the start of the current block of numbers
    if operation[i] == '+' or operation[i] == '*' :
        current_operation = operation[i]
        start_block_idx = i
    
    # Get the end of the current block of number
    j = i + 1
    while True :
        if j == len(operation) :
            end_block_idx = j
            break
        elif operation[j] == '+' or operation[j] == '*' :
            end_block_idx = j - 1
            break
        else :
            j += 1

    # Compute the operation (sum/mult) for the block
    tmp_value = 0 if current_operation == '+' else 1
    for k in range(end_block_idx - start_block_idx) :
        idx_block = i + k

        num = int(''.join(map(str, data_txt_matrix[:, idx_block])))
        print('\t', idx_block, num)

        if current_operation == '+' :
            tmp_value += int(num)
        elif current_operation == '*' :
            tmp_value *= int(num)
        else :
            raise ValueError('Error with current operation')

    # Add the result to final sums
    print(tmp_value, current_operation, start_block_idx, end_block_idx, "\n")
    if current_operation == '+' : plus_sum += tmp_value
    if current_operation == '*' : mult_sum += tmp_value
    
    # Increase idx (move to the start of the next block)
    i = j
    # print(i)


# Get the final result and print it
final_result = plus_sum + mult_sum
print(f'Sum of summation part      : {plus_sum}')
print(f'Sum of multiplication part : {mult_sum}')
print(f'Final result               : {final_result}')

# Copy the final result to clipboard
pyperclip.copy(final_result)
