import numpy as np

# Puzzle 1

'''
Approach: split string into relevant parts
Add 1 to 0 matrix every time that block is used in a sample
'''

map = np.zeros((1000, 1000))

with open('data/dec_3_input.txt') as f:
    for lines in f:
        print(lines)
        id, remainder1 = lines.split(' @ ', 2)
        column, remainder2 = remainder1.split(',')
        row, remainder3 = remainder2.split(': ')
        width, length = remainder3.split('x')
        print(id)
        print(column)
        print(row)
        print(width)
        print(length)
        for i in range(int(width)):
            for j in range(int(length)):
                map[int(row) + j, int(column) + i] += 1

print(map)

unique, counts = np.unique(map, return_counts=True)
n_counts = dict(zip(unique, counts))
print(n_counts)
print((1000*1000) - n_counts[0.0] - n_counts[1.0])


# Puzzle 2

'''
Approach: use the same map object from above
Repeat the whole process
Any observation that occurs by itself will only change by 1
and all the numbers will be the same (2)
'''

with open('data/dec_3_input.txt') as f:
    for lines in f:
        print(lines)
        id, remainder1 = lines.split(' @ ', 2)
        column, remainder2 = remainder1.split(',')
        row, remainder3 = remainder2.split(': ')
        width, length = remainder3.split('x')

        count_add = []
        for i in range(int(width)):
            for j in range(int(length)):
                map[int(row) + j, int(column) + i] += 1
                count_add.append(map[int(row) + j, int(column) + i])

        print(id)
        print(set(count_add))
        if set(count_add) == {2.0}:
            break
