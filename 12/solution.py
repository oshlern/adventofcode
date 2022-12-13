import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip()



si = ll.index('S')
ei = ll.index('E')

def nbrs(i, j):
    ns = []
    if i < nr - 1:
        ns.append([i+1,j])
    if i > 0:
        ns.append([i-1,j])
    if j < nc - 1:
        ns.append([i,j+1])
    if j > 0:
        ns.append([i,j-1])
    # return ns
    return [tuple(n) for n in ns]

def get(cur):
    global grid
    c = grid[cur[0]][cur[1]]
    if c == "S":
        c = "a"
    if c == "E":
        c = "z"
    return c

grid = ll.split('\n')
nr = len(grid)
nc = len(grid[0])
s = (si // (nc + 1), si % (nc + 1))
e = (ei // (nc + 1), ei % (nc + 1))
print(s, e)
print(si, ei, nr, nc)
ds = {s: 0}
q = [s]

for i in range(nr):
    for j in range(nc):
        if grid[i][j] == "a":
            q.append((i,j))
            ds[(i,j)] = 0
while len(q) > 0:
    cur = q.pop(0)
    # print(cur)
    ns = nbrs(cur[0], cur[1])
    for n in ns:
        if n in ds:
            continue
        if ord(get(cur)) < ord(get(n)) - 1:
            continue
        ds[n] = ds[cur] + 1
        # print(n, ds[n])
        q.append(n)
print(ds)
print(ds[e])