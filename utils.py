def minimal_neighbours(row, col, arr):
    last = len(arr) - 1
    indices = []
    if row != 0:
        indices.append((row - 1, col))
    if row != 0 and col != last:
        indices.append((row - 1, col + 1))
    if col != last:
        indices.append((row, col + 1))
    if row != last and col != last:
        indices.append((row + 1, col + 1))
    if row != last:
        indices.append((row + 1, col))
    if row != last and col != 0:
        indices.append((row + 1, col - 1))
    if col != 0:
        indices.append((row, col - 1))
    if row != 0 and col != 0:
        indices.append((row - 1, col - 1))

    values = []
    for element in indices:
        values.append(arr[element[0]][element[1]])
    min_val = min(values, arr[row][col])
    result = []
    for index, element in enumerate(values):
        if element == min_val:
            result.append(indices[index])
    return result

foo = [[x for x in range (3)] for y in range(3)]
for i in range(3):
    print foo[i]

for i in range(3):
    for j in range(3):
        print i, j, "\t", mooo(i, j, foo)
    print "\n"
