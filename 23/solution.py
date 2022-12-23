import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
grid = open(filename).read().strip().split('\n')
elves = []
for i,r in enumerate(grid):
    for j,c in enumerate(r):
        if c == "#":
            elves.append((i,j))

grid = np.array([[c == "#" for c in r ] for r in grid], dtype=bool)

print(grid)
def north_empty(c):
    return not( (c[0] - 1, c[1]) in elves or  (c[0] - 1, c[1]-1) in elves or  (c[0] - 1, c[1]+1) in elves)

def south_empty(c):
    return not( (c[0] + 1, c[1]) in elves or  (c[0] + 1, c[1]-1) in elves or  (c[0] + 1, c[1]+1) in elves)

def west_empty(c):
    return not ( (c[0], c[1]-1) in elves or  (c[0] - 1, c[1]-1) in elves or  (c[0] + 1, c[1]-1) in elves)

def east_empty(c):
    return not( (c[0], c[1]+1) in elves or  (c[0] - 1, c[1]+1) in elves or  (c[0] + 1, c[1]+1) in elves)

def north(c):
    return  (c[0] - 1, c[1])
def south(c):
    return  (c[0] + 1, c[1])

def west(c):
    return  (c[0], c[1]-1)

def east(c):
    return  (c[0], c[1]+1)

def empty(c):
    # print(c, d_es[0])
    # print(d_es[0](c))
    # print([d_e(c) for d_e in d_es])
    # d_es[0](c) and d_es[1](c) and d_es[2](c) and d_es[3](c)#
    return all([d_e(c) for d_e in d_es])

d_es = [north_empty, south_empty, west_empty, east_empty]
ds = [north, south, west, east]
dis = [0,1,2,3]

def display(elves):

    min_x = min([e[0] for e in elves])
    min_y = min([e[1] for e in elves])
    max_x = max([e[0] for e in elves])
    max_y = max([e[1] for e in elves])
    print(min_x, max_x, min_y, max_y)
    for i in range(min_x, max_x+1):
        r = ""
        for j in range(min_y, max_y+1):
            if (i,j) in elves:
                r += "#"
            else:
                r += "."
        print(r)
display(elves)

round = -1
# while round < 2:
#     round += 1
for round in range(10):
    print("Round", round+1)
    # print(dis)
    props = [None for e in elves]
    ps = []
    moved = False
    for i,e in enumerate(elves):
        if empty(e):
            # props = e
            continue
        for di in dis:
            if d_es[di](e):
                props[i] = ds[di](e)
                ps.append((i, ds[di](e)))
                # moved = True
                # print(props[i])
                break
    # print(ps)
    # print(props)
    # for i in range(len(props)):
    

    # for ind, (i,p) in enumerate(props):

    #     p = props[i]
    #     inds = [j if p == props[j] for j in range(i, len(props))]
    #     if len(inds) == 0:
    #         elves[i] = p
    #     else:

    #         []
    # B = set()
    # for i,p in enumerate(props):
    #     if p is None:
    #         continue
    #     # for j in 
    #     # p = props[i]
    #     if p in props[:i] or p in props[i+1:]:
    #         continue
    #     else:
    #         # print(i, p, elves[i])
    #         if p != elves[i]:
    #             # print("B", i,p)
    #             # B.add((i,p))
    #             # moved = True
    #         elves[i] = p
    
    # A = set()
    while ps:
        i,p = ps.pop()
        a = False
        for ind in reversed(range(len(ps))):
        # for ind, (j,p2) in (enumerate(ps)):
            
            if ps[ind][1] == p:
                ps.pop(ind)
                a = True
        if not a:
            # if p != elves[i]:
            moved = True
            elves[i] = p
            # print("A", i, p)
            # A.add((i,p))
    # print(B-A, A-B)
    if not moved:
        print(round + 1)
        break

    dis = dis[1:] + [dis[0]]
    # display(elves)
# print(elves)

min_x = min([e[0] for e in elves])
min_y = min([e[1] for e in elves])
max_x = max([e[0] for e in elves])
max_y = max([e[1] for e in elves])
print(min_x, max_x, min_y, max_y)

size = (max_x - min_x + 1) * (max_y - min_y + 1)
print((max_x - min_x + 1) , (max_y - min_y + 1))
print(size, len(elves))
print(size - len(elves))


# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))