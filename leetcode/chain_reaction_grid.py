# https://www.codewars.com/kata/65c420173817127b06ff7ea7

from collections import deque

def min_bombs_needed(grid):
    grid = grid.split('\n')
    assert grid and grid[0]
    h, w = len(grid), len(grid[0])

    def out_nodes(i,j):
        assert grid[i][j] != "0"
        ns_plus = [(i-1, j  ), (i+1, j  ), (i  , j-1), (i  , j+1)]
        ns_diag = [(i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]
        ns = ns_plus if grid[i][j] == "+" else ns_diag
        ns = [(ni,nj) for ni,nj in ns if 0<=ni<h and 0<=nj<w and grid[ni][nj] != "0"]
        return ns

    def in_nodes(i,j):
        ns = [ (i-1, j  , '+'), (i+1, j  , '+'), (i  , j-1, '+'), (i  , j+1, '+'),
               (i-1, j-1, 'x'), (i-1, j+1, 'x'), (i+1, j-1, 'x'), (i+1, j+1, 'x')]
        ns = [(ni,nj) for ni,nj,c in ns if 0<=ni<h and 0<=nj<w and grid[ni][nj] == c]
        return ns

    def reachable_from(v, ignored):
        to_search = deque([v])
        reachable = set([v])
        while to_search:
            for n in out_nodes(*to_search.popleft()):
                if n in reachable or n in ignored:
                    continue
                reachable.add(n)
                to_search.append(n)
        return reachable

    def source_outside(v, reachable, ignored):
        to_search = deque([v])
        sources = set([v])
        while to_search:
            for n in in_nodes(*to_search.popleft()):
                if n in sources or n in ignored:
                    continue
                if n not in reachable:
                    return n
                sources.add(n)
                to_search.append(n)
        return False

    ignored = set()
    count = 0
    for i in range(h):
        for j in range(w):
            v = (i,j)
            if v in ignored or grid[i][j] == "0":
                continue
            while v:
                reachable = reachable_from(v, ignored) # can combine searches into 1
                v = source_outside(v, reachable, ignored)
                ignored |= reachable
            count += 1
    return count



# find directed edges
# paint by color
# if not colored:
#     paint new color

# x
# x00+0
# 0+x0
# 00+0


# reached_from
# reachable
# # spread out
# if reached_from ''


# for v in G
#     v.reached_from = union(w.reached_from for w in v.ingoing)
#     v.reachable = union(w.reachable for w in v.outgoing)
#     if v.reached_from:
#         w0 = v.reached_from[0]
# #         id = ids[w0]
#         for w in v.reachable:
#             ids[w] = w0
# #         v.reached_from = [w for w in v.reached_from if w == w0 or w not in v.reachable]
# #         v.reachable = [w0] if w0 in v.reachable else []
    
#     if not v.reached_from:
#         v.reached_from = [v_ids[i]]
# #     v.reachable = union(w.reachable for w in v.ingoing)
#     v.reached_from = union(w.reachable for w in v.ingoing)
#         v.outgoing

# +   +
# +++++
#  ++
#  ++ 
#    x++
#     x

# ->

# ++++
#   +
#  x
# x

# x x
# +x x+
#  x
#  +
# ->


# paint yellow out
# paint purple for ingoing edges

# if any w purple and not yellow, update source to be w
#     no yellows lead to w
#     delete purples
#     paint blue anything out of w (ignoring yellows)
#     paint purple anything into w (ignoring yellows)
    
# pick v
# Loop: (ignore yellows)
#     paint yellow reachable from v
#     find w that gets to v outside of yellow
#     v = w

    

    
# paint yellow reachable from v
    
    
# if out is purple, update yellow-purple source
# if any 

# paint, follow, delete edges
# next. paint, follow, delete edges. if reached w==w.source, update w.source = v # ids[w] ==


# can i do less then O(n^2), like O(n max_deg) or O(Nlog n)

# choose all without in nodes
# reduce shortest cycles to nodes
# choose all without in nodes



# directional graph
