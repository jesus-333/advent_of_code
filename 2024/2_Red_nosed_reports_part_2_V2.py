"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/2 

Solution for part 2 : 528
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("2_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

# string_to_analyze = """
# 58 64 67 69 70 73 74
# """

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def check_ascending(report : np.array) :
    # Check if number in the report are in ascending order (full list)
    safe_report_ascending = True
    for j in range(len(report) - 1) :
        if report[j] >= report[j + 1] or abs(report[j] - report[j + 1]) > 3:
            safe_report_ascending = False
            break

    return safe_report_ascending

def check_ascending_brute_force(report : np.array) :

    if check_ascending(report) : # Check if number in the report are ok (full report)
        return True 
    else : # Check if removing a number the rest of the list is ok
        safe_report_ascending_list = []

        for i in range(len(report)) :
            # Copy the report and remove the i-th element
            report_copy = report.copy()
            report_copy = np.delete(report_copy, i)
            
            # Check if the report is ok with the element removed
            safe_report_ascending_list.append(check_ascending(report_copy))

        if True in safe_report_ascending_list : return True
        else : return False

def check_descending(report : np.array) :
    # Check if number in the report are in ascending order (full list)
    safe_report_descending = True
    for j in range(len(report) - 1) :
        if report[j] <= report[j + 1] or abs(report[j] - report[j + 1]) > 3:
            safe_report_descending  = False
            break

    return safe_report_descending 

def check_descending_brute_force(report : np.array) :

    if check_descending(report) : # Check if number in the report are ok (full report)
        return True 
    else : # Check if removing a number the rest of the list is ok
        safe_report_descending_list = []

        for i in range(len(report)) :
            # Copy the report and remove the i-th element
            report_copy = report.copy()
            report_copy = np.delete(report_copy, i)
            
            # Check if the report is ok with the element removed
            safe_report_descending_list .append(check_descending(report_copy))

        if True in safe_report_descending_list  : return True
        else : return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Remove reports impossibile to correct

string_divided_by_line = string_to_analyze.strip().split('\n')
count_safe_report = 0

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Counts correct report in the remaining report

# Count the safe sequence on the remaining reports
for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    
    # Check if the current report is safe (ASCENDING)
    safe_report_ascending = check_ascending_brute_force(report)
    
    # Check if the current report is safe (DESCENDING)
    if not safe_report_ascending :
        safe_report_descending = check_descending_brute_force(report)
    else :
        safe_report_descending = False

    if safe_report_ascending or safe_report_descending : count_safe_report += 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("The number of safe report is {}".format(count_safe_report))



