import itertools# N = int(input())

ps = [
    [0.000, 0.000],
    [0.000, 2.000],
    [1.000, 1.800],
    [1.000, 0.200],
    [1.800, 1.000],
    [2.000, 0.000],
    [2.000, 2.000]
]
P = 0.61413
n = 7
inds = list(range(len(ps)))
Ccws = {}
ccws = []
for A in inds:
    _grid = []
    for B in inds:
        _row = []
        for C in inds:
            x = (ps[C][1]-ps[A][1])*(ps[B][0]-ps[A][0]) > (ps[B][1]-ps[A][1])*(ps[C][0]-ps[A][0])
            _row.append(x)
            Ccws[(A,B,C)] = x

# def ccw(A,B,C):
#     return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

# can 4x
# for A in range(n):
#     for B in range(A+1, n):
#         for C in range(A+1, n):
#             if C == B:
#                 continue

Xs = {}
Xs = set()
for A in inds:
    for B in inds:
        if A == B:
            continue
        for C in inds:
            if A == C or B == C:
                continue
            for D in inds:
                if A == D or B == D or C == D:
                    continue
                x =  Ccws[(A,C,D)] != Ccws[(B,C,D)] and Ccws[(A,B,C)] != Ccws[(A,B,D)]
                if x:
                    Xs.add(((A,B),(C,D)))

# edges = []
# V0 = inds[0]
# Vs = [V0]
# inds_left = set(inds)
# inds_left.remove(V0)
# for i in range(1,n):
#     for V in inds:
#         if V in Vs:
#             continue
# inds = set(inds)
def expand(i, inds_left, last_V, edges, area):
    print(i, inds_left)
    if i == n-1:
        V = inds_left.pop()
        new_edge1 = (last_V,V)
        new_edge2 = (V,V0)
        if any([(edge, new_edge1) in Xs for edge in edges]) or any([(edge, new_edge1) in Xs for edge in edges]):
            return
        da1 = ps[new_edge1[0]][0]*ps[new_edge1[1]][1] - ps[new_edge1[0]][1]*ps[new_edge1[1]][0]
        da2 = ps[new_edge2[0]][0]*ps[new_edge2[1]][1] - ps[new_edge2[0]][1]*ps[new_edge2[1]][0]
        area = area - da1 - da2
        area = area / 2
        prob = area / 4
        prob = prob ** 3
        if abs(prob - P) <= 0.00001:
            Vs = [e[0] for e in edges] + [last_V, V]
            return Vs
    else:
    for V in inds_left:
        new_edge = (last_V,V)
        if any([(edge, new_edge) in Xs for edge in edges]):
            continue
        da = ps[new_edge[0]][0]*ps[new_edge[1]][1] - ps[new_edge[0]][1]*ps[new_edge[1]][0]
        o = expand(i+1, inds_left - set([V]), V, edges + [new_edge], area - da)
        if o:
            return o
    return os
V0 = inds[0]
o = expand(1, set(inds) - set([V0]), V0, [], 0)
print([x+1 for x in o[0]])
# area = 0
# for V1 in set(inds) - set(Vs):
#     new_edge = (V0,V1)
#     if any([(edge, new_edge) in Xs for edge in edges]):
#         continue
#     edges.append(new_edge)
#     da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#     for V2 in set(inds) - set(Vs):
#         new_edge = (V1,V2)
#         if any([(edge, new_edge) in Xs for edge in edges]):
#             continue
#         edges.append(new_edge)
#         da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#         for V3 in set(inds) - set(Vs):
#             new_edge = (V2,V3)
#             if any([(edge, new_edge) in Xs for edge in edges]):
#                 continue
#             edges.append(new_edge)
#             da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#             for V4 in set(inds) - set(Vs):
#                 new_edge = (V3,V4)
#                 if any([(edge, new_edge) in Xs for edge in edges]):
#                     continue
#                 edges.append(new_edge)
#                 da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#                 for V5 in set(inds) - set(Vs):
#                     new_edge = (V4,V5)
#                     if any([(edge, new_edge) in Xs for edge in edges]):
#                         continue
#                     edges.append(new_edge)
#                     da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#                     for V6 in set(inds) - set(Vs):
#                         new_edge = (V5,V6)
#                         if any([(edge, new_edge) in Xs for edge in edges]):
#                             continue
#                         new_edge2 = (V6,V0)
#                         if any([(edge, new_edge2) in Xs for edge in edges]):
#                             continue
#                         # edges.append(new_edge)
#                         # edges.append(new_edge)
#                         da = new_edge[0][0]*new_edge[1][1] - new_edge[0][1]*new_edge[1][0]
#                         area += new_edge2[0][0]*new_edge2[1][1] - new_edge2[0][1]*new_edge2[1][0]
#                     edges = edges[:-1]
#                     area -= 
