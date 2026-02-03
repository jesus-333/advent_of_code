"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2025/day/11

"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Imports

from functools import cache

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Preprocess)

# Read txt files
with open('./11_data.txt') as f :
    data_txt = f.read().strip().split('\n')


dict_link = dict()

for i in range(len(data_txt)) :
    current_line = data_txt[i]

    source = current_line.split(":")[0].strip()
    destination = current_line.split(":")[1].strip().split(' ')

    dict_link[source] = destination

start = data_txt[0].split(":")[0]
next_destination = data_txt[0].split(":")[1].strip().split(' ')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 1 (Computation)

@cache
def recursive_traverse(current_node) :
    next_destination = dict_link[current_node]

    if len(next_destination) == 1 :
        if next_destination[0] == 'out' : return 1
        else : return recursive_traverse(next_destination[0])
    else :
        total_way_out_current_node = 0
        for i in range(len(next_destination)) :
            total_way_out_current_node  += recursive_traverse(next_destination[i])

        return total_way_out_current_node

total_way_out = 0
for i in range(len(next_destination)) :
    current_destination = next_destination[i]

    total_way_out += recursive_traverse(current_destination)

print(f'Total way out (1) : {total_way_out}')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Part 2 (Computation)

@cache
def recursive_traverse_2(current_node, visit_dac : bool, visit_fft : bool) :
    next_destination = dict_link[current_node]
    
    if current_node == 'dac' : visit_dac = True
    if current_node == 'fft' : visit_fft = True

    if len(next_destination) == 1 :
        if next_destination[0] == 'out' :
            if visit_dac is True and visit_fft is True : return 1
            else : return 0
        else :
            return recursive_traverse_2(next_destination[0], visit_dac, visit_fft)
    else :
        total_way_out_current_node = 0
        for i in range(len(next_destination)) :
            total_way_out_current_node  += recursive_traverse_2(next_destination[i], visit_dac, visit_fft)

        return total_way_out_current_node

start = 'svr'
next_destination = dict_link[start]

total_way_out = 0
for i in range(len(next_destination)) :
    current_destination = next_destination[i]

    total_way_out += recursive_traverse_2(current_destination, False, False)

print(f'Total way out (2) : {total_way_out}')

