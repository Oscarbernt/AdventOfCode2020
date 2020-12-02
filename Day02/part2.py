import numpy as np
     
def find_valid_passwords(file_path):
    with open(file_path, "r") as file:
        array_of_lines = file.read().splitlines()
        valid_passwords = 0      
        for i in array_of_lines:
            input_values = i.split(" ")
            policy_positions = list(map(int, input_values[0].split("-")))
            policy_letter = input_values[1].strip(":")
            password = input_values[2]
            
            count = 0
            for i in policy_positions:
                if len(password) > (i - 1) and password[i - 1] == policy_letter:
                    count = count + 1
            
            if count == 1:
                valid_passwords = valid_passwords + 1
        
        print("Valid passwords:", valid_passwords)


if __name__ == "__main__":
    find_valid_passwords("passworddb.txt")