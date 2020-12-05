
def parse_file(file_path):
    file = open(file_path, "r")
    split_lines = file.read().split("\n\n")
    passport_list = []
    for i in split_lines:
        i = i.replace("\n", " ")
        props = i.split(" ")
        passport = dict()        
        for prop in props:
            key_value = prop.split(":")
            passport[key_value[0]] = key_value[1]
        passport_list.append(passport)

    return passport_list
def find_valid_passports(passports):
    valid_mask = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    number_of_invalid_passports = 0
    for passport in passports:
        for i in valid_mask:
            if i not in passport:
                number_of_invalid_passports += 1
                break

    print(len(passports) - number_of_invalid_passports)
        

if __name__ == "__main__":
    passports = parse_file("passport_batch.txt")
    find_valid_passports(passports)