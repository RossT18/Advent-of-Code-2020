from input_reader import *

data = read_task_input(2).split("\n")

"""
# Task One:
def format_policy(policy):
    limitsRaw, ltr = policy.split(" ")
    limits = [int(l) for l in limitsRaw.split("-")]

    return limits, ltr

def is_password_valid(policy, pwd):
    limits, ltr = format_policy(policy)
    if limits[0] <= str(pwd).count(ltr) <= limits[1]:
        return True
    return False
"""

def format_policy(policy):
    indicesRaw, ltr = policy.split(" ")
    indices = [(int(i) - 1) for i in indicesRaw.split("-")]

    return indices, ltr

def is_password_valid(policy, pwd):
    count = 0
    indices, ltr = format_policy(policy)
    for i in indices:
        if pwd[i] == ltr:
            count += 1
    return count == 1

count = 0
for entry in data:
    policy, pwd = entry.split(": ")
    if is_password_valid(policy, pwd):
        count += 1

print(count, "valid passwords in the database.")