"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/7

Solution part 1 : 6392012777720
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("7_data.txt", "r")
string_to_analyze = f.read()
string_divided_by_line = string_to_analyze.strip().split('\n')

list_test_results = []
list_of_equations_input = []

for line in string_divided_by_line :
    tmp_values = line.split(' ')
    list_test_results.append(int(tmp_values[0].split(':')[0]))

    list_of_equations_input.append([int(tmp_values[i]) for i in range(1, len(tmp_values))])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def binary_increase(binary_array) :
    """
    Given an array of 1s and 0s consider it as a binary number and increase it by 1
    I know that probably with some bit operation it will be faster
    """

    for idx in range(len(binary_array)) :
        binary_array[idx] += 1
        if binary_array[idx] == 2 : 
            binary_array[idx] = 0
        else :
            return binary_array


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Test which equations are true

results_of_correct_equation = []
for i in range(len(list_test_results)) :
    test_result = list_test_results[i]
    equation_input = list_of_equations_input[i]

    # Iterate over all possible operation
    result_found = False
    possible_operation = np.zeros(len(equation_input) - 1)
    for j in range(2 ** (len(equation_input) - 1)) :
        tmp_result = 0

        # Compute the result according to current operation order
        for k in range(len(possible_operation)) :
            if k == 0 :
                if possible_operation[k] == 0 :
                    tmp_result = equation_input[k] + equation_input[k + 1]
                else :
                    tmp_result = equation_input[k] * equation_input[k + 1]
            else :
                if possible_operation[k] == 0 :
                    tmp_result = tmp_result + equation_input[k + 1]
                else :
                    tmp_result = tmp_result * equation_input[k + 1]
            # print("\t", tmp_result, "{}, {}".format(equation_input[k], equation_input[k + 1]))
        
        # Check if the results is valid
        # print(possible_operation, tmp_result, test_result, "\n")
        if tmp_result == test_result :
            result_found = True
            break
        else :
            possible_operation = binary_increase(possible_operation)

    if result_found : results_of_correct_equation.append(test_result)

print("Solution part 1 : ", np.sum(results_of_correct_equation))
