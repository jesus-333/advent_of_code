"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/5

Solution for part 1 : 5713
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("5_data_1.txt", "r")
page_ordering_rules_string = f.read()
f.close()

f = open("5_data_2.txt", "r")
update_string = f.read()
f.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Data preprocess

# Convert page order in array
page_ordering_divided_by_line = page_ordering_rules_string.strip().split("\n")
page_ordering_1 = np.zeros(len(page_ordering_divided_by_line))
page_ordering_2 = np.zeros(len(page_ordering_divided_by_line))

for i in range(len(page_ordering_divided_by_line)) :
    tmp_values = page_ordering_divided_by_line[i].split("|")
    page_ordering_1[i] = int(tmp_values[0])
    page_ordering_2[i] = int(tmp_values[1])

# Update print information
update_string_divided_by_line = update_string.strip().split("\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Search for correct rules

correct_sequence_list = []
for i in range(len(update_string_divided_by_line)) :
    current_update = update_string_divided_by_line[i].strip().split(',')
    current_update = np.array(current_update, dtype = int)
    
    correct_sequence = True
    for j in range(len(current_update)) :
        # Get the current element
        current_element = current_update[j]

        # Find all the elements required for the current element
        idx_in_array_2 = page_ordering_2 == current_element
        element_before_current_element = page_ordering_1[idx_in_array_2]

        # Filter the elements required. Keep only the ones in the current sequence
        idx_to_keep = []
        for tmp_element in element_before_current_element :
            if tmp_element in current_update :
                idx_to_keep.append(True)
            else :
                idx_to_keep.append(False)
        element_before_current_element = element_before_current_element[idx_to_keep]

        # Get the sequence up to the current element and after the element
        sequence_before_current_element = current_update[0:j]
        sequence_after_current_element  = current_update[(j + 1):]
        
        for tmp_element in element_before_current_element :
            if tmp_element in sequence_after_current_element :
                correct_sequence = False
                break

    if correct_sequence : correct_sequence_list.append(i)
print(len(correct_sequence_list))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Compute the middle element and their sum
sum_middle_element = 0

for i in range(len(update_string_divided_by_line)) :
    if i in correct_sequence_list :
        current_update = update_string_divided_by_line[i].strip().split(',')
        current_update = np.array(current_update, dtype = int)
        middle_element = current_update[int(len(current_update) / 2)]
        sum_middle_element += middle_element

print("The sum of middle element of correct sequence is : ", sum_middle_element)

