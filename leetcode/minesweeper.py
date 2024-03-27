# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/python
from preloaded import open


class Frontier:
    def __init__(self):
        self.ns = {} # coord to num
        self.qs = {} # coord to neighboring n coords

    def mark_bomb(self, q, ns):
        self.qs.pop(q)
        for n in ns:
            self.ns[v] -= 1
    
    def unmark_bomb(self, q, ns):
        self.qs[q] = ns
        for n in ns:
            self.ns[n] += 1

    def mark_empty(self, q, ns):
        self.qs.pop(q)
    
    def unmark_empty(self, q, ns):
        self.qs[q] = ns
        
    def feasible(self):
        for 
        for q,ns in list(self.qs.items()):
            self.mark_empty(q, ns)
            feasible = self.feasible()
            self.unmark_empty(q, ns)
            if feasible: return True
            self.mark_bomb(q, ns)
            feasible = self.feasible():
            self.unmark_bomb(q, ns)
            if feasible: return True
        return False
    
    #pruning
    possible_bs # no neighbors of 0
    ns
    q = 
    next_bs = possible_bs - {q}
    for n in adj_ns(q, ns):
        F[n] -= 1
        if F[n] == 0:
            next_bs -= adj_qs(n, next_bs)
    x = feasible(F, next_bs):
    for n in neighbors(q):
        F[n] += 1
    if 
    
                    
            feasible
            self.qs.remove()
        if 
        for n in neighbors(q, F):
            F[n] -= 1
        if any(F[n] < 0 for n in ns) or not feasible(F, Q):
            feasible = False
        for n in neighbors(q, F):
            F[n] += 1
        return not feasible
        
        

def solve_mine(map, n):
    # coding and coding...
    open(0,1)
    return '?'

adjacent_question_marks
feasible(bombs, numbers):
    for spot in open_spots:
        if feasible(bombs + [spot], numbers):
            return spot
    return False # find spot that can't be bomb

# breadth first search?
# separate frontiers, but combine by adjacents... probably
# sort in order of size, maybe unmergeed before merged


for frontier, adjs in frontiers:
    if (b := not_bomb(f, adjs)):
        return b
#     any(map(not_bomb, frontiers))

def not_bomb(frontier, adjs):
    if len(adjs) == 0: return None
    for spot in adjs:
        adjs.remove(spot)
        neighbors(spot, frontier)
        for n in ns:
            F[n] -= 1
            if F[n] > 0:
                continue continue
            )
            if len(neighbors(n, adjs))
        adjs.add(spot)

bipartite
is it possible to pick elements of As so that deg(n) == F[n] for n in F

iterate in order of adjacency

def cant_be_bomb(F, Qs, q);
    feasible = True
    for n in neighbors(q, F):
        F[n] -= 1
    if any(F[n] < 0 for n in ns) or not feasible(F, Q):
        feasible = False
    for n in neighbors(q, F):
        F[n] += 1
    return not feasible
    
    
    
if a bomb, is the rest feasible?
if yes:
    skip
if no:
    return n

def feasible(F, Qs);
    if not Qs: return all(v==0 for k,v in F)

    feasible = True
    q = Qs.pop()
    if not feasible(F, Qs): # no bomb
        for n in neighbors(q, F):
            F[n] -= 1
        if any(F[n] < 0 for n in ns) or not feasible(F, Q):
            feasible = False
        for n in neighbors(q, F):
            F[n] += 1
    Qs.add(q)
    return feasible

not feasible(F, Q) or any(F[n] < 0) or 
        feasible(F, Q):
            feasible = False
if feasible(F, Q)

# def assign(q, is_bomb, F, Q)
if a is a bomb, is the rest feasible?
if a is not a bomb, is the rest feasible?

 111
 2x21
ox x
1110


def get_frontiers(map):
    return frontiers, adjacent_qs