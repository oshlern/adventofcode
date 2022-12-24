import sys
import numpy as np
import string
from collections import defaultdict
import functools

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

@functools.cache
def _counts(a,b, n): # all but last
    if n == 0 or not(a + b in ts):
        return defaultdict(int, {a: 1})
    n -= 1
    z = ts[a+b]
    c1 = _counts(a, z, n)
    c2 = _counts(z, b, n)
    c = {L: c1[L] + c2[L] for L in Ls}
    # c[z] -= 1
    return c


# d = {}
# for sam in ts:
#     p = sam 
#     for round in range(40):
#         print(round)
#         new_p = ""
#         for i in range(len(p)-1):
#             new_p += p[i]
#             # print(p[i:i+2], p[i:i+2] in ts)
#             new_p += ts.get(p[i:i+2], "")
#         new_p += p[-1]
#         # print(new_p)
#         p = new_p
#     p = p[1:-1]
#     counts = [p.count(L) for L in Ls]
#     d[sam] = counts

p = P
# counts = [p.count(L) for L in Ls]
counts = defaultdict(int)
for i in range(len(p)-1):
    c0 = _counts(p[i], p[i+1], 40)
    for L in Ls:
        counts[L] += c0[L]
counts[p[-1]] += 1

counts = {L: counts[L] for L in counts if counts[L] > 0 }

#     new_p += ts.get(p[i:i+2], "")
# new_p += p[-1]
    # print(new_p)
    # p = new_p
# counts = [p.count(L) for L in Ls if L in p]

# counts = [p.count(L) for L in Ls if L in p]
print(max(counts.values()), min(counts.values()))
print(max(counts.values()) - min(counts.values()))