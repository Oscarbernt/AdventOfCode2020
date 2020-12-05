
import re
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
    number_of_invalid_passports = 0
    for passport in passports:
        if not contains_valid_properties(passport):
            number_of_invalid_passports += 1
        else:
            if not validate_property_values(passport):
                number_of_invalid_passports += 1
        

    print(len(passports) - number_of_invalid_passports)
        
def validate_property_values(passports):
    cases = {
        'byr': lambda a: len(a) == 4 and int(a) >= 1920 and int(a) <= 2002,
        'iyr': lambda a: len(a) == 4 and int(a) >= 2010 and int(a) <= 2020,
        'eyr': lambda a: len(a) == 4 and int(a) >= 2020 and int(a) <= 2030,
        'hgt': lambda a: height_rule(a),
        'hcl': lambda a: re.match(r"^#+[0-9,a-f]{6}$", a),
        'ecl': lambda a: re.match(r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$", a),
        'pid': lambda a: re.match(r"^[0-9]{9}$", a),
        'cid': lambda a: True
    }
    for i in passports:
        ok = cases[i](passports[i])
        if not ok:
            return False
    
    return True

def height_rule(height):
    number = int(re.findall("\d+", height)[0])
    if re.match("\d+cm+", height):
        return number >= 150 and number <= 193
    else:
        return number >= 59 and number <= 76

def contains_valid_properties(passport):
    valid_mask = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for i in valid_mask:
        if i not in passport:
            return False
    return True

if __name__ == "__main__":
    passports = parse_file("passport_batch.txt")
    find_valid_passports(passports)