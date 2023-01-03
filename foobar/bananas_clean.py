from collections import defaultdict
import fractions
import copy

# Does gambling continue infinitely for given pair
def infinite(n1, n2):
    d = fractions.gcd(n1, n2)
    n1, n2 = int(n1/d), int(n2/d)
    n = n1 + n2
    is_2pow = (n & (n-1)) == 0
    return not is_2pow

# Forest has "meta" root, which is the parent of all tree roots (for easing computation)
meta_root = -1
def ancestors(v, roots):
    head = v
    v_to_root = []
    while head != meta_root:
        v_to_root.append(head)
        head = roots[head]
    return v_to_root

# Lift edge in trimmed graph to v,[v1,v2,v3,v4,..],u in original nodes
def lift_edge(v, u, nbs, roots):
    for nbr in nbs[u]: # could optimize to store blossom membership ahead of time
        blossom_path = []
        head = nbr
        while head != meta_root:
            if head == v:
                return list(reversed(blossom_path))
            blossom_path.append(head)
            head = roots[head]

# Blossom algorithm
def find_augmented(vs, edges, pairs):
    vs = set(vs)
    edges = set(edges)
    nbs = defaultdict(set)
    for e in edges:
        nbs[e[0]].add(e[1])
        nbs[e[1]].add(e[0])
    pair = dict()
    for e in pairs:
        pair[e[0]] = e[1]
        pair[e[1]] = e[0]
    nbs_copy = copy.deepcopy(nbs)

    blossoms = dict()
    exposed = vs - set([pair[0] for pair in pairs] + [pair[1] for pair in pairs])
    roots = {v: meta_root for v in exposed}
    F = copy.copy(exposed)
    even_depths = copy.copy(exposed)
    next_vs = copy.copy(exposed)

    while next_vs:
        v = next_vs.pop() # breadth typically better than depth
        next_ws = copy.copy(nbs[v])
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
                        path = list(reversed(v_to_root)) + w_to_root
                        for i in reversed(range(len(path)-1)):
                            if path[i] in blossoms:
                                path = path[:i+1] + lift_edge(path[i],path[i+1],nbs_copy,roots) + path[i+1:]
                        return path
                    else:
                        root_to_v = list(reversed(v_to_root))
                        root_to_w = list(reversed(w_to_root))
                        for i in range(min(len(root_to_v),len(root_to_w))):
                            if root_to_v[i] != root_to_w[i]:
                                i -= 1
                                break
                        cycle = root_to_v[i:] + w_to_root[:-i-1] # doesn't double-count root
                        newV = root_to_v[i] # youngest common ancestor
                        blossoms[newV] = cycle # mostly for debugging
                        # Update data structure to collapse blossom
                        F = F.difference(cycle[1:])
                        even_depths = even_depths.difference(cycle[1:])
                        for v1 in roots:
                            if not v1 in cycle and roots[v1] in cycle:
                                roots[v1] = newV
                            # keep predecessor data of collapsed nodes, used for lifting path later
                        if w in next_vs:
                            next_vs.remove(w)
                            next_ws |= nbs[w]
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
                        next_ws = next_ws.difference(cycle)
                        v = newV
    return False

def solution(banana_list):
    # Build graph
    n = len(banana_list)
    vs = list(range(n))
    edges = [(i,j) for i in range(n) for j in range(i+1, n) if infinite(banana_list[i], banana_list[j])]

    # Greedy matching
    pairs = set()
    candidates = edges[:]#[e for e in edges]
    while candidates:
        pair = candidates.pop()
        pairs.add(pair)
        candidates = [e for e in candidates if not (e[0] in pair or e[1] in pair)]

    while True:
        path = find_augmented(vs, edges, pairs)
        if not path: # maximum matching
            return len(vs) - len(pairs)*2
        for i in range(len(path)-1): # augment along path
            edge = (path[i], path[i+1]) if path[i] < path[i+1] else (path[i+1], path[i])
            if i % 2 == 0:
                pairs.add(edge)
            else:
                pairs.remove(edge)

print(solution([1, 7, 3, 21, 13, 19]))
print(solution([1,1]))