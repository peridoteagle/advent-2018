import itertools

# Puzzle 1

data = []
result = 0
with open('input_correct.txt') as f:
    for lines in f:
        result = result + int(lines)
        data.append(int(lines))

print(result)


# Puzzle 2
g = itertools.cycle(data)
result_list = [0]
result = next(g)
print(result)
while result not in result_list:
    result_list.append(result)
    result = result + next(g)
    print(result)
