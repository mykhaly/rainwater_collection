from .utils import minimal_neighbours

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
