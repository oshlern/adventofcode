import itertools

def expand(i, inds_left, last_V, edges, area):
    if i == n-1:
        V = inds_left.pop()
        new_edge1 = (last_V,V)
        new_edge2 = (V,V0)
        if any([(edge, new_edge1) in Xs for edge in edges]) or any([(edge, new_edge2) in Xs for edge in edges]):
            return 0
        da1 = ps[new_edge1[0]][0]*ps[new_edge1[1]][1] - ps[new_edge1[0]][1]*ps[new_edge1[1]][0]
        da2 = ps[new_edge2[0]][0]*ps[new_edge2[1]][1] - ps[new_edge2[0]][1]*ps[new_edge2[1]][0]
        area = (area - da1 - da2)/2
        prob = (area/4) ** 3
        if abs(prob - P) <= 0.00001:
            Vs = [e[0] for e in edges] + [last_V, V]
            print([v+1 for v in Vs])
            return 1
    else:
        for V in inds_left:
            new_edge = (last_V,V)
            if any([(edge, new_edge) in Xs for edge in edges]):
                continue
            da = ps[new_edge[0]][0]*ps[new_edge[1]][1] - ps[new_edge[0]][1]*ps[new_edge[1]][0]
            if expand(i+1, inds_left - set([V]), V, edges + [new_edge], area - da):
                return 1

n = 7
inds = list(range(n))
V0 = inds[0]

N = int(input())
for test_case in range(N):
    ps = [list(map(float, input().split(" "))) for _ in range(n)]
    P = float(input())
    Ccws = {(A,B,C): (ps[C][1]-ps[A][1])*(ps[B][0]-ps[A][0]) > (ps[B][1]-ps[A][1])*(ps[C][0]-ps[A][0])
            # for A,B,C in itertools.combinations(inds,3)}
            for A,B,C in itertools.product(inds,repeat=3) if A != B and B!= C and C!= A}
    Xs = set(((A,B),(C,D)) 
    #for A,B,C,D in itertools.combinations(inds, 4)
            for A,B,C,D in itertools.product(inds,repeat=4)
            if A != B and B!= C and C!= A and D != A and D!= B and D!= C and 
            Ccws[(A,C,D)] != Ccws[(B,C,D)] and Ccws[(A,B,C)] != Ccws[(A,B,D)])
    A,B,C,D = 2,3,4,0
    # print(Ccws)
    # print(((2,3),(4,0)) in Xs)
    # print(ps[2], ps[3], ps[4], ps[0])
    # print(Ccws[(A,C,D)] != Ccws[(B,C,D)], Ccws[(A,B,C)] != Ccws[(A,B,D)])
    # print("____")
    # break
    o = expand(1, set(inds) - set([V0]), V0, [], 0)
    # print([x+1 for x in o])


# ps = [
#     [0.000, 0.000],
#     [0.000, 2.000],
#     [1.000, 1.800],
#     [1.000, 0.200],
#     [1.800, 1.000],
#     [2.000, 0.000],
#     [2.000, 2.000]
# ]
# P = 0.61413