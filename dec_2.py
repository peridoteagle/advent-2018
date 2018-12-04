from collections import Counter
import itertools

# Puzzle 1

two_count = 0
three_count = 0

with open('dec_2_input.txt') as f:
    for lines in f:

        count_list = []
        counts = Counter(lines)

        for k, v in counts.items():
            count_list.append(v)

        if 2 in set(count_list) and 3 not in set(count_list):
            two_count = two_count + 1

        if 3 in set(count_list) and 2 not in set(count_list):
            three_count = three_count + 1

        if 2 and 3 in set(count_list):
            two_count = two_count + 1
            three_count = three_count + 1

print(two_count * three_count)

# Puzzle 2
line_list = []
with open('dec_2_input.txt') as f:
    for lines in f:
        line_list.append(lines)

for a, b in itertools.combinations(line_list, 2):
    diff = [i for i in range(len(a)) if a[i] != b[i]]
    if len(diff) == 1:
        print(a)
        print(b)
