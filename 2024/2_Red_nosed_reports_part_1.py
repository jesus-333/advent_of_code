"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/2 

Solution for part 1 : 483
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("2_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Count safe sequence

string_divided_by_line = string_to_analyze.strip().split('\n')
count_safe_report = 0

for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    
    # Check if number in the report are in ascending order
    safe_report_ascending = True
    for j in range(len(report) - 1) :
        if report[j] >= report[j + 1] :
            safe_report_ascending = False
            break

        if abs(report[j] - report[j + 1]) > 3 :
            safe_report_ascending = False
            break
    
    # Check if number in the report are in descending order
    if not safe_report_ascending :
        safe_report_descending = True

        for j in range(len(report) - 1) :
            if report[j] <= report[j + 1] :
                safe_report_descending  = False
                break

            if abs(report[j] - report[j + 1]) > 3 :
                safe_report_descending  = False
                break
    else :
        safe_report_descending  = False

    if safe_report_ascending or safe_report_descending : count_safe_report += 1

    print(report, count_safe_report)
    print("Ascending  : ", safe_report_ascending)
    print("Descending : ", safe_report_descending)
    print("Safe       : ", safe_report_descending or safe_report_descending)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("The number of safe report is {}".format(count_safe_report))



