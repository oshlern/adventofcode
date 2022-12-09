import sys
# import functools, string, itertools, collections, re
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

def add(x, y):
    return [x[0] + y[0], x[1] + y[1]]

visited = set()
# h = [0,0]
# t = [0,0]
knot = []
for i in range(10):
    knot.append(np.array([0,0], int))
ds = {
    "R": np.array((1, 0)),
    "L": np.array((-1, 0)),
    "U": np.array((0, 1)),
    "D": np.array((0, -1)),
}

def dist(x, y):
    return np.max(np.abs(x - y))
    # return max([abs(x[0] - y[0]) + abs(x[1] - y[1]])

def move(t, h):
    # print(t, h)
    if dist(t, h) > 1:
        t += np.sign(h -t)
    # if (t[0] < h[0] - 1):
    #     # print("a")
    #     t[0] = h[0] - 1
    #     t[1] = t[1] 
    #     t[1] = h[1]
    # elif (t[0] > h[0] + 1):
    #     # print("b")
    #     t[0] = h[0] + 1
    #     t[1] = h[1]
    # elif (t[1] < h[1] - 1):
    #     # print("c")
    #     t[1] = h[1] - 1
    #     t[0] = h[0]
    # elif (t[1] > h[1] + 1):
    #     # print("d")
    #     t[1] = h[1] + 1
    #     t[0] = h[0]
    # # print(t, "___")
    return t

def disp(knot):
    z = zip(*knot)
    x = next(z)
    y = next(z)
    # print(x)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    grid = -np.ones((xmax - xmin + 1, ymax-ymin + 1))
    # print(knot)
    for i,k in enumerate(reversed(knot)):
        # print
        grid[k[0]-xmin,k[1]-ymin] = 9-i
    # print(grid)
    grid = np.flip(grid.T, axis=0)
    for r in grid:
        s = "\t\t\t"
        for c in r:
            if c == -1:
                s += '.'
            elif c == 0:
                s += 'H'
            else:
                s += str(int(c))
                # print(str(int(c)), "__", len(str(c)))
            # print('__', len(r), len(s))

        # print(len(r), len(s))
        print(s)
    # print('\n')
    # for i in range(xmax-xmin):

for l in ll:
    print(l)
    d_s, n_s = l.split(' ')
    d = ds[d_s]
    n = int(n_s)
    # print(knot[0], knot[-1])
    # print(d_s, d)
    for i in range(n):
        # print(knot[0])
        knot[0] += d
        for j in range(1,10):
            if dist(knot[j], knot[j-1]) > 1:
                # print('\t', j, dist(knot[j], knot[j-1]), knot[j], knot[j-1])
                knot[j] += np.sign(knot[j-1] - knot[j])
                # print('\t',knot[j])

            # knot[j] = move(knot[j], knot[j-1])
        # print(d_s, d)
        # disp(knot)
        # knot[0] = add(knot[0], d)
        # for j in range(1,10):
        #     knot[j] = move(knot[j], knot[j-1])
        # print(i+1, knot[0], knot[-1])
        # print()
        visited.add(tuple(knot[-1]))
        # break
    # print(d_s, d)
    # disp(knot)
    # break
# print(visited)
print(len(visited))
