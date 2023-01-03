def solution(banana_list):
    graph = []
infs = set()
def infinite(n1, n2):
    visited = set()
    while n1 != n2:
        if n2 < n1: # sort n1 < n2
            n1, n2 = n2, n1
        if (n1, n2) in infs or (n1, n2) in visited:
            infs += visited
            return True
        visited.add((n1,n2))
        n1, n2 = n1*2, n2 - n1
    return False

def find_augmented(vs, nbs, edges, pairs): # sets
    forest = {}
    F_dict = {}
    F_depth = {}
    even_depths = set()
    odd_depths = set()
    unmarked_edges = edges - pairs
    unmarked_vs = set([v for v in vs])
    unmarked_F_vs = set()
    exposed = vs - set([pair[0] for pair in pairs] + [pair[1] for pair in pairs])
    for v in exposed:
        subtree = {}
        forest[v] = subtree #.append(subtree)
        F_dict[v] = subtree
        F_depth[v] = 0
        unmarked_F_vs.add(v)
    next_vs = even_depths.intersection(unmarked_vs)
    while next_vs:
        v = next_vs.pop()
        for w in nbs[v].intersection(unmarked_edges):
            if not w in F:
                add(v, w)
                add(w, pair(w))
            else:
                if not w in even_depths:
                    pass
                else:
                    v_root, v_to_root = [] # reverse during construction
                    w_root, w_to_root = []
                    path = path = list(reversed(v_to_root)) + [(v,w)] + w_to_root
                    if path[0] != path[-1]:
                        return path
                    else:
                        
                        Gp, Mp = contract_blossom(G,M,B)
                        Pp = find_augmented(Gp, Mp)
                        P = lift(Pp)
                        return P
        unmarked_vs.remove(v)
        next_vs = even_depths.intersection(unmarked_vs)
    return False


print(solution([1, 7, 3, 21, 13, 19]))
# print(solution(4))