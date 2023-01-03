from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
# def solution(banana_list):
#     graph = []
infs = set()
def infinite(n1, n2):
    global infs
    visited = set()
    while n1 != n2:
        if n2 < n1: # sort n1 < n2
            n1, n2 = n2, n1
        # print(n1, n2)
        if (n1, n2) in infs or (n1, n2) in visited:
            # print("infinite\n")
            infs = infs.union(visited)
            return True
        visited.add((n1,n2))
        n1, n2 = n1*2, n2 - n1
    # print(n1, n2)
    # print("equal\n")
    return False

def infinite2(n1, n2):
    visited = set()
    while n1 != n2:
        if n2 < n1: # sort n1 < n2
            n1, n2 = n2, n1
        if (n1, n2) in visited:
            # print("infinite\n")
            return True
        visited.add((n1,n2)) # add only once in a while
        n1, n2 = n1*2, n2 - n1
    # print(n1, n2)
    # print("equal\n")
    return False

# diff = n2 - n1
# diff = abs(n2 - 3*n1)
# n2, n1
# n2 - n1, 2n1
# n2 - 3n1, 4n1
# n2 - 7n1, 8n1
# n2 - 15n1, 16n1
# n2 - (2^k-1)n1, 2^kn2

# (1*15 + 1)n1, n2-15n1
# (2*15 + 1)n1 - n2, 2*n2 - 2*15n1
# (4*15 + 1)n1 - 3*n2, 4*n2 - 4*15n1
# (2^k*15 + 1)n1 - (2^k - 1)n2, (2^k)n2-(2^k*15)n1


# (2^k)n2 - (2^k*15)n1, (2^k*15 + 1)n1 - (2^k - 1)n2
# (2*2^k-1)n2 - (2*2^k*15+1)n1, 2*(2^k*15 + 1)n1 - 2*(2^k - 1)n2
# (4*2^k-3)n2 - (4*2^k*15+3)n1, 4*(2^k*15 + 1)n1 - 4*(2^k - 1)n2
# (2^m*2^k-(2^m-1))n2 - (2^m*2^k*15+(2^m-1))n1, (2^m2^k*15 + 2^m)n1 - (2^m2^k - 2^m)n2
# # diff =  
# import time
# print("A")
# s = time.time()
# for i in range(100000):
#     x = [j for j in range(i)]
# print("H", time.time() - s)
# import random

meta_root = -1
def ancestors(v, roots):
    head = v
    v_to_root = []
    while head != meta_root:
        v_to_root.append(head)
        head = roots[head]
    print(v, v_to_root, roots)

    return v_to_root

def find_augmented(n, vs, edges, pairs): # sets
    G2 = nx.Graph()
    blossoms = dict()
    exposed = vs - set([pair[0] for pair in pairs] + [pair[1] for pair in pairs])
     # 0
    roots = {v: meta_root for v in exposed}
    F = {v for v in exposed}
    next_vs = {v for v in exposed}
    even_depths = {v for v in exposed}
    nbs = defaultdict(set)
    for e in edges:
        nbs[e[0]].add(e[1])
        nbs[e[1]].add(e[0])
    pair = dict()
    for e in pairs:
        pair[e[0]] = e[1]
        pair[e[1]] = e[0]
    print(pairs)
    print(roots)
    G2.add_nodes_from(list(exposed))

    while next_vs:
        v = next_vs.pop() # breadth better than depth
        for w in nbs[v]:
            if not w in F:
                x = pair[w]
                F.add(x)
                F.add(w)
                roots[w] = v
                roots[x] = w
                next_vs.add(x)
                even_depths.add(x)
                G2.add_edge(v, w)
                G2.add_edge(w, x)
                subax1 = plt.subplot(121)
                nx.draw(G, with_labels=True, font_weight='bold')
                subax2 = plt.subplot(122)
                nx.draw(G2, with_labels=True, font_weight='bold')
                # plt.waitforbuttonpress()
                plt.show()
            else:
                if not w in even_depths:
                    pass
                else:
                    v_to_root = ancestors(v, roots) 
                    w_to_root = ancestors(w, roots) 
                    if v_to_root[-1] != w_to_root[-1]:
                        path = list(reversed(v_to_root)) + w_to_root # ish
                        print("___ blossoms")
                        print(blossoms)
                        return path
                    else:
                        i = 1
                        while v_to_root[-i] == w_to_root[-i] and i < len(v_to_root) and i < len(w_to_root):
                            # print(i, v_to_root[-i], w_to_root[-i])
                            i += 1
                        common_ancestor = v_to_root[-i+1]
                        even = i % 2 == 0
                        cycle = list(reversed(v_to_root[:-i+2])) + w_to_root[:-i+2]
                        # cycle_vs = set(cycle)
                        # n = 1000
                        newV = n+1
                        blossoms[newV] = cycle
                        roots[newV] = roots[common_ancestor]
                        # for v in cycle:
                        #     roots[v] = roots[common_ancestor]
                        F = F.difference(cycle)
                        F.add(newV)
                        # next_vs = next_vs.difference(cycle)
                        if w in next_vs:
                            next_vs.remove(w)
                            next_vs.add(newV)
                        if common_ancestor in even_depths: #if i % 2 == 0:
                            even_depths.add(newV)
                        even_depths = even_depths.difference(cycle)
                        for v1 in cycle:
                            for v2 in nbs[v1]:
                                if v2 == newV:
                                    continue
                                nbs[v2].remove(v1)
                                nbs[v2].add(newV)
                            del nbs[v1]
    return False


banana_list = [1, 7, 3, 21, 13, 19]
# banana_list = [random.randint(1,int(10737418230/3)) for _ in range(4)]

n = len(banana_list)
vs = list(range(n))
# edges = [(i,j) for i in range(n) for j in range(i+1, n) if infinite(banana_list[i], banana_list[j])]
edges = []
for i in range(n):
    for j in range(i+1, n):
        # print(i,j,banana_list[i],banana_list[j])
        if infinite(banana_list[i], banana_list[j]):
            # print("+")
            edges.append((i,j))

candidates = [e for e in edges]
pairs = []
while candidates:
    pair = candidates.pop()
    pairs.append(pair)
    candidates = [e for e in candidates if not (e[0] in pair or e[1] in pair)]
print(vs)
print(edges)
print(pairs)
G = nx.Graph()
for e in edges:
    w = 3 if e in pairs else 1
    G.add_edge(*e, weight=w)
# G.add_edges_from(edges)
print("-"*10)
print(find_augmented(n, set(vs), set(edges), set(pairs)))
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
# print(edges)
# print(inf/tot, inf, tot)
# print(len(banana_list), len(edges), len(banana_list)*(len(banana_list)-1)/2)


# def find_augmented(vs, nbs, edges, pairs): # sets
#     root = -1 # 0
#     forest = {}
#     F_dict = {}
#     F_depth = {}
#     even_depths = set()
#     odd_depths = set()
#     unmarked_edges = edges - pairs
#     unmarked_vs = set([v for v in vs])
#     unmarked_F_vs = set()
#     exposed = vs - set([pair[0] for pair in pairs] + [pair[1] for pair in pairs])
#     for v in exposed:
#         subtree = {}
#         forest[v] = subtree #.append(subtree)
#         F_dict[v] = subtree
#         F_depth[v] = 0
#         unmarked_F_vs.add(v)
#     # next_vs = even_depths.intersection(unmarked_vs)
#     next_vs = exposed
#     while next_vs: 
#         v = next_vs.pop() # breadth better than depth
#         for w in nbs[v]:
#             if not w in F:
#                 x = pair(w)
#                 add(v, w)
#                 add(w, x)
#                 next_vs.add(w)
                
#             else:
#                 if not w in even_depths:
#                     pass
#                 else:
#                     # head = v
#                     # v_to_root = []
#                     # while head != root:
#                     #     v_to_root.append(head)
#                     #     head = roots[head]
#                     # head = w
#                     # root_to_w = []
#                     # while head != root:
#                     #     if head in v_to_root:
                            
#                     #     root_to_w.insert(0, head) # deque
#                     #     head = roots[head]


#                     roots[v
#                     v_root, v_to_root = [] # reverse during construction
#                     w_root, w_to_root = []
#                     path = path = list(reversed(v_to_root)) + [(v,w)] + w_to_root
#                     if path[0] != path[-1]:
#                         return path
#                     else:
                        
#                         Gp, Mp = contract_blossom(G,M,B)
#                         Pp = find_augmented(Gp, Mp)
#                         P = lift(Pp)
#                         return P
        # unmarked_vs.remove(v)
        # next_vs = even_depths.intersection(unmarked_vs)
    # return False



# print(solution([1, 7, 3, 21, 13, 19]))
# print(solution(4))