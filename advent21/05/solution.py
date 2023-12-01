import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [int(l) for l in ll if len(l) > 0]

grid = np.zeros((1000,1000))
for l in ll:
    c = l.split(' -> ')
    a = np.array(eval('['+c[0]+']'))
    b = np.array(eval('['+c[1]+']'))
    # print(a, b, l)
    # if (a-b)[0] != 0 and (a-b)[1] != 0:
    #     continue
    # d = int(np.linalg.norm(a-b))
    d = int(max(abs((a-b)[0]), abs((a-b)[1])))
    for i in range(d):
        cur = a + i*(b-a)/d 
        # print(cur)
        grid[int(cur[0])][int(cur[1])] += 1
    grid[int(b[0])][int(b[1])] += 1

# print(grid)
# for r in grid:
#     print(''.join([str(int(c)) for c in r]))
print(np.sum(grid >= 2))
    