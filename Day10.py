from input_reader import *

adapters_raw = read_task_input(10).split("\n")

adapters = sorted([int(a) for a in adapters_raw])

# Start with one 1diff and one 3diff for 0 jolt out and built-in adapter diffs
diff_counts = [1, 1]

for a in range(0, len(adapters) - 1):
    this_a = adapters[a]
    next_a = adapters[a + 1]

    if (next_a - this_a == 1):
        diff_counts[0] += 1
    elif (next_a - this_a == 3):
        diff_counts[1] += 1

print("When using all adapters...")
print("1-jolt Differences:", diff_counts[0], " 3-jolt Differences:", diff_counts[1])
print("Answer:", diff_counts[0] * diff_counts[1])
print("============================================")


# Tree with 0 as root node and 22 as the final leaf down each path

def valid_traverse(current, next):
    if (next - current < 4 and next - current > 0):
        return True
    else:
        return False

# Dictionary of values to counts.
# Keys are adapters and counts are the number of possible paths to the end
seen = {}

def traverse(start, d):
    global seen

    #At the end of the path, return 1
    if start == list(d)[-1]:
        return 1

    count = 0
    for v in d[start]:
        # If already seen the start of this path, just add path count so we don't have to traverse it again
        if v in seen:
            count += seen[v]
        else:
            paths = traverse(v, d)
            seen[v] = paths # Remember how many paths were after this v
            count += paths
    return count


def count_arrangements(adapters):
    # Add 0 jolt output and built-in adapter to list
    adapters = [0] + adapters
    adapters.append(adapters[-1] + 3)

    things = {}
    for a in range(0, len(adapters)):
        for b in range(a + 1, len(adapters)):
            this_a = adapters[a]
            next_a = adapters[b]
            if valid_traverse(this_a, next_a):
                if (this_a in things):
                    things[this_a].append(next_a)
                else:
                    things[this_a] = [next_a]

    arrangement_count = 0
    for v in things[0]:
        arrangement_count += traverse(v, things)
    return arrangement_count

print("Number of Arrangements:", count_arrangements(adapters))