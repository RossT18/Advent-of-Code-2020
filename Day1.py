from input_reader import *
data = read_task_input(1)

typedData = [int(i) for i in data.split("\n")]

for p1 in typedData:
    for p2 in typedData:
            if p1 + p2 == 2020:
                print(p1*p2)

for p1 in typedData:
    for p2 in typedData:
        for p3 in typedData:
            if p1 + p2 + p3 == 2020:
                print(p1*p2*p3)