import sys
import numpy as np
import re
import copy

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().split('\n\n')
instr = ll[-1]
heads = "RDLU"
arrows = ">v<^"


grid = ll[0].split('\n')


dvecs = {
    "R": np.array([0,1]),
    "L": np.array([0,-1]),
    "U": np.array([-1,0]),
    "D": np.array([1,0]),
}
dvecs = {heads.index(head): dvecs[head] for head in heads}

class Edge:
    def __init__(self, v, head, passing_head=None, dist=49):
        if type(head) == str:
            head = heads.index(head)
        self.v = np.array(v)
        self.head = head
        self.dvec = dvecs[head]
        self.dist = dist
        if type(passing_head) == str:
            passing_head = heads.index(passing_head)
        self.passing_head = passing_head
        # self.v2 = v + dist * self.dvec
        self.horz = head % 2 == 0#head in "RL"

    def intersects(self, v, head):
        if head == self.passing_head:
            d = np.dot(v - self.v, self.dvec)
            if d == np.linalg.norm(v - self.v) and 0 <= d <= self.dist:
                return d
        return False
    
    def get_at(self, dist):
        nv = self.v + dist * self.dvec
        if self.passing_head is None:
            return nv, None
        nhead = (self.passing_head + 2) % 4
        return nv, nhead

    def __str__(self):
        return "({self.v[0]},{self.v[1]}) {heads[self.head]}{self.dist}"

edge_pairs = [
    [Edge((  0,  50), "R", "U"), Edge((150,   0), "D", "L")],
    [Edge((  0,  50), "D", "L"), Edge((149,   0), "U", "L")],
    [Edge((  0, 100), "R", "U"), Edge((199,   0), "R", "D")],
    [Edge((  0, 149), "D", "R"), Edge((149,  99), "U", "R")],
    [Edge(( 49, 100), "R", "D"), Edge(( 50,  99), "D", "R")],
    [Edge(( 50,  50), "D", "L"), Edge((100,   0), "R", "U")],
    [Edge((149,  50), "R", "D"), Edge((150,  49), "D", "R")],
]

if len(sys.argv) > 1:
    edge_pairs = [
        [Edge(( 0,  8), "R", "U"), Edge(( 4,  3), "L", "U")],
        [Edge((11,  8), "R", "D"), Edge(( 7,  3), "L", "D")],
        [Edge(( 0,  8), "D", "L"), Edge(( 4,  4), "R", "U")],
        [Edge((11,  8), "U", "L"), Edge(( 7,  4), "R", "D")],
        [Edge(( 4, 11), "D", "R"), Edge(( 8, 15), "L", "U")],
        [Edge(( 0, 13), "D", "R"), Edge((11, 15), "U", "R")],
        [Edge(( 5,  0), "D", "L"), Edge((11, 15), "L", "D")],
    ]
edges = sum(edge_pairs, [])
for pair in edge_pairs:
    pair[0].pair = pair[1]
    pair[1].pair = pair[0]


def move(v, head):
    for edge in edges:
        d = edge.intersects(v, head)
        if not (d is False):
            nv, nhead = edge.pair.get_at(d)
            break
    else:
        nv, _ = Edge(v, head, dist=1).get_at(1)
        nhead = head

    if grid[nv[0]][nv[1]] == "#":
        return True, v, head
    else:
        assert grid[nv[0]][nv[1]] == "."
        return False, nv, nhead

g2 = copy.deepcopy(grid)
def display():
    print("\n\n")
    for r in g2:
        print(r)


col = re.search('[^ ]', grid[0]).start()
row = 0
head = heads.index("R")
rots = {"R": 1, "L": -1, "O": 0}
v = np.array([row, col])
print(v, head)
cur_i = 0
for m in re.compile('[LRUDO]').finditer(instr + "O"):
    dist = int(instr[cur_i:m.start()])
    for _ in range(dist):
        g2[v[0]]= g2[v[0]][:v[1]] + arrows[head] + g2[v[0]][v[1]+1:]
        blocked, v, head = move(v, head)
        if blocked:
            break
    cur_i = m.start() + 1
    head = (head + rots[m.group()]) % 4
display()
pw = 1000 * (v[0]+1) + 4 * (v[1]+1) +  head
print(v[0]+1, v[1]+1, head)
print(pw)
