def minimal_neighbours(row, col, arr):
    indices = neighbours(row, col, arr)
    values = []
    for element in indices:
        values.append(arr[element[0]][element[1]].height)
    min_val = min(values)
    min_val = min(min_val, arr[row][col].height)
    #print "values  ", values
    #print "min value  ", min_val
    result = []
    for index, element in enumerate(values):
        if element == min_val:
            result.append(indices[index])
    return result

def neighbours(row, col, arr):
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
    #print indices
    return indices

def minimum_diff(curr_row, curr_col, min_row, min_col, arr):
    foo = minimal_neighbours(curr_row, curr_col, arr)
    bar = minimal_neighbours(min_row, min_col, arr)
    print foo
    print bar
    quax = set.intersection(foo, bar)
    print quax



























#def blabla(arr):
#    size = len(arr)
#    water_moved = False
#    for i in range(size):
#        for j in range(size):
#            water_moved = move_water(i, j, arr)
#    if water_moved:
#        return blabla(arr)
#    return arr
#
#def move_water(row, col, arr):
#    this_column_water_amount = arr[row][col].water
#    this_column_height = arr[row][col].height
#    min_neigh = minimal_neighbours(row, col, arr)
#    how_many_water_could_be_moved_into_neighbour = []
#    for neighbour in min_neigh:
#        water_could_be_moved_into_current_neighbour = minimal_higher_neighbour(neighbour[0], neighbour[1], arr)
#    i need to find cells to move water into k
#
#def water_could_be_moved_into(row, col, arr):
#    result = 0
#    if minimal_higher_neighbour.height == arr[row][col].height:
#        
