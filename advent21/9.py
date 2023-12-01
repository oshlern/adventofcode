filename = 'inputs/9.txt'

ll = open(filename).read().strip().split('\n')

n_row = len(ll)
n_col = len(ll[0])

grid = [[int(c) for c in l] for l in ll]


def neighbors(pos):
    i,j = pos
    ns = []
    if i != 0:
        ns.append((i-1, j))
    if i != n_row-1:
        ns.append((i+1, j))
    if j != 0:
        ns.append((i, j-1))
    if j != n_col-1:
        ns.append((i, j+1))
    return ns

def basin_size(pos):
    b = set([pos])
    checked = set([pos])
    for n in neighbors(pos):
        expand(b, n, checked)
    print(len(b), b)
    return len(b)

def expand(b, pos, checked):
    if grid[pos[0]][pos[1]] == 9:
        return
    in_b = True
    ns = neighbors(pos)
    for n in ns:
        if grid[n[0]][n[1]] < grid[pos[0]][pos[1]]:
            if not (n in b):
                in_b = False
                break
    # print(pos, grid[pos[0]][pos[1]], in_b, b)
    if in_b:
        b.add(pos)
        checked.add(pos)
        for n in ns:
            if not (n in checked):
                expand(b, n, checked)

    


total = 0
basins = []
for i in range(n_row):
    for j in range(n_col):
        # neighbors = []
        # if i!= 0:
        #     neighbors.append()
        low = ((i == 0 or ll[i-1][j] > ll[i][j])
                and (i == n_row-1 or ll[i+1][j] > ll[i][j])
                and (j == 0 or ll[i][j-1] > ll[i][j])
                and (j == n_col-1 or ll[i][j+1] > ll[i][j]))
        if low:
            # print(i, j,ll[i][j] )
            risk = int(ll[i][j]) + 1
            total += risk
        if low:
            s = basin_size((i, j))
            basins.append(s)
print(total)
import numpy as np
print(basins)
bs = np.sort(basins)
print(bs[-1] * bs[-2] * bs[-3])
print(bs[-1], bs[-2], bs[-3])
