"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/1 

Solution for part 2 : 23126924
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Read data
f = open("1_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Convert string to array

string_divided_by_line = string_to_analyze.strip().split('\n')

array_1 = np.zeros(len(string_divided_by_line))
array_2 = np.zeros(len(string_divided_by_line))

for i in range(len(string_divided_by_line)) :
    numbers_in_line = string_divided_by_line[i].split('   ')
    array_1[i] = int(numbers_in_line[0])
    array_2[i] = int(numbers_in_line[1])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute similarity score

similarity_score = 0

for i in range(len(array_1)) :
    element_array_1 = array_1[i]

    count_element_in_array_2 = np.sum(array_2 == element_array_1) * element_array_1
    similarity_score += count_element_in_array_2

print("The similarity score is ", similarity_score)
