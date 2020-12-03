def read_task_input(day_num):
    content = ""
    with open("day" + str(day_num) + "_data.txt", 'r') as f:
        content = f.read()

    return content