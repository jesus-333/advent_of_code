"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/7

Solution part 2 : 61561126043536
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

def ternary_increase(ternary_array) :
    """
    Given an array of 2s, 1s and 0s consider it as a ternary number number and increase it by 1
    """

    for idx in range(len(ternary_array)) :
        ternary_array[idx] += 1
        if ternary_array[idx] == 3 : 
            ternary_array[idx] = 0
        else :
            return ternary_array


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Test which equations are true

results_of_correct_equation = []
for i in range(len(list_test_results)) :
    print("{}%".format(np.round((i + 1) / len(list_test_results) * 100, 2)))
    test_result = list_test_results[i]
    equation_input = list_of_equations_input[i]

    # Iterate over all possible operation
    result_found = False
    possible_operation = np.zeros(len(equation_input) - 1)
    for j in range(3 ** (len(equation_input) - 1)) :
        tmp_result = 0

        # Compute the result according to current operation order
        # print(possible_operation)
        for k in range(len(possible_operation)) :
            if k == 0 :
                if possible_operation[k] == 0 :
                    tmp_result = equation_input[k] + equation_input[k + 1]
                elif possible_operation[k] == 1 :
                    tmp_result = equation_input[k] * equation_input[k + 1]
                else :
                    tmp_result = int(str(equation_input[k]) + str(equation_input[k + 1]))
            else :
                if possible_operation[k] == 0 :
                    tmp_result = tmp_result + equation_input[k + 1]
                elif possible_operation[k] == 1 :
                    tmp_result = tmp_result * equation_input[k + 1]
                else :
                    tmp_result = int(str(tmp_result) + str(equation_input[k + 1]))
            # print("\t", tmp_result, "{}, {}".format(equation_input[k], equation_input[k + 1]))
        
        # Check if the results is valid
        # print(tmp_result, test_result, "\n")
        if tmp_result == test_result :
            result_found = True
            break
        else :
            possible_operation = ternary_increase(possible_operation)

    if result_found : results_of_correct_equation.append(test_result)

print("Solution part 2 : ", np.sum(results_of_correct_equation))
