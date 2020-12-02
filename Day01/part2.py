import numpy as np
from fileReader import read_file


def find_2020(file_path):
    sum_to_find = 2020
    expenses = read_file(file_path)

    result = find_values(2020, expenses)
    
    if len(result) != 0:
        product = np.prod(result)
        print("Values added resulting in sum", sum_to_find, ":", result[0:len(result)])
        print("Product:", product)
        return product

#Returns tuple of 3 values added together resulting in value provided for "goal"
def find_values(goal, report_values):
    for i in range(0, len(report_values) -1):
        value_set = []
        current_sum = goal - report_values[i]
        for j in range(i + 1, len(report_values)):
            if current_sum - report_values[j] in value_set:
                return (report_values[i], report_values[j], current_sum - report_values[j])
            value_set.insert(j, report_values[j])

    return ()

if __name__ == "__main__":
    find_2020("expenses.txt")