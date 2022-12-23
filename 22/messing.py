# automatic folding
# cube with current position as top? Translate headings
import sys
import numpy as np
import re
import copy
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().split('\n\n')
grid = ll[0].split('\n')
instr = ll[1]
heads = "RDLU"
arrows = ">v<^"
s = 50 if len(sys.argv) == 1 else 4



dvecs = {
    "R": np.array([0,1]),
    "L": np.array([0,-1]),
    "U": np.array([-1,0]),
    "D": np.array([1,0]),
}
dvecs = {heads.index(head): dvecs[head] for head in heads}


i0 = 0
j0 = re.search('[^ ]', grid[0]).start()
head = 0
head_3d = np.array([1,0,0])

seen = set([(i0,j0)])
neighbors = defaultdict(list)
to_visit = [(i0, j0, head, head_3d)]
normals = {(i0,j0): np.array([0,0,1])}


while to_visit:
    print(to_visit)
    print("\t", normals)
    i, j, head, head_3d = to_visit.pop(0)
    for turn in [-1, 0, 1]:
        nhead = (head + turn) % 4
        disp = s * dvecs[nhead]
        ni, nj = i + disp[0], j + disp[1]
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[ni]) and grid[ni][nj] != " ":
            if (ni,nj) in normals:
                continue
            if turn == 0:
                nhead_3d = head_3d
            else:
                nhead_3d = turn * np.cross(head_3d, normals[(i,j)])
            normals[(ni,nj)] = nhead_3d
            # save head and head3d info?
            to_visit.append((ni, nj, nhead, -normals[(i,j)]))
print(normals)


class Vertex:
    # def __init__(self):
    #     self.pos = None
    #     self.head = None
    #     self.normal = None

        # pass
    def set_init(self):
        # self.pos = np.array([0,0,0])
        self.head = np.array([1,0,0])
        self.normal = np.array([0,0,1])

    def join_to(self, v, turn):
        if turn == 0:
            new_head = v.head
        else:
            new_head = turn * np.cross(v.head, v.normal)
        self.normal = new_head
        self.head = -v.normal

faces = {(i0,j0): (np.array([1,0,0]), np.array([0,0,1]))}

face = (i0,j0)



