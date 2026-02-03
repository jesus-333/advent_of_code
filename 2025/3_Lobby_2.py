"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/3

Solution part 2 : 168798209663590

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

def find_next_digit(row : list, start_digit : int) :
    digit = -1
    rest_of_the_row = []

    for i in range(start_digit, -1, -1) :
        possible_idx_current_digit = np.argwhere(row == str(i))

        # Check if the digit is inside the row
        if len(possible_idx_current_digit) > 0 :
            # Get the index of the first occurrence of the digit
            idx_digit = int(possible_idx_current_digit[0])

            # Add the digit to the list
            digit = i
            
            # Update the string to search from the next position
            rest_of_the_row = row[(idx_digit + 1):]

            break

    return digit, rest_of_the_row

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 2 (Computation)

largest_joltage_list = []

for idx_row in range(len(data_txt)) :
    row = np.asarray(list(data_txt[idx_row].strip()))
    
    # Variable for the research
    digit_list = []
    row_backup = []
    start_digit = 9
    while len(digit_list) < 12 :

        # print("--------------")
        # print(start_digit, "x", digit_list, row)

        digit, rest_of_the_row = find_next_digit(row, start_digit)
        # print(digit, rest_of_the_row)

        if digit == -1 :
            # I didn't find the current digit in the string
            start_digit -= 1

            if start_digit < 0 :
                row = row_backup[-1][0]
                start_digit = row_backup[-1][1] - 1

                del digit_list[-1]
                del row_backup[-1]
        else :
            # I find a valid digit

            if (len(digit_list) + 1) == 12 :
                # I finish the search for digits. I currently have 11 digits + the last found ---> 12 total digit
                digit_list.append(str(digit))
                continue
            elif len(rest_of_the_row) > 0 :
                # I have found less than 12 digits but I still have digits left in the string
                digit_list.append(str(digit))
                row_backup.append([row, start_digit])

                row = rest_of_the_row
                start_digit = 9
            if len(rest_of_the_row) == 0 :
                # I have no more digit to use but I did't find the required 12 digits
                # print("FAIL")
                # print(row_backup)

                start_digit -= 1

                if start_digit < 0 :
                    row = row_backup[-1][0]
                    row_backup[-1][1] -= 1
                    start_digit = row_backup[-1][1]

                    del digit_list[-1]
                    del row_backup[-1]

    # Compute largest joltage
    print("Found digits :", digit_list, f"({idx_row + 1}/{len(data_txt)})")
    largest_joltage = int(''.join(digit_list))
    largest_joltage_list.append(largest_joltage)

# Print results and copy the final result to clipboard
print(f'Sum of largest joltages : {np.sum(largest_joltage_list)}')
pyperclip.copy(np.sum(largest_joltage_list))
