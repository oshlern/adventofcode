# https://www.codewars.com/kata/60d0fd89efbd700055f491c4/train/python
from functools import cache

def converge(g, coins):
    vs = set(g.keys())
    ss = [{c} for c in coins]
    n = len(g)#//2 + 2#if len(g)<20 else len(g)//4
    
    @cache
    def neighbors(s):
        return tuple(set().union(*(g[v] for v in s)))

    for i in range(n):
        if vs.intersection(*ss): return i
        ss = [x for s in ss if (x:=neighbors(tuple(s)))!=vs]
#         ss = [x for s in ss if (x:=neighbors(tuple(sorted(s))))!=vs]
#         find possible length paths between every node



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