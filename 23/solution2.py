import sys
import numpy as np
import time

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
grid = open(filename).read().strip().split('\n')
elves = []
for i,r in enumerate(grid):
    for j,c in enumerate(r):
        if c == "#":
            elves.append((i,j))

grid = np.array([[c == "#" for c in r ] for r in grid], dtype=bool)
min_x = min([e[0] for e in elves])
min_y = min([e[1] for e in elves])
max_x = max([e[0] for e in elves])
max_y = max([e[1] for e in elves])
min_x -= 1
grid = np.insert(grid, 0, False, axis=0)
max_x += 1
grid = np.insert(grid, grid.shape[0], False, axis=0)
min_y -= 1
grid = np.insert(grid, 0, False, axis=1)
max_y += 1
grid = np.insert(grid, grid.shape[1], False, axis=1)


def display():
    print(grid.shape)
    for r in grid:
        print(''.join(["#" if c else "." for c in r]))
    # min_x = min([e[0] for e in elves])
    # min_y = min([e[1] for e in elves])
    # max_x = max([e[0] for e in elves])
    # max_y = max([e[1] for e in elves])
    # print(min_x, max_x, min_y, max_y)
    # for i in range(min_x, max_x+1):
    #     r = ""
    #     for j in range(min_y, max_y+1):
    #         if (i,j) in elves:
    #             r += "#"
    #         else:
    #             r += "."
    #     print(r)
# display(elves)

dirs = [
    (-1,0,0,1,0,3),
    ( 1,0,2,3,0,3),
    (0,-1,0,3,0,1),
    (0, 1,0,3,2,3),
]
i0s = [-1,1,0,0]
j0s = [0,0,-1,1]
start = time.time()
d_ind = 0
all_ems = None

# print(grid, min_x, min_y, max_x, max_y)
round = -1
while True:
    round += 1
    if round % 100 == 0:
        # print(round)
# for round in range(10):
        print("Round", round+1)
    # display()
    ps = []
    moved = False
    for i,e in enumerate(elves):
        ns = grid[e[0]-1-min_x:e[0]+2-min_x, e[1]-1-min_y:e[1]+2-min_y]
        n_emps = [np.any(ns[0]), np.any(ns[2]), np.any(ns[:,0]), np.any(ns[:,2])]
        if any(n_emps):
            for di in range(d_ind, d_ind + 4):
                di = di % 4
                if not n_emps[di]:
                    ps.append((i, (e[0] + i0s[di], e[1] + j0s[di])))
                    break
    # e_ms = set()
    while ps:
        i,p = ps.pop()
        n = len(ps)
        ps = [x for x in ps if x[1] != p]
        if len(ps) == n:
            moved = True
            # e_ms.add(i)
            # if p[0] == min_x:
            #     min_x -= 1
            #     grid = np.insert(grid, 0, np.zeros((grid.shape[0], 1), dtype=bool))#, grid, axis=1)
            # elif p[0] == max_x:
            #     max_x += 1
            #     grid =  np.insert(grid, -1, np.zeros((grid.shape[0], 1), dtype=bool))
            if p[0] == min_x:
                # print("before minx", p, grid.shape, min_x)
                min_x -= 1
                grid = np.insert(grid,  0, False, axis=0)
                # print("after minx", p, grid.shape, min_x)

            elif p[0] == max_x:
                # print("before maxx", p, grid.shape, max_x)
                max_x += 1
                grid = np.insert(grid, grid.shape[0], False, axis=0)
                # print("after maxx", p, grid.shape, max_x)

            elif p[1] == min_y:
                # print("before miny", p, grid.shape, min_y)
                min_y -= 1
                grid = np.insert(grid,  0, False, axis=1)
                # print("after miny", p, grid.shape, min_y)

            elif p[1] == max_y:
                # print("before maxy", p, grid.shape, min_x)
                max_y += 1
                grid = np.insert(grid, grid.shape[1], False, axis=1)
                # print("after maxy", p, grid.shape, min_x)

            grid[elves[i][0]-min_x,elves[i][1]-min_y] = False
            grid[       p[0]-min_x,       p[1]-min_y] = True
            elves[i] = p
    # if all_ems:
    #     print(len(e_ms - all_ems), len(all_ems - e_ms), len(elves))
    #     # print()
    # else:
    #     print(len(e_ms))
    # all_ems = e_ms

    d_ind += 1

    if not moved:
        print(round + 1)
        break

end = time.time()
print("time", end - start)
    # display(elves)
# print(elves)

# min_x = min([e[0] for e in elves])
# min_y = min([e[1] for e in elves])
# max_x = max([e[0] for e in elves])
# max_y = max([e[1] for e in elves])
print(min_x, max_x, min_y, max_y)

size = (max_x - min_x - 1) * (max_y - min_y - 1)
print((max_x - min_x - 1) , (max_y - min_y - 1))
print(size, len(elves))
print(size - len(elves))



# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))