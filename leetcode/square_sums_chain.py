import random

def square_sums(n):
    vs = list(range(1, n+1))
    squares = [i**2 for i in range(2, int((2*n-1)**0.5)+1)]

    def calc_neighbors(v):
        candidates = [sq - v for sq in squares]
        for i in range(len(candidates)):
            if candidates[i] >= 1:
                candidates = candidates[i:]
                break
        for i in range(len(candidates)-1, -1, -1):
            if candidates[i] <= n:
                candidates = candidates[:i+1]
                break
        return list(candidates)

    neighbors = {v: calc_neighbors(v) for v in vs}
    
    _isPath_cache = {}
    def isPath(S, v):
        if (cached := _isPath_cache.get(tuple(sorted(S)) + (v,), None)) is not None:
            return cached
        cs = S.intersection(neighbors[v])
        if len(S) == 1:
            if len(cs) == 1:
                path = (cs.pop(),v,)
                _isPath_cache[tuple(sorted(S)) + (v,)] = path
                return path
            else:
                return False
        for w in cs:
            S.remove(w)
            if (path := isPath(S,w)):
                path = path + (v,)
                _isPath_cache[tuple(sorted(S)) + (v,)] = path
                return path
            S.add(w)
        return False
    
    S = {v for v in vs}
    for v in vs:
        S.remove(v)
        if (path := isPath(S, v)):
            return list(path)
        S.add(v)
    
    return False