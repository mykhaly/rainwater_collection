#def min_neigh(row, col, arr):
#    last = len(arr) - 1
#    result = []
#    if row != last and row != 0:
#        if col != last and col != 0:
#            result.append((row - 1, col))
#            result.append((row - 1, col + 1))
#            result.append((row, col + 1))
#            result.append((row + 1, col + 1))
#            result.append((row + 1, col))
#            result.append((row + 1, col - 1))
#            result.append((row, col - 1))
#            result.append((row - 1, col - 1))
#        elif col == last:
#            result.append((row - 1, col))
#            result.append((row + 1, col))
#            result.append((row + 1, col - 1))
#            result.append((row, col - 1))
#            result.append((row - 1, col - 1))
#        elif col == 0:
#            result.append((row - 1, col))
#            result.append((row - 1, col + 1))
#            result.append((row, col + 1))
#            result.append((row + 1, col + 1))
#            result.append((row + 1, col))
#    elif row == last:
#        if col != last and col != 0:
#
#    elif row == 0:
#        if col != last and col != 0:
#            result.append((row, col + 1))
#            result.append((row + 1, col + 1))
#            result.append((row + 1, col))
#            result.append((row + 1, col - 1))
#            result.append((row, col - 1))
#        elif col == last:
#            result.append((row + 1, col))
#            result.append((row + 1, col - 1))
#            result.append((row, col - 1))
#        elif col == 0:
#            result.append((row, col + 1))
#            result.append((row + 1, col + 1))
#            result.append((row + 1, col))
#
def mooo(row, col, arr):
    last = len(arr) - 1
    result_ind = []
    if row != 0:
        result_ind.append((row - 1, col))
    if row != 0 and col != last:
        result_ind.append((row - 1, col + 1))
    if col != last:
        result_ind.append((row, col + 1))
    if row != last and col != last:
        result_ind.append((row + 1, col + 1))
    if row != last:
        result_ind.append((row + 1, col))
    if row != last and col != 0:
        result_ind.append((row + 1, col - 1))
    if col != 0:
        result_ind.append((row, col - 1))
    if row != 0 and col != 0:
        result_ind.append((row - 1, col - 1))

    result_val = []
    for element in result_ind:
        result_val.append(arr[element[0]][element[1]])
    minimum = min(result_val)
    minimum = min(minimum, arr[row][col])
    result_result = []
    for index, element in enumerate(result_val):
        if element == minimum:
            result_result.append(result_ind[index])
    return result_result

foo = [[x for x in range (3)] for y in range(3)]
for i in range(3):
    print foo[i]

for i in range(3):
    for j in range(3):
        print i, j, "\t", mooo(i, j, foo)
    print "\n"
