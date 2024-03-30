# https://www.codewars.com/kata/5ea6a8502186ab001427809e/train/python
neighbors = lambda loc: {(loc[0]+di, loc[1]+dj) for di in [-1,0,1] for dj in [-1,0,1]} - {loc}

def find_predecessor(goal: list[list[int]]) -> list[list[int]]:
    goal = {(i,j): goal[i][j] for i in range(len(goal)) for j in range(len(goal[0]))}
#     predecesor has coords -1,-1 to h+1,w+1
# gs_neighbors ws_neighbors (no need, using set intersections)
    pass

def num_alive(g_loc):
    len(neighbors(g_loc) & w_alive)
def num_unkown(g_loc):
    len(neighbors(g_loc) & w_unknown)
def g_neighbors(w_loc): return neighbors(w_loc) & g_locs


checked = set()
# order by number of degrees of freedom? weird when dual edged
def check_and_propagate(g_locs):
    queue = set()
    for g_loc in g_neighbors(w_loc) - checked:
        if g_loc in w_alive:
            min_l, max_l = 2, 3
        else:
            min_l, max_l = 3, 3
        
        ns = neighbors(g_loc)
        ns_unknown = ns & w_unknown
        ns_alive   = ns & w_alive
        n_live = len(ns_alive)
        n_left = len(ns_unknown)
        if g_loc in g_alive:
            if n_live > max_l or n_live + n_left < min_l:
                return False
            elif n_live == max_l:
                w_set(n_left to dead)
            elif n_live+n_left == min_l:
                w_set(n_left to alive)
#             else:
#                 queue.update(ns_unknown)
        elif g_loc in g_dead:
            if n_live >= min_l and n_live + n_left <= max_l:
                return False
            elif n_live >= min_l and n_live + n_left == max_l+1:
                w_set(n_left to alive)
            elif n_live == min_l-1 and n_live + n_left <= max_l:
                w_set(n_left to dead)
#             else:
#                 queue.update(ns_unknown)
#     return queue

def w_set(w_locs, to_alive):
    assert w_unknown.issuperset(w_locs)
    w_unknown.difference_update(w_locs)
    w_alive.update(w_locs)
    
    

# try open
# go forth
# try closed
# go forth

# stack 2 step rather than recursion?

# how to prune?

# find 1 feasible configuration

# from decided: allowed number of alive neighbors (2,3), (3), complement (2,3), complement (3)
# from undecided: allowed number of alive neighbors: (2,3), complement (2,3)
# dont enumerate, prune. if Alive, neighbor can be alive if num_alive < 3. 
#                                           can be dead  if num_alive + num_neighbors_left >= 2or3
#                        if Dead,  neighbor can be alive if num_alive + 1: below
#                                           can be dead  if num_alive + num_neighbors_left > 3 or num_alive < 2or3


# default to guessing existing state?



