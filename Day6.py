from input_reader import *

data = read_task_input(6).split("\n\n")

"""
# Task 1
total_sum = 0
for group in data:
    answers = "".join(group.split("\n"))
    already_seen = []
    for ltr in answers:
        if ltr not in already_seen:
            already_seen.append(ltr)
    total_sum += len(already_seen)

print(total_sum)
"""

# Task 2
def find_common(s1, s2):
    # common_ltrs should stay a string so it can be input into
    # this method again.
    common_ltrs = ""
    for l in s1:
        if l in s2:
            common_ltrs += l
    return common_ltrs

total_sum = 0
for group in data:
    person_answers = group.split("\n")
    if len(person_answers) == 1:
        # Only one person in group
        total_sum += len(person_answers[0])
    else:
        # More than one person, so find common letters
        common_letters = find_common(person_answers[0], person_answers[1])
        for i in range(2, len(person_answers), 1):
            answers = person_answers[i]
            common_letters = find_common(common_letters, answers)
        total_sum += len(common_letters)

print(total_sum)
            