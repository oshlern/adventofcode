import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [eval(l) for l in ll if len(l) > 0]

# grid = 
ws = set()
for l in ll:
    cs = l.split(' -> ')
    # first = cs[0]
    c = np.array(eval('['+cs[0]+']'))
    # c = cs[0].split(',')
    # c = np.array([int(c[0]), int(c[1])])
    last = c
    for c in cs[1:]:
        # c = c.split(',')
        # c = np.array([int(c[0]), int(c[1])])
        c = np.array(eval('['+c+']'))
        dist = int(np.linalg.norm(c - last))
        for i in range(int(dist)):
            cur = last + i*(c-last)/dist
            ws.add((int(cur[0]), int(cur[1])))
        last = c
    ws.add((int(last[0]), int(last[1])))

ws = np.array([list(w) for w in ws])
print(ws)

buff = 1000
grid = np.zeros((buff + max(ws[:,0])+1+buff, max(ws[:,1])+3), dtype=bool)
for w in ws:
    grid[buff+w[0],w[1]] = True

grid[:,-1] = True

print(grid)
si = 0
while True:
    si += 1
    s = [buff + 500, 0]
    print(si)
    while s[1] < grid.shape[1]-1:
        if grid[s[0],s[1]+1]:
            if s[0] > 1 and not grid[s[0]-1,s[1]+1]:
                s[0] -= 1
            elif s[0] < grid.shape[0]-1 and not grid[s[0]+1,s[1]+1]:
                s[0] += 1
            else:
                break
        s[1] += 1
        # print(s)
    else:
        break

    grid[s[0],s[1]] = True
    # if si> 3:
    #     break
    if s == [buff + 500,0]:
        break
print(si-1)
