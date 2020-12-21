from input_reader import *

xmas_raw = read_task_input(9).split("\n")

def is_valid(target, previous):
    for x in previous:
        for y in previous:
            if int(x) + int(y) == target and int(x) != int(y):
                return True
    return False

def find_contiguous(target, set):
    start = -1
    end = -1
    for i in range(len(set)):
        found = False
        total = set[i]
        counter = 1
        start = i
        end = i
        while i + counter < len(set):
            total += set[i + counter]
            if (total > target):
                # to save time
                break
            if (total == target):
                end = i + counter
                found = True
            counter += 1
        if found:
            break
    return set[start:end]

PREV_COUNT = 25

i = PREV_COUNT
found_invalid = False
target = -1

while not found_invalid:
    t = int(xmas_raw[i])
    if not is_valid(t, xmas_raw[i - PREV_COUNT:i]):
        target = t
        found_invalid = True
    i += 1

print("Invalid Number:", target)

# Remove numbers higher than the target to reduce the set
new_xmas = [int(x) for x in xmas_raw if int(x) <= target]


contiguous_nums = sorted(find_contiguous(target, new_xmas))
encryption_weakness = contiguous_nums[0] + contiguous_nums[-1]

print("Encryption Weakness:", encryption_weakness)