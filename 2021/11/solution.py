import sys
import numpy as np
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

ns = np.array([[int(n) for n in r] for r in ll])
def nbrs(p, shape):
    min_i = p[0]-1 if p[0] > 0 else p[0]
    max_i = p[0]+1 if p[0] < shape[0]-1 else p[0]
    min_j = p[1]-1 if p[1] > 0 else p[1]
    max_j = p[1]+1 if p[1] < shape[1]-1 else p[1]
    ns = [(i,j) for i in range(min_i, max_i+1) for j in range(min_j, max_j+1) if i != p[0] or j != p[1]]
    return ns

nf = 0
for round in range(100000):
    if round % 10 == 0:
        print(round, nf)
    # print(round, ns.shape)
    # for r in ns:
    #     print(''.join(map(str,r)))
    ns += 1
    # print(ns)
    # print(np.argwhere(ns>=9))
    to_f = set([tuple(x) for x in np.argwhere(ns>9)])
    # print(to_f)
    has_f = set()
    while to_f:
        nf += 1
        i,j = to_f.pop()
        has_f.add((i,j))
        for x,y in nbrs((i,j),ns.shape):
            if (x,y) in has_f:
                continue
            ns[x,y] += 1
            if ns[x,y] > 9:
                to_f.add((x,y))
    if len(has_f) == np.prod(ns.shape):
        print("ROUND", round+1)
        break
    ns = np.where(ns > 9, 0, ns)
print(round, nf)
print(nf)