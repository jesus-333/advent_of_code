"""
I make no claim to be efficient or effective. What you see is simply the first solution I came up with.

Original problem https://adventofcode.com/2024/day/2 

This solution was wrong so I applied a more brute force approach
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Imports

import numpy as np

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Read data

f = open("2_data.txt", "r")
string_to_analyze = f.read()
# print(string_to_analyze) 

string_to_analyze = """
58 64 67 69 70 73 74
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def check_ascending(report) :
    # Check if number in the report are in ascending order
    safe_report_ascending = True
    for j in range(len(report) - 1) :
        if report[j] >= report[j + 1] or abs(report[j] - report[j + 1]) > 3:
            safe_report_ascending = False
            break
    
    # Check the possibile type of error
    if not safe_report_ascending :
        if abs(report[j] - report[j + 1]) > 3 :  # Distance between values is bigger than 3
            # Example : 26 29 31 34 36 40
            idx_error = j + 1
        elif j == len(report) - 2 : # Error is in the last values of the sequence
            idx_error = -1
        else : # Check what is the best value to remove
            current_value     = report[j]
            possible_error    = report[j + 1]
            value_after_error = report[j + 2]

            if current_value > value_after_error : 
                # Example. The error is that 77 is smaller than 79. But if I remove 79 the rest of the sequence is ok
                # current_value = 79, possible_error = 77, value_after_error = 78
                # 70 73 76 79 77 78 
                idx_error = j
            else :
                # Example. The error is that 77 is smaller than 79. But if I remove 77 the rest of the sequence is ok
                # current_value = 79, possible_error = 77, value_after_error = 81
                # 70 73 76 79 77 81
                idx_error = j + 1
    else :
        idx_error = None
    
    return safe_report_ascending, idx_error

def check_descending(report) :
    safe_report_descending = True
    for j in range(len(report) - 1) :
        if report[j] <= report[j + 1] or abs(report[j] - report[j + 1]) > 3 :
            safe_report_descending  = False
            break

    # Check the possibile type of error
    if not safe_report_descending :
        if abs(report[j] - report[j + 1]) > 3 :  # Distance between values is bigger than 3
            # Example : 40 36 34 31 29 26
            idx_error = j + 1
        elif j == len(report) - 2 : # Error is in the last values of the sequence
            idx_error = -1
        else : # Check what is the best value to remove
            current_value     = report[j]
            possible_error    = report[j + 1]
            value_after_error = report[j + 2]

            if current_value > value_after_error : 
                # Example. The error is that 77 is smaller than 79. But if I remove 79 the rest of the sequence is ok
                # current_value = 79, possible_error = 77, value_after_error = 78
                # 78 77 79 76 73 70
                idx_error = j + 1
            else :
                # Example. The error is that 77 is smaller than 79. But if I remove 77 the rest of the sequence is ok
                # current_value = 79, possible_error = 77, value_after_error = 81
                # 81 77 79 76 73 70
                idx_error = j 
    else :
        idx_error = None
    
    return safe_report_descending, idx_error

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Remove reports impossibile to correct

string_divided_by_line = string_to_analyze.strip().split('\n')
count_safe_report = 0

fail_sequence = []
sequence_to_skip = []

print("Total element = ", len(string_divided_by_line))

# Remove reports with more than 1 duplicate element
for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    unique_values, count_values = np.unique(report, return_counts = True)
    if abs(np.sum(count_values) - len(unique_values)) > 1 : sequence_to_skip.append(i)
print("Element after filter 1 = ", len(string_divided_by_line) - len(sequence_to_skip))

# Remove reports with more than 1 gap bigger than 4
for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    diff_values = np.abs(np.diff(report))
    if np.sum(diff_values >= 4) > 1 : sequence_to_skip.append(i)
sequence_to_skip = list(np.unique(sequence_to_skip))
print("Element after filter 2 = ", len(string_divided_by_line) - len(sequence_to_skip))

# Remove reports with at least 1 gap bigger than 4 and a duplicate
for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    diff_values = np.abs(np.diff(report))
    if np.sum(diff_values >= 4) >= 1 and 0 in diff_values : sequence_to_skip.append(i)
sequence_to_skip = list(np.unique(sequence_to_skip))
print("Element after filter 3 = ", len(string_divided_by_line) - len(sequence_to_skip))

# Remove reports with at multiple number in ascending and descending order
for i in range(len(string_divided_by_line)) :
    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    diff_values = np.diff(report)
    if np.sum(diff_values > 0) >= 1 and np.sum(diff_values < 0) : sequence_to_skip.append(i)
sequence_to_skip = list(np.unique(sequence_to_skip))
print("Element after filter 4 = ", len(string_divided_by_line) - len(sequence_to_skip))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Counts correct report in the remaining report

# Count the safe sequence on the remaining reports
for i in range(len(string_divided_by_line)) :
    if i in sequence_to_skip : continue

    report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
    
    # Check if the current report is safe (ASCENDING)
    safe_report_ascending, idx_error = check_ascending(report)

    # If it is not remove the value that cause the error and check again
    if not safe_report_ascending :
        print("ASCENDING ERROR")
        print(report, idx_error)
        report = np.delete(report, idx_error)
        print(report, idx_error, "\n")

        safe_report_ascending, _ = check_ascending(report)

    # Check if number in the report are in descending order
    if not safe_report_ascending :
        report = np.asarray(string_divided_by_line[i].split(' '),  dtype = int)
        safe_report_descending = True

        # Check if the current report is safe (DESCENDING)
        safe_report_descending, idx_error = check_descending(report)

        # If it is not remove the value that cause the error and check again
        if not safe_report_descending :
            # print("DESCENDING ERROR")
            # print(report, idx_error)
            report = np.delete(report, idx_error)
            # print(report, idx_error, "\n")

            safe_report_descending , _ = check_descending(report)

    else :
        safe_report_descending  = False

    if safe_report_ascending or safe_report_descending : 
        count_safe_report += 1
    else :
        fail_sequence.append(np.asarray(string_divided_by_line[i].split(' '),  dtype = int))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

print("The number of safe report is {}".format(count_safe_report))



