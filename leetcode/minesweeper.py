# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/python
from preloaded import open
import copy

class Frontier:
    def __init__(self):
        self.qs = []
        self.empties = {}
        self.bombs = {}
        self.ns = {} # coord to num
        self.adj_ns = {} # q coord to neighboring n coords
        self.adj_qs = {} # n coord to neighboring q coords

    def find_safe_q(self):
        save = self.get_save()
        for q in self.qs:
            status = self.mark_bomb(q)
            if status == "INVALID" or not self.feasible():
                self.reset_to_save(save)
                return q # check if empty is satisfiable?
            self.reset_to_save(save)
        return None

    def feasible(self):
        if len(self.qs) == 0:
            return all(self.ns[n] == 0 for n in self.ns)

        q = self.qs[0]

        save = self.get_save()
        status = self.mark_empty(q)
        if status != "INVALID" and self.feasible():
            self.reset_to_save(save)
            return True
        self.reset_to_save(save)

        save = self.get_save()
        status = self.mark_bomb(q)
        if status != "INVALID" and self.feasible():
            self.reset_to_save(save)
            return True
        self.reset_to_save(save) # or just unmark marked qs

        return False

    def mark_empty(self, q): # does this preserve our constraint len(adj_qs[n]) > ns[n] and ns[n] >= 0
        if q in self.empties: return "OK"
        if q in self.bombs: return "INVALID"
        self.qs.remove(q)
        self.empties.add(q)
        for n in self.adj_ns[q]:
            self.adj_qs[n].remove(q)
        for n in self.adj_ns[q]:
            if len(self.adj_qs[n]) < self.ns[n]:
                print("small list")
                return "INVALID"
            if len(self.adj_qs[n]) == self.ns[n]:
                for b in self.adj_qs[n]:
                    status = self.mark_bomb(b)
                    if status == "INVALID": return status
        return "OK"

    def mark_bomb(self, q): # mark and propagate. if invalid, break (garbled state) 
        if q in self.empties: return "INVALID"
        if q in self.bombs: return "OK"
        self.qs.remove(q)
        self.bombs.add(q)
        for n in self.adj_ns[q]:
            self.adj_qs[n].remove(q)
            self.ns[n] -= 1
        for n in self.adj_ns[q]:
            if self.ns[n] < 0:
                print("below zero")
                return "INVALID"
            if self.ns[n] == 0:
                for b in self.adj_qs[n]:
                    status = self.mark_empty(b)
                    if status == "INVALID": return status
        return "OK"

    def get_save(self):
        saved_attrs = ["qs", "empties", "bombs", "adj_qs", "ns"]# "adj_ns",
        save = {attr: copy.deepcopy(getattr(self, attr)) for attr in saved_attrs}
        return save
    
    def reset_to_save(self, save):
        for attr, val in save.items():
            setattr(self, attr, val)

        # data = adj_ns = list(self.adj_ns.items())
        # adj_qs = list(self.adj_qs.items())
        # ns = list(self.ns.items())
        # q, adj_ns = adj_ns_copy[0]
                # self.mark_bomb(b)
        
#     def try_bomb_or_empty(self, q, ):
         
#         for n in self.adj_ns[q]:
#             self.adj_qs[n].remove(q)
#         adj_ns = self.qs_adj_ns[q]
#         self.remove_bomb(q)
#         for n in adj_ns:
#             if len(self.ns_adj_qs[n]) == self.ns[n]:
#                 self.mark_bomb(b)
        
#                 , mark
#         # marked empty
#         if self.feasible(): return True
#         # marked as bomb
#         for n in adj_ns:
#             self.ns[n] -= 1
#             if self.ns[n] == 0:
#                 for q2 in self.ns_adj_qs[n]:
#                     for n2 in self.qs_adj_ns[q2]:
#                         if if len(self.ns_adj_qs[n]
#                     if len(self.qs_adj_ns[b]) == 1:

#                     self.remove_bomb(q)
#             elif len(self.adj_qs[n]) == 0:
#                 return False
#         return self.feasible()
#     def check_empty(self, q):

# # maintain that all len(adj_qs[n]) >= ns[n]
# # if at any point len(adj_qs[n]) < ns[n]: infeasible
# # Try all ns[n] size subsets of adj_qs[n] as bombs and rest empty
# # iterate subsets bomb by bomb
# order bombs sequentially
# if empty:
# check for n in adj_js[q] len(adj_qs[n]) == ns[n], mark
# if bomb:
# check for n in adj_js[q], ns[n]-=1. if ns[n] == 0. remove adj_qs[n]. propagate to preserve len > ns


#     #pruning
#     possible_bs # no neighbors of 0
#     ns
#     q = 
#     next_bs = possible_bs - {q}
#     for n in adj_ns(q, ns):
#         F[n] -= 1
#         if F[n] == 0:
#             next_bs -= adj_qs(n, next_bs)
#     x = feasible(F, next_bs):
#     for n in neighbors(q):
#         F[n] += 1
#     if 
    
                    
#             feasible
#             self.qs.remove()
#         if 
#         for n in neighbors(q, F):
#             F[n] -= 1
#         if any(F[n] < 0 for n in ns) or not feasible(F, Q):
#             feasible = False
#         for n in neighbors(q, F):
#             F[n] += 1
#         return not feasible
        
        

# def solve_mine(map, n):
#     # coding and coding...
#     open(0,1)
#     return '?'

# adjacent_question_marks
# feasible(bombs, numbers):
#     for spot in open_spots:
#         if feasible(bombs + [spot], numbers):
#             return spot
#     return False # find spot that can't be bomb

# # breadth first search?
# # separate frontiers, but combine by adjacents... probably
# # sort in order of size, maybe unmergeed before merged


# for frontier, adjs in frontiers:
#     if (b := not_bomb(f, adjs)):
#         return b
# #     any(map(not_bomb, frontiers))

# def not_bomb(frontier, adjs):
#     if len(adjs) == 0: return None
#     for spot in adjs:
#         adjs.remove(spot)
#         neighbors(spot, frontier)
#         for n in ns:
#             F[n] -= 1
#             if F[n] > 0:
#                 continue continue
#             )
#             if len(neighbors(n, adjs))
#         adjs.add(spot)

# bipartite
# is it possible to pick elements of As so that deg(n) == F[n] for n in F

# iterate in order of adjacency

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


# def get_frontiers(map):
#     return frontiers, adjacent_qs




    # def mark_empty(self, q):
    #     if q in self.empties: return "OK", []
    #     if q in self.bombs: return "INVALID", []
    #     self.qs.remove(q)
    #     self.empties.add(q)
    #     all_marked = [q]
    #     for n in self.adj_ns[q]:
    #         self.adj_qs[n].remove(q)
    #     for n in self.adj_ns[q]:
    #         if len(self.adj_qs[n]) == self.ns[n]:
    #             for b in self.adj_qs[n]:
    #                 status, marked = self.mark_bomb(b)
    #                 all_marked += marked
    #                 if status == "INVALID":
    #                     return status, all_marked
    #     return "OK", all_marked
        # not deleting adj_ns[q] for now