import sys
import numpy as np
import re
import copy

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().split('\n\n')
instr = ll[-1]
heads = "RDLU"

grid = ll[0].split('\n')

ms = [re.search('[\.#]+', r) for r in grid]
r_starts = [m.start() for m in ms]
r_ends = [m.end()-1 for m in ms]

c_starts = []
c_ends = []
for j in range(max(map(len, grid))):
    first = True
    start = -1
    end = -1
    for i, r in enumerate(grid):
        if j < len(r) and r[j] != " ":
            if first:
                # print(i )
                first = False
                start = i
            end = i
    c_starts.append(start)
    c_ends.append(end)



dvecs = {
    "R": np.array([0,1]),
    "L": np.array([0,-1]),
    "U": np.array([-1,0]),
    "D": np.array([1,0]),
}
dvecs = {heads.index(head): dvecs[head] for head in heads}
edges = [
    ((0,50), (0,99)),
    ((0,0), (0,99)),
    ((0,50), (0,99)),
    

]

# vertex_gluings = [
#     ((0,50), (150,0)),
#     ((0,100), (199,0)),
#     ((0,149), (199,49)),
#     ((0,100), (199,0)),
#     ((0,100), (199,0)),
# ]
edge_pairs = [
    [((0,50), (0,99)), ((150,0), (199,0))],
    [((0,50), (49,50)), ((149,0), (100,0))],
    [((0,100), (0,149)), ((199,0), (199,49))],
    [((0,149), (49,149)), ((199,99), (150,99))],
    [((49,100), (49,149)), ((50,99), (99,99))],
    [((50,50), (99,50)), ((100,0), (100,49))],
    [((149,100), (149,149)), ((150,49), (199,49))],
]

# class Edge:
#     def __init__(self, v1, v2):
#         self.v1 = v1
#         self.v2 = v2
#         self.horz = v1[0] == v2[0]
#         self.vert = v1[1] == v2[1]

#     def intersects(self, e):
#         if self.horz == e.horz:
#             return False
#         dist = np.dot(e.u1 - self.v1, dvec)



class Edge:
    def __init__(self, v, head, passing_head=None, dist=49):
        if type(head) == str:
            head = heads.index(head)
        self.v = np.array(v)
        self.head = head
        self.dvec = dvecs[head]
        self.dist = dist
        self.passing_head = passing_head
        # self.v2 = v + dist * self.dvec
        self.horz = head % 2 == 0#head in "RL"

    def intersects(self, e):
        if e.head == self.passing_head:
            d = np.dot(e.v - self.v, self.dvec)
            if 0 <= d <= self.dist:
                return d 
        # if self.horz == e.horz:
            # return False
        
        return False
    
    def get_at(self, dist):
        return self.v + dist * self.dvec
    
    def __str__(self):
        return "({self.v[0]},{self.v[1]}) {heads[self.head]}{self.dist}"

edge_pairs = [
    [Edge((  0,  50), "R"), Edge((150,   0), "D")],
    [Edge((  0,  50), "D"), Edge((149,   0), "U")],
    [Edge((  0, 100), "R"), Edge((199,   0), "R")],
    [Edge((  0, 149), "D"), Edge((199,  99), "U")],
    [Edge(( 49, 100), "R"), Edge(( 50,  99), "D")],
    [Edge(( 50,  50), "D"), Edge((  0, 100), "R")],
    [Edge((149,  50), "R"), Edge((150,  49), "D")],
]

if len(sys.argv) > 1:

    edge_pairs = [
        [Edge(( 0,  8), "R"), Edge(( 4,  3), "L")],
        [Edge((15,  8), "R"), Edge(( 7,  3), "L")],
        [Edge(( 0,  8), "D"), Edge(( 4,  4), "R")],
        [Edge((15,  8), "U"), Edge(( 7,  4), "R")],
        [Edge(( 4, 11), "D"), Edge(( 8, 12), "R")],
        [Edge(( 0, 13), "D"), Edge((15, 15), "U")],
        [Edge(( 5,  0), "D"), Edge((15, 15), "L")],
    ]
edges = sum(edge_pairs, [])
for pair in edge_pairs:
    pair[0].pair = pair[1]
    pair[1].pair = pair[0]


def move(v, head):
    motion = Edge(v, head, dist=1)
    for edge in edges:
        d = edge.intersects(motion)
        if d:
            nv = edge.pair.get_at(d)
            nhead = (head + edge.pair.head - edge.head) % 4
            print("--", v, head, d, nv)
            break
    else:
        nv = motion.get_at(1)
        print("_._", nv)
        nhead = head


    if grid[nv[0]][nv[1]] == "#":
        return True, v, head
    else:
        assert grid[nv[0]][nv[1]] == "."
        return False, nv, nhead



def move_d(v, head, dist):
    for _ in range(dist):
        blocked, v, head = move(v, head)
        if blocked:
            break
    return v, head


def display(grid, v, head):
    print("\n\n")
    g2 = copy.deepcopy(grid)
    g2[v[0]]= g2[v[0]][:v[1]] + heads[head] + g2[v[0]][v[1]+1:]
    for r in g2:
        print(r)




col = re.search('[^ ]', grid[0]).start()
row = 0
head = heads.index("R")
print(set(zip(r_starts, r_ends)))
print(set(zip(c_starts, c_ends)))
rots = {"R": 1, "L": -1, "O": 0}
v = np.array([row, col])
print(v, head)
cur_i = 0
for m in re.compile('[LRUDO]').finditer(instr + "O"):
    dist = int(instr[cur_i:m.start()])
    for _ in range(dist):
        display(grid, v, head)
        blocked, v, head = move(v, head)
        if blocked:
            break
    cur_i = m.start() + 1
    head = (head + rots[m.group()]) % 4

pw = 1000 * (row+1) + 4 * (col+1) +  head
# print(pw)

# I 

# def find_edge(row, col, head):
#     for pair in edge_pairs:
#         for i, edge in pair:
#             if edge[0][0] <= row <= edge[1][0] and edge[0][1] <= col <= edge[1][1]:
#                 if edge[0][0] == edge[1][0]:
#                     if head == "R" or head == "L":
#                         p = col - edge

#             if edge[0][0] == edge[1][1]:
#                 if edge 

# edge_gluings = {((0,50), (0,99)): }
