from input_reader import *

data = read_task_input(3).split("\n")

STEPS = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

tree_counts = []

for step in STEPS:
    tree_count = 0
    
    at_end = False
    x, y = 0, 0

    while not at_end:
        current = data[y][x]

        if current == "#":
            tree_count += 1

        x += step[0]
        y += step[1]

        x = x % len(data[0])

        at_end = y > (len(data) - 1)

    tree_counts.append(tree_count)

result = 1
for t in tree_counts:
    result *= t
print(result)
