import sys
import numpy as np
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [l.split('-') for l in ll]

nodes = set()
nbs = defaultdict(set)
for l in ll:
    a, b = l.split('-')
    nodes.add(a)
    nodes.add(b)
    nbs[a].add(b)
    nbs[b].add(a)

def num_ps(p, twice=False):
    a = p[-1]
    out = 0
    for n in nbs[a]:
        if n == "start":
            continue
        if n == "end":
            # print(p)
            out += 1
            continue
        if not n.isupper():
            if n in p:
                if twice:
                    continue
                else:
                    out += num_ps(p + [n],True)
            else:
                out += num_ps(p + [n],twice)
        else:
            out += num_ps(p + [n],twice)
        
    return out
print(num_ps(["start"]))

