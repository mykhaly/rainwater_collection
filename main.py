from utils import minimal_neighbours, neighbours

class C:
    def __init__(self, terrain_height=0, water_height=0):
        self.t = terrain_height
        self.w = water_height

    @property
    def height(self):
        return self.t + self.w

    def __str__(self):
        return "({}, {})".format(self.t, self.w)

    __repr__ = __str__


foo = \
[
    [C(1, 1.2), C(-2, 1), C(2, 1)],
    [C(-2, 1), C(1, 1), C(2, 1)],
    [C(1, 1), C(1, 1), C(2, 1)]
]

for i in range(3):
    print foo[i]

for i in range(3):
    for j in range(3):
        print foo[i][j].height,
    print "\n"

current_neighbours = neighbours(0, 0, foo)
curr_min_neighb = minimal_neighbours(0, 0, foo)
curr_min_neighb_diffs = []
print "NEIGHBours  ", current_neighbours
print "MIN NEIGHB  ", curr_min_neighb

for min_neighb in curr_min_neighb:
    min_neighb_neighb = neighbours(min_neighb[0], min_neighb[1], foo)
    shared_neighb = list(set.intersection(set(current_neighbours), set(min_neighb_neighb)))
    minimal_diff = float("inf")

    for shrd_nghbr in shared_neighb:
        if foo[shrd_nghbr[0]][shrd_nghbr[1]].height - foo[min_neighb[0]][min_neighb[1]].height < minimal_diff and foo[shrd_nghbr[0]][shrd_nghbr[1]].height - foo[min_neighb[0]][min_neighb[1]].height != 0:
            minimal_diff = foo[shrd_nghbr[0]][shrd_nghbr[1]].height - foo[min_neighb[0]][min_neighb[1]].height
    curr_min_neighb_diffs.append(minimal_diff)
print "curr_min_neighb_diffs  ", curr_min_neighb_diffs
diff_sum = sum(curr_min_neighb_diffs)
the_most_min_diff = min(curr_min_neighb_diffs)
if the_most_min_diff * len(curr_min_neighb) > foo[0][0].w:
    amount_of_water = foo[0][0].w / len(curr_min_neighb)
    for min_neighb in curr_min_neighb:
        foo[min_neighb[0]][min_neighb[1]].w += amount_of_water
        foo[0][0].w -= amount_of_water

for i in range(3):
    print foo[i]

for i in range(3):
    for j in range(3):
        print foo[i][j].height,
    print "\n"

