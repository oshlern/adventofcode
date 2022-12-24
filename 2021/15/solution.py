import sys
import numpy as np
from collections import defaultdict
from heapq import *

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

grid = np.array([[int(n) for n in l] for l in ll])
start = (0,0)
end = (grid.shape[0]-1, grid.shape[1]-1)
print(end)
# min_risk = {start: 0}
min_risk = {}

ds = {
    "U": [-1,0],
    "D": [1,0],
    "R": [0,1],
    "L": [0,-1],
}
ds = [np.array(d) for d in ds.values()]

def inside(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

# to_explore = set([start])
# for dist in range(grid.shape[0] + grid.shape[1]+3):

# h.append(0, start)
# h = []
# heappush(h, (0, start))

q = {start: 0}#grid[start[0],start[1]]}
# while not (end in min_risk):
while q:
    # min_key, min_val = None, np.inf
    # for key in q:
    #     if q[key] < min_val:
    #         min_key, min_val = key, q[key]
    c, d = min(q.items(), key=lambda p: p[1])
    # print(q, c, d)
    d = q.pop(c)
    min_risk[c] = d
    # c, d = min_key, min_val
    # d = min
    # d, c = heappop(h)

    # for c in min_risk:
    # print(to_explore)
    # nexp = set()
    # for c in to_explore:
    # c = to_explore.pop()
# while not end in min_risk:
    for d in ds:
        n = (c[0] + d[0], c[1]+ d[1])
        # print(n, n in min_risk, inside(n, grid.shape), (n in q))
        # if n == end:
        #     print("DD", min_risk[c] + grid[n[0]][n[1]])
        #     exit()
        if n in min_risk:
            continue
        if not inside(n, grid.shape):
            continue
        nrisk = min_risk[c] + grid[n[0]][n[1]]
        if not (n in q) or nrisk < q[n]:
            q[n] = nrisk
        
        # if nrisk < min_risk[n]:
        #     min_risk[n] = nrisk
        # if n in min_risk:
        #     continue
        # if n in to_explore:
        #     continue
        # nexp.add(n)
        # min_risk[n] = min_risk[c] + grid[n[0]][n[1]]
        # if n == end:
        #     print("DD", min_risk[n])#min_risk[c] + grid[n[0]][n[1]])
        #     exit()
                # to_explore()
    # to_explore = nexp

# print(min_risk)
print(min_risk[end])

        

