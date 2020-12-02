import numpy as np
import time
from fileReader import read_file
     
#Returns tuple of 2 values added together resulting in value provided for "goal"
def find_values(goal, list_of_values):
    for i in range(0, len(list_of_values) - 1):
        value_to_find = goal - list_of_values[i]
        for j in range(i + 1, len(list_of_values) - 1):
            if list_of_values[j] == value_to_find:
                return (list_of_values[i],list_of_values[j])
    return ()

def find_2020(file_path):
    sum_to_find = 2020
    expenses = read_file(file_path)
    result = find_values(sum_to_find, expenses)

    if len(result) != 0:
        product = np.prod(result)
        print("Values added resulting in sum", sum_to_find, ":", result[0:len(result)])
        print("Product:", product)
        return product
    
if __name__ == "__main__":
    find_2020("C:\\Users\\oscar\\Documents\\Repo\\AdventOfCode2020\\Day01\\exampleInput.txt")