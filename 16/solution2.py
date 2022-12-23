import sys
import numpy as np
import re

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

p = "Valve ([A-Z]{2}) has flow rate=(\d+); tunnels? leads? to valves? "

rs = [re.search(p, l) for l in ll]
rates = dict((r[1], int(r[2])) for r in rs)
outs = dict((r[1], r.string[r.end():].split(", ")) for r in rs)
vs = [r[1] for r in rs]

N = len(vs)
dists = np.full((N,N), np.inf)
np.fill_diagonal(dists, 0)
for i,v in enumerate(vs):
    for v2 in outs[v]:
        dists[i][vs.index(v2)] = 1

for k in range(N):
    for i in range(N):
        dists[i] = np.minimum(dists[i], dists[i,k] + dists[k])
print(dists, dists.shape)

Vs = vs
rs, vs = [], []
for i,v in reversed(list(enumerate(Vs))):
    r = rates[v]
    if r == 0 and v != "AA":
        dists = np.delete(np.delete(dists, i, 0), i, 1)
    else:
        rs.append(r)
        vs.append(v)
rs, vs = rs[::-1], vs[::-1]

def evaluate(path,t):
    i = 0
    out = 0
    for j in path:
        d = dists[i, j]
        i = j
        t -= d
        out += rs[i] * t
    return out

def best_flow(path, t):
    # if t == 0:
    #     return 0, path
    out = sum(rs[i] for i in path)
    best = 0
    best_path = path
    i = path[-1]
    for j in range(N):
        if j in path:
            continue
        d = dists[i, j]
        if d > t:
            continue
        b, p = best_flow(path + [j], t - d) 
        b = b + rs[j] * (t - d)
        if best < b:
            best = b
            best_path = p
        # best = max(best, best_flow(path + [j], t - d))
    # passive = sum(rs[i] for i in path)
    return best, best_path

dists = dists.astype(int) + 1
N = len(dists)
print(best_flow([vs.index("AA")], 30))




def best_flow(path1, path2, t1, t2):
    # if t1 == 0:
    #     return 0, path1, path2
    if len(path1) + len(path2) < 5:
        print(path1, path2)
    best = 0
    # best_path = [vs[k] for k in path1], [vs[k] for k in path2]
    # i1 = path1[-1]
    # i2 = path2[-1]
    if t1 > t2:
        i = path1[-1]
        t = t1
    else:
        i = path2[-1]
        t = t2
    for j in range(N):
        if j in path1 or j in path2:
            continue
        d = dists[i, j]
        if d > t:
            continue
        if t1 > t2:
            b = best_flow(path1 + [j], path2, t1 - d, t2)
        else:
            b = best_flow(path1, path2 + [j], t1, t2 - d) 
        b = b + rs[j] * (t - d)
        # if t1 < t2
        # if best < b:
        #     best = b
            # best_path = p
    # if best_path
        best = max(best, b)
    return best#, best_path

print(best_flow([vs.index("AA")],[vs.index("AA")],26,26))
# P = ["DD", "BB", "JJ", "HH", "EE", "CC"]
# # p = [vs.index(v) for v in P]
# # for V in P:
# i = 0
# out = 0
# t = 31
# p = []
# for V in P:
#     j = vs.index(V)
    
#     d = dists[i, j]
#     if V == "DD":
#         dists -= 1
#     i = j
#     t -= d
#     out += rs[i] * t
#     p.append(i)
#     print(t, i, d, sum(rs[k] for k in p))
# print(out)

# print(dists)
# print(bs)
# print(ps)
