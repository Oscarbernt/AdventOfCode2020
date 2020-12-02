import numpy as np
     
def find_valid_passwords(file_path):
    with open(file_path, "r") as file:
        valid_passwords = 0   
        array_of_lines = file.read().splitlines()
        
        for i in array_of_lines:
            input_values = i.split(" ")
            policy_min_and_max = list(map(int, input_values[0].split("-")))
            policy_letter = input_values[1].strip(":")
            password = input_values[2]
            
            count = 0
            for i in password:
                if i == policy_letter:
                    count = count + 1

            if policy_min_and_max[0] <= count <= policy_min_and_max[1]:
                valid_passwords = valid_passwords + 1
        
        print("Valid passwords:", valid_passwords)


if __name__ == "__main__":
    find_valid_passwords("passworddb.txt")
    