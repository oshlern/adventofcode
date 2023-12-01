from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.drawing.nx_pydot import graphviz_layout
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
# n2 - (2^j-1)n1, 2^j*n1

# 2^jn1, n2 - (2^j-1)n1
# (2*(2^j-1)+1)n1 - n2, 2n2 - 2(2^j-1)n1
# (4*(2^j-1)+1)n1 - 3n2, 4n2 - 4(2^j-1)n1
# (2^k(2^j-1)+1)n1 - (2^k-1)n2, (2^k)n2 - 2^k(2^j-1)n1

# (2^k)n2 - 2^k(2^j-1)n1, (2^k(2^j-1)+1)n1 - (2^k-1)n2
# (2*(2^k-1)+1)n2 - (2*2^k(2^j-1)+1)n1, 2*(2^k(2^j-1)+1)n1 - 2*(2^k-1)n2
# (4*(2^k-1)+1)n2 - (4*2^k(2^j-1)+3)n1, 4*(2^k(2^j-1)+1)n1 - 2*(2^k-1)n2
# (2^m(2^k-1)+1)n2 - (2^m(2^k(2^j-1)+1)-1)n1, 2^m(2^k(2^j-1)+1)n1 - 2^m(2^k-1)n2
# (2^m2^k-2^m+1)n2 - (2^m2^k2^j-2^m2^k+2^m-1)n1, (2^m2^k2^j-2^m2^k+2^m)n1 - (2^m2^k-2^m)n2
# (2^m(2^k-1)+1)n2 = (2^m(2^k(2^j-1)+1)-1)n1
# (2^m(2^k-1)+1)n2 = (2^m(2^k(2^j-1)+1)-1)n1
# (2^k-1)+ (n2+n1)/2^m = (2^k(2^j-1)+1)n1
# (2^k-1)+ (n2+n1)/2^m = (2^k(2^j-1)+1)n1



# (2^m(2^k(2^j-1)+1)-1)
# (2^m+k+j-2^m+k+2^m-1),  (2^m+k-2^m+1)

# 16+4+1 = 21, 8+2+1=11
# 8+2+1 = 11, 4+1=5
# 4+1=5, 2+1=3

# (1*15 + 1)n1, n2-15n1
# (2*15 + 1)n1 - n2, 2*n2 - 2*15n1
# (4*15 + 1)n1 - 3*n2, 4*n2 - 4*15n1
# (2^k*15 + 1)n1 - (2^k - 1)n2, (2^k)n2-(2^k*15)n1


# (2^k)n2 - (2^k*15)n1, (2^k*15 + 1)n1 - (2^k - 1)n2
# (2*2^k-1)n2 - (2*2^k*15+1)n1, 2*(2^k*15 + 1)n1 - 2*(2^k - 1)n2
# (4*2^k-3)n2 - (4*2^k*15+3)n1, 4*(2^k*15 + 1)n1 - 4*(2^k - 1)n2
# (2^m*2^k-(2^m-1))n2 - (2^m*2^k*(2^j-1)+(2^m-1))n1, (2^m2^k*(2^j-1) + 2^m)n1 - (2^m2^k - 2^m)n2
# (2^m*2^k-(2^m-1))n2 - (2^m*2^k*(2^j-1)+(2^m-1))n1, (2^m2^k*(2^j-1) + 2^m)n1 - (2^m2^k - 2^m)n2
# (2^m*2^k-(2^m-1))n2 - (2^m*2^k*(2^j-1)+(2^m-1))n1, (2^m2^k*(2^j-1) + 2^m)n1 - (2^m2^k - 2^m)n2
# (2^m*2^k-(2^m-1))n2 - (2^m*2^k*(2^j-1)+(2^m-1))n1, (2^m2^k*(2^j-1) + 2^m)n1 - (2^m2^k - 2^m)n2


# 6, 6 #2k
# 3, 9 # over

# 12, 12
# 6, 18
# 3, 21    9, 15


# p*2^k, p*2^k
# p*2^k-1, 3p*2^k-1
# p*2^k-2, 7p*2^k-2                           5p*2^k-2, 3p*2^(k-2)
# p*2^k-3, 15p*2^k-3  9p*2^k-3, 7p*2^k-3      5p*2^k-3, 11p*2^(k-3)    5p*2^k-2, 3p*2^(k-2)


# a*2^k, b*2^k
# a+b/2 2^k
# c*2^K

# find m in gcd?
# find k power of 2 in c
# coefs of k match to a,b




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

def find_augmented(n, vs, edges, pairs, vis=False): # sets
    vs = set(vs)
    edges = set(edges)

    blossoms = dict()
#     b_membership = dict()
    exposed = vs - set([pair[0] for pair in pairs] + [pair[1] for pair in pairs])
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
        
    nb_copy = {x: {y for y in nbs[x]} for x in nbs}
    
    if vis:
        G2 = nx.Graph()
        G2.add_nodes_from(list(exposed))
    
    while next_vs:
        v = next_vs.pop() # breadth better than depth
        next_ws = {a for a in nbs[v]}
        while next_ws:
            if vis:
                subax1 = plt.subplot(121)
                pos = graphviz_layout(G2, prog="dot")
                nx.draw(G2, pos, with_labels=True, font_weight='bold',node_size=1000,font_size=28,
                        node_color='#5fa8d4',edge_color=[G2[u][v]['color'] for u,v in G2.edges()])
                subax2 = plt.subplot(122)
                colors = [G[u][v]['color'] for u,v in G.edges()]
                weights = [G[u][v]['weight'] for u,v in G.edges()]
                pos = nx.circular_layout(G)
                nx.draw(G, pos, edge_color=colors, width=weights, with_labels=True,font_weight='bold',
                        node_size=1000,font_size=28,node_color='#5fa8d4')
                plt.show()
            w = next_ws.pop()
            if not w in F:
                x = pair[w]
                F.add(x)
                F.add(w)
                roots[w] = v
                roots[x] = w
                next_vs.add(x)
                even_depths.add(x)
                if vis:
                    G2.add_edge(v, w, color="black")
                    G2.add_edge(w, x, color="blue")
            else:
                if not w in even_depths:
                    pass
                else:
                    v_to_root = ancestors(v, roots) 
                    w_to_root = ancestors(w, roots) 
                    if v_to_root[-1] != w_to_root[-1]:
                        path = list(reversed(v_to_root)) + w_to_root # ish
                        print("___ blossoms", blossoms)
                        print("PATH", path)
                        for i in reversed(range(len(path)-1)):
                            if path[i] in blossoms:
                                b_root = path[i]
                                blossom_path = []
                                for nbr in nb_copy[path[i+1]]:#ns:
                                    blossom_path = []
                                    head = nbr
                                    print(i, "Head,", head)
                                    while head != meta_root:
                                        if head == b_root:
                                            print(blossom_path)
                                            break
                                        blossom_path.append(head)
                                        head = roots[head]
                                        print(head)
                                    else:
                                        continue
                                    break
                                path = path[:i+1] + list(reversed(blossom_path)) + path[i+1:]
                        return path
                    else:
                        root_to_v = list(reversed(v_to_root))
                        root_to_w = list(reversed(w_to_root))
                        for i in range(min(len(root_to_v),len(root_to_w))):
                            if root_to_v[i] != root_to_w[i]:
                                i -= 1
                                break
                        common_ancestor = root_to_v[i]
                        cycle = root_to_v[i:] + w_to_root[:-i-1]
                        newV = common_ancestor
                        print("CYCLE", cycle)
                        blossoms[newV] = cycle
                        for v1 in roots:
                            if not v1 in cycle and roots[v1] in cycle:
                                roots[v1] = newV
                        F = F.difference(cycle[1:])
                        if w in next_vs:
                            next_vs.remove(w)
                            next_vs.add(newV)
                        even_depths = even_depths.difference(cycle[1:])
                        to_del = nbs[v] - next_ws
                        for v1 in cycle[1:]:
                            for v2 in nbs[v1]:
                                if v2 in cycle[1:]:
                                    continue
                                nbs[v2].remove(v1)
                                if v2 == newV:
                                    continue
                                nbs[v2].add(newV)
                                nbs[newV].add(v2)
                            del nbs[v1]
                        if vis:
                            for V1 in cycle[1:]:
                                G2 = nx.contracted_nodes(G2, newV, V1)
                            G2.remove_edges_from(nx.selfloop_edges(G2))
                        print(v, next_ws)
                        v = newV
                        next_ws = nbs[newV].difference(cycle) - to_del
                        print(v, next_ws)
        if vis:
            pos = graphviz_layout(G2, prog="dot")
            nx.draw(G2, pos, with_labels=True, font_weight='bold',node_size=100,font_size=28,
                node_color='#5fa8d4',edge_color=[G2[u][v]['color'] for u,v in G2.edges()])
            plt.show()
        return False

def solution(banana_list):
    n = len(banana_list)
    vs = list(range(n))
    edges = [(i,j) for i in range(n) for j in range(i+1, n) if infinite(banana_list[i], banana_list[j])]

    candidates = [e for e in edges]
    pairs = set()
    while candidates:
        pair = candidates.pop()
        pairs.add(pair)
        candidates = [e for e in candidates if not (e[0] in pair or e[1] in pair)]

    while True:
        path = find_augmented(vs, edges, pairs)
        # bored = len(vs) - len(pairs)*2
        # print("BORED", bored)
        if not path:
            return len(vs) - len(pairs)*2
        for i in range(len(path)-1):
            edge = (path[i], path[i+1])
            if edge[0] > edge[1]:
                edge = (edge[1], edge[0])
            if i % 2 == 0:
                pairs.add(edge)
            else:
                pairs.remove(edge)

print(solution([1, 7, 3, 21, 13, 19]))