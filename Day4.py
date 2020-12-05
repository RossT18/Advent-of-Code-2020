from input_reader import *

passportsRaw = read_task_input(4).split("\n\n")

def correct_year(lower, upper, value):
    return lower <= int(value) <= upper

def validate_birth(year):
    return correct_year(1920, 2002, year)

def validate_issue(year):
    return correct_year(2010, 2020, year)

def validate_expiration(year):
    return correct_year(2010, 2030, year)

def validate_height(height):
    str_height_val = str(height)[:-2]
    if str_height_val == '':
        return False
    value = int(str_height_val)
    if str(height).endswith("cm"):
        return 150 <= value <= 193
    elif str(height).endswith("in"):
        return 59 <= value <= 76
    else:
        return False

def validate_hair(colour):
    digits = colour[1:]

    hash = colour[0] == '#'
    dig_len = len(str(digits)) == 6
    valid_digits = True
    for dig in digits:
        if (not str(dig).isnumeric()) and ((not str(dig).isalpha()) or str(dig) > 'f'):
            valid_digits = False
            break;
    return hash and dig_len and valid_digits

def validate_eye(colour):
    COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return colour in COLOURS

def validate_pp_id(id):
    return len(id) == 9 and str(id).isnumeric()


FIELDS_WITH_VALIDATION = [  ["byr", validate_birth],
                            ["ecl", validate_eye],
                            ["eyr", validate_expiration],
                            ["hcl", validate_hair],
                            ["hgt", validate_height],
                            ["iyr", validate_issue],
                            ["pid", validate_pp_id]]

ALL_FIELDS = ["byr", "cid", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]
REQUIRED_FIELDS = ["byr", "ecl", "eyr", "hcl", "hgt", "iyr", "pid"]

def validate_field(field_name, field_value):
    for field_set in FIELDS_WITH_VALIDATION:
        if field_set[0] == field_name:
            if not field_set[1](field_value):
                return False
    return True


def isValid(passport):
    these_fields = []
    for field in passport:
        f, v = field.split(":")
        if validate_field(f, v):
            # If the field value was valid, add it to the list
            these_fields.append(field.split(":")[0])

    these_fields.sort()
    # these_fields will only contain field names with valid data
    return these_fields == ALL_FIELDS or these_fields == REQUIRED_FIELDS

passport_data = []

for passport in passportsRaw:
    pp_data = []
    for some_field_data in passport.split("\n"):
        for field_data in some_field_data.split(" "):
            pp_data.append(field_data)

    passport_data.append(pp_data)

validCount = 0
for passport in passport_data:
    if isValid(passport):
        validCount += 1

print(str(validCount) + " valid passports")