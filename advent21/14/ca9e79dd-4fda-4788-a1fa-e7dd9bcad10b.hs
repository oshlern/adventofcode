import sys
import numpy as np
import string
from collections import defaultdict
from itertools import memoize

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n\n')
Ls = string.ascii_uppercase

P = ll[0].strip()
ts = [l.split(' -> ') for l in ll[1].split('\n')]
ts = {t[0]: t[1] for t in ts}
print(ts)

Ls = set()
for t in ts:
    for c in t:
        Ls.add(t)
        Ls.add(ts[t])

@memoize
def _counts(a,b):
    

d = {}
for sam in ts:
    p = sam 
    for round in range(40):
        print(round)
        new_p = ""
        for i in range(len(p)-1):
            new_p += p[i]
            # print(p[i:i+2], p[i:i+2] in ts)
            new_p += ts.get(p[i:i+2], "")
        new_p += p[-1]
        # print(new_p)
        p = new_p
    p = p[1:-1]
    counts = [p.count(L) for L in Ls]
    d[sam] = counts

p = P
counts = [p.count(L) for L in Ls]
for i in range(len(p)-1):
    new_p += p[i]
    # print(p[i:i+2], p[i:i+2] in ts)
    if p[i:i+2] in d:
        counts = [c + n for c,n in zip(counts, d[p[i:i+2]])] 
# )

#     new_p += ts.get(p[i:i+2], "")
# new_p += p[-1]
    # print(new_p)
    # p = new_p
# counts = [p.count(L) for L in Ls if L in p]

# counts = [p.count(L) for L in Ls if L in p]
print(max(counts) - min(counts))