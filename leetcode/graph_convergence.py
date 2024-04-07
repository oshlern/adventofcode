# https://www.codewars.com/kata/60d0fd89efbd700055f491c4/train/python
def converge(g, coins):
    coins = set(coins)
    if len(coins) <= 1: return 0
    r = [{c}   for c in coins] # reachable from c
    l = [set() for c in coins] # reachable from c last time
    r_new, l_new = r[:], l[:]
    for i in range(1, len(g)):
        (r, r_new), (l, l_new) = (l, l_new), (r, r_new)
        for c in range(len(coins)):
            r_new[c] = set().union(*(g[v] for v in l_new[c])) - r_new[c]
            r[c].update(r_new[c])
            if not r_new[c]: return None
            if r_new[c].intersection(*r): return i
        
        
# def converge(g, coins):
#     coins = set(coins)
#     if len(coins) <= 1: return 0
#     def neighbors(s):
#         return set().union(*(g[v] for v in s))
#     data  = [[{c}, {c}, set(), set()] for c in coins] # d: [reachable_i, new_i, reachable_i-1, new_i-1]
#     odds  = [d[2] for d in data]
#     evens = [d[0] for d in data]
#     for i in range(1,len(g),2):
#         for d in data:
#             new = neighbors(d[1]) - d[3]
#             d[2].update(new)
#             d[3] = new
#             if not new: return None
#             if new.intersection(*odds): return i
#         for d in data:
#             new = neighbors(d[3]) - d[1]
#             d[0].update(new)
#             d[1] = new
#             if not new: return None
#             if new.intersection(*evens): return i+1 


# from functools import cache
# def converge(g, coins):
#     vs = set(g.keys())
#     coins = set(coins)
# #     @cache
#     def neighbors(s):
#         return set().union(*(g[v] for v in s))
#     data = [[{c}, {c}, set(), set()] for c in coins]
#     for i in range(0,len(vs),2):
#         if vs.intersection(*[d[0] for d in data]): return i
#         for d in data:
#             new = neighbors(d[1]) - d[3]
#             if not new: return None
#             d[2].update(new)
#             d[3] = new
#         if vs.intersection(*[d[2] for d in data]): return i+1
#         for d in data:
#             new = neighbors(d[3]) - d[1]
#             if not new: return None
#             d[0].update(new)
#             d[1] = new
            

# from functools import cache
# def converge(g, coins):
#     vs = set(g.keys())
#     coins = set(coins)
# #     @cache
#     def neighbors(s):
#         return set().union(*(g[v] for v in s))
#     N = len(vs)
#     n_coins = len(coins)
# #     print("   starting", N, n_coins)
#     data = [(set(), set(), {c}, {c}) for c in coins]
#     for i in range(N):
#         ss = [d[2] for d in data]
#         if vs.intersection(*ss):
#             print("found  ", i, N, n_coins)
#             return i
#         for idx in range(n_coins):
#             l, l_frontier, s, s_frontier = data[idx]
#             new = neighbors(s_frontier) - l_frontier
#             if not new:
#                 print("none   ", i, N)
#                 return None
#             data[idx] = (s, s_frontier, l|new, new)
    
# from functools import cache
# def converge(g, coins):
#     vs = set(g.keys())
#     coins = set(coins)
#     ls = [None for c in coins]
#     ss = [{c} for c in coins]
#     N = len(g)
# #     @cache
# #     def neighbors(s):
# #         return set().union(*(g[v] for v in s))
# # min_dists
# # possible_dists = min_dist + set(d_ik + d_kj) min_dist @ min_dist)
# # loop? 
#     for i in range(N):
#         if ss[0].intersection(*ss):
#             print("found  ", i, N, len(ss))
#             return i
# #         ns = [neighbors(s) for s in ss]
# #         only consider new vertices
# #         ns = [set().union(*(g[v] for v in s)) for s in ss]
#         l_frontier, s_frontier
#         for n,l in zip(ns, ls):
#             if n == l:
#                 print("stopped", i, N)
#                 return None
#             new = n - l_frontier
#             s_frontier = new
#             s = l + new
#             l_frontier = s_frontier
#             l = s

#         ls = ss
#         ss = ns
# #         new = ns-ls
        
#     print(N)





# from functools import cache                 
# def converge(g, coins):
#     vs = set(g.keys())
#     ss = [{c} for c in set(coins)]
# #     n = len(g)//2 + 2 if len(g)<20 else len(g)//4
#     n = len(g)//2 + 2 if len(g)<20 else int(len(g)/3.7)
#     def neighbors(s):
#         return set().union(*(g[v] for v in s))
#     class Searcher:
#         def __init__(self, c):
#             self.period = None
#             self.last = None
#             self.vs = [c]

#         def next(self):
#             if self.period is None:
#                 n = neighbors(self.vs)
#                 if n == self.vs:
#                     self.period = 1
#                 elif n == self.last:
#                     self.period = 2
#                 self.last = self.vs
#                 self.vs = n
#             elif self.period == 2:
#                 self.last, self.vs = self.vs, self.last
#             return self.vs

#     Ns = [Searcher(c) for c in set(coins)]
    
#     while any(N.period is None for N in Ns):
#         if vs.intersection(*(N.next() for N in ss)):
            
#         net = [N.next() for N in ss]
        
    
# #     @cache
    
# # min_dists
# # possible_dists = min_dist + set(d_ik + d_kj) min_dist @ min_dist)
# # loop? 
#     for i in range(n):
#         if vs.intersection(*ss):
#             print(i, n, len(ss), len(set(coins)))
#             return i
        
#         ss = [neighbors(s) for s in ss]
# #         ss = [x for s in ss if (x:=neighbors(tuple(s)))!=vs]
# #         ss = [set().union(*(g[v] for v in s)) for s in ss]
# #         ss = [x for s in ss if (x:=neighbors(tuple(sorted(s))))!=vs]
# #         find possible length paths between every node
#     print(n)


# import numpy as np
# def converge(g, coins):
#     vs = list(g.keys())
#     cs = [vs.index(c) for c in set(coins)]
#     [v in cs for v in vs]
#     converged = lambda es: np.any(np.all(es[cs],axis=0))
#     A = np.array([[n in g[v] for n in vs] for v in vs])#, dtype=bool)
#     As = []
#     if len(cs) == 1: return 0
#     if converged(A): return 1
#     for i in range(len(vs).bit_length()):
#         B = A @ A
#         if converged(B):
#             break
#         As.append(A)
#         A = B
#     else:
#         return None
#     out = 2**len(As)
#     for i in range(len(As)-1,-1,-1):
#         next_A = A @ As[i]
#         if not converged(next_A):
#             A = next_A
#             out += 2**i
#     return out + 1

# from functools import cache
# def converge(g, coins):
#     vs = set(g.keys())
#     ss = [{c} for c in set(coins)]
# #     n = len(g)//2 + 2 if len(g)<20 else len(g)//4
#     n = len(g)//2 + 2 if len(g)<20 else int(len(g)/3.7)
# #     @cache
#     def neighbors(s):
#         return set().union(*(g[v] for v in s))
# # min_dists
# # possible_dists = min_dist + set(d_ik + d_kj) min_dist @ min_dist)
# # loop? 
#     for i in range(n):
#         if vs.intersection(*ss):
#             print(i, n, len(ss), len(set(coins)))
#             return i
#         ss = [neighbors(s) for s in ss]
# #         ss = [x for s in ss if (x:=neighbors(tuple(s)))!=vs]
# #         ss = [set().union(*(g[v] for v in s)) for s in ss]
# #         ss = [x for s in ss if (x:=neighbors(tuple(sorted(s))))!=vs]
# #         find possible length paths between every node
#     print(n)

    
# import numpy as np
# def converge(g, coins):
#     vs = list(g.keys())
#     cs = [vs.index(c) for c in set(coins)]
#     converged = lambda es: np.any(np.all(es[cs],axis=0))
#     A = np.array([[n in g[v] for n in vs] for v in vs])#, dtype=bool)
#     As = []
#     if len(cs) == 1: return 0
#     if converged(A): return 1
#     for i in range(len(vs).bit_length()):
#         B = A @ A
#         if converged(B):
#             break
#         As.append(A)
#         A = B
#     else:
#         return None
#     out = 2**len(As)
#     for i in range(len(As)-1,-1,-1):
#         next_A = A @ As[i]
#         if not converged(next_A):
#             A = next_A
#             out += 2**i
#     return out + 1


# import numpy as np
# def converge(g, coins):
#     vs = list(g.keys())
#     es = np.array([[n in g[v] for n in vs] for v in vs])#, dtype=bool)
#     ss = np.array([[v==c for v in vs] for c in coins])
#     n = len(g)//2 + 2#if len(g)<20 else len(g)//4

#     @cache
#     def neighbors(s):
#         return np.any(es[list(s)],axis=0)

#     for i in range(n):
#         if np.any(np.all(ss,axis=0)): return i
#         ss = [neighbors(tuple(s)) for s in ss]

# def converge(g, coins):
#     vs = list(g.keys())
#     es = [(n in g[v] for n in vs) for v in vs]
#     ss = [(v==c for v in vs) for c in coins]
#     n = len(g)//2 + 2#if len(g)<20 else len(g)//4
    
#     @cache
#     def neighbors(s):
#         return or(es[v] for v in s)
    
#     for i in range(n):
#         if any(and(ss)): return i
#         ss = [x for s in ss if (x:=neighbors(s))!=vs]