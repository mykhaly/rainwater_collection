class C:
    def __init__(self, terrain_height=0, water_height=0):
        self.t = terrain_height
        self.w = water_height

    def height(self):
        return self.t + self.w

    def __str__(self):
        return "({}, {})".format(self.t, self.w)

    __repr__ = __str__


array = []
for i in range(5):
    array.append([])
    for j in range(5):
        array[i].append(C(i + 1, 0))


for i in range(5):
    for l in range(5):
        print array[i][l], "\t",
    print "\n"

def min_neigh(row, col, arr):
    last = len(arr) - 1
    result = []
    if row != last and row != 0:
        if col != last and col != 0:
            result.append((row - 1, col))
            result.append((row - 1, col + 1))
            result.append((row, col + 1))
            result.append((row + 1, col + 1))
            result.append((row + 1, col))
            result.append((row + 1, col - 1))
            result.append((row, col - 1))
            result.append((row - 1, col - 1))
        elif col == last:
            result.append((row - 1, col))
            result.append((row + 1, col))
            result.append((row + 1, col - 1))
            result.append((row, col - 1))
            result.append((row - 1, col - 1))
        elif col == 0:
            result.append((row - 1, col))
            result.append((row - 1, col + 1))
            result.append((row, col + 1))
            result.append((row + 1, col + 1))
            result.append((row + 1, col))
    elif row == last:
        if col != last and col != 0:

    elif row == 0:
        if col != last and col != 0:
            result.append((row, col + 1))
            result.append((row + 1, col + 1))
            result.append((row + 1, col))
            result.append((row + 1, col - 1))
            result.append((row, col - 1))
        elif col == last:
            result.append((row + 1, col))
            result.append((row + 1, col - 1))
            result.append((row, col - 1))
        elif col == 0:
            result.append((row, col + 1))
            result.append((row + 1, col + 1))
            result.append((row + 1, col))

def mooo(row, col, arr):
    last = len(arr)
    result_ind = []
    result_ind.append((row - 1, col)) if row != 0
    result_ind.append((row - 1, col + 1)) if row != 0 and col != last
    result_ind.append((row, col + 1)) if col != last
    result_ind.append((row + 1, col + 1)) if row != last and col != last
    result_ind.append((row + 1, col)) if row != last
    result_ind.append((row + 1, col - 1)) if row != last and col != 0
    result_ind.append((row, col - 1)) if col != 0
    result_ind.append((row - 1, col - 1)) if row != 0 and col != 0
    print result
