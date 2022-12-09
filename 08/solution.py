import sys
# import functools, string, itertools, collections, re
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

grid = np.array([[int(c) for c in l] for l in ll])

nr = len(grid)
nc = len(grid[0])


max_d = 0
for i in range(nr):
    for j in range(nr):
        h = grid[i,j]
        vls = np.flip(grid[i,:j]) < h
        vrs = grid[i,j+1:] < h
        vts = np.flip(grid[:i,j]) < h
        vbs = grid[i+1:,j] < h
        vs = [vls, vrs, vts, vbs]
        v_w = [np.where(np.logical_not(v))[0] for v in vs]
        ds = [w[0] + 1 if len(w) > 0 else len(v) for w,v in zip(v_w, vs)]
        d = np.prod(ds)
        if d > max_d:
            max_d = d
print(max_d)


# total = 0
# for i in range(nr):
#     for j in range(nr):
#         h = grid[i,j]
#         vis_left = np.all(grid[i,:j] < h)
#         vis_right = np.all(grid[i,j+1:] < h)
#         vis_top = np.all(grid[:i,j] < h)
#         vis_bot = np.all(grid[i+1:,j] < h)
#         vis = vis_left or vis_right or vis_top or vis_bot
#         total += vis
# print(total)