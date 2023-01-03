from collections import defaultdict
import math
# def solution(banana_list):
#     graph = []
def infinite(n1, n2):
    d = math.gcd(n1, n2)
    n1, n2 = int(n1/d), int(n2/d)
    n = n1 + n2
    is_2pow = (n & (n-1)) == 0
    return not is_2pow

meta_root = -1
def ancestors(v, roots):
    head = v
    v_to_root = []
    while head != meta_root:
        v_to_root.append(head)
        head = roots[head]
    return v_to_root

def find_augmented(vs, edges, pairs):
    vs = set(vs)
    edges = set(edges)

    blossoms = dict()
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

    while next_vs:
        v = next_vs.pop() # breadth better than depth
        next_ws = {a for a in nbs[v]}
        while next_ws:
            w = next_ws.pop()
            if not w in F:
                x = pair[w]
                F.add(x)
                F.add(w)
                roots[w] = v
                roots[x] = w
                next_vs.add(x)
                even_depths.add(x)
            else:
                if not w in even_depths:
                    pass
                else:
                    v_to_root = ancestors(v, roots) 
                    w_to_root = ancestors(w, roots) 
                    if v_to_root[-1] != w_to_root[-1]:
                        path = list(reversed(v_to_root)) + w_to_root # ish
                        for i in reversed(range(len(path)-1)):
                            if path[i] in blossoms:
                                b_root = path[i]
                                blossom_path = []
                                for nbr in nb_copy[path[i+1]]:#ns:
                                    blossom_path = []
                                    head = nbr
                                    while head != meta_root:
                                        if head == b_root:
                                            break
                                        blossom_path.append(head)
                                        head = roots[head]
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
                        blossoms[newV] = cycle
                        for v1 in roots:
                            if not v1 in cycle and roots[v1] in cycle:
                                roots[v1] = newV
                        F = F.difference(cycle[1:])
                        if w in next_vs:
                            next_vs.remove(w)
                            # next_vs.add(newV)
                            next_ws |= nbs[w]
                        even_depths = even_depths.difference(cycle[1:])
                        # to_del = nbs[v] - next_ws
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
                        v = newV
                        # next_ws = nbs[newV].difference(cycle) - to_del
                        next_ws = next_ws.difference(cycle)
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
        # print("BORED", len(vs) - len(pairs)*2)
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
print(solution([1,1]))