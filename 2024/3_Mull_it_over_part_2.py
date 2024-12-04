"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/3

Solution for part 2
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Read data
f = open("3_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

# string_to_analyze = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def get_number_from_str(string : str) :
    """
    Analyze the string string and return the first number it found and the index of when it ends
    """

    n = 0

    for idx in range(len(string)) :
        char = string[idx]
        if char.isnumeric() :
            n = n * 10 + int(char)
        else :
            break

    return n, idx


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

total_sum = 0
list_of_mult_found = []
mul_idx_start_list = []

enable_mul = True

for idx in range(len(string_to_analyze)) :
    # Check for do/don't instruction

    # Search for do word 
    do_word_found = False
    if string_to_analyze[idx] == 'd' :
        if string_to_analyze[idx + 1] == 'o' : 
            do_word_found  = True
    
    # Check if the word is a do or don't
    do_instruction_found = False
    dont_instruction_found = False
    if do_word_found   :
        if string_to_analyze[idx + 2] == '(' and string_to_analyze[idx + 3] == ')' : 
            do_instruction_found = True
            dont_instruction_found =  False # I know that this instruction is redundant and unnecessary
        elif string_to_analyze[idx + 2] == 'n' and string_to_analyze[idx + 3] == '\'' and string_to_analyze[idx + 4] == 't' and string_to_analyze[idx + 5] == '(' and string_to_analyze[idx + 6] == ')' :
            do_instruction_found = False # I know that this instruction is redundant and unnecessary
            dont_instruction_found = True

    if do_instruction_found :
        enable_mul = True
    elif dont_instruction_found :
        enable_mul = False
    
    # Check for mul instruction
    if enable_mul :
        # Search for mul world
        mul_found = False
        if string_to_analyze[idx] == 'm' and string_to_analyze[idx + 1] == 'u' and string_to_analyze[idx + 2] == 'l' : mul_found = True
        
        # Check if there is the open round bracket
        round_bracket_open_found = False
        if mul_found and string_to_analyze[idx + 3] == '(' : 
            round_bracket_open_found = True
        else : continue
        
        # Check if there is the first number
        first_number_found = False
        if round_bracket_open_found and string_to_analyze[idx + 4].isdigit() :
            first_number_found = True
            number_1, idx_end_number_1 = get_number_from_str(string_to_analyze[(idx + 4):])
        else : continue
        
        # Check if there is the comman between the two numbers
        comma_found = False
        if first_number_found and string_to_analyze[idx + 4 + idx_end_number_1] == ',' :
            comma_found = True
        else : continue

        # Check if there is the second number
        second_number_found = False
        if comma_found and string_to_analyze[idx + 4 + idx_end_number_1 + 1].isdigit() :
            second_number_found = True
            number_2, idx_end_number_2 = get_number_from_str(string_to_analyze[(idx + 4 + idx_end_number_1 + 1):])
        else : continue
        
        # Check for closing round bracket
        round_bracket_closed_found = False
        if second_number_found and string_to_analyze[idx + 4 + idx_end_number_1 + 1 + idx_end_number_2] == ')' :
            total_sum += (number_1 * number_2)
            list_of_mult_found.append([number_1, number_2])
            mul_idx_start_list.append(idx)
        else :
            continue


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("Total sum = {}".format(total_sum))


