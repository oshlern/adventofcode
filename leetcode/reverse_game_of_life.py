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

def could_be_alive(w_loc): # move checks into propagate
    assert w_loc in w_unknown
    for g_loc in g_neighbors(w_loc):
        n_live = len(neighbors(g_loc) & w_alive)
        n_left = len(neighbors(g_loc) & w_unknown)
        if g_loc in w_alive:
            min_l, max_l = 2, 3
        else:
            min_l, max_l = 3, 3
        if g_loc in g_alive:
            return n_live+1         <= max_l and n_live+1+n_left-1 >= min_l
        else:
            assert g_loc in g_dead
            return n_live+1+n_left-1 > max_l or  n_live+1           < min_l
            if g_loc in w_alive:
            min_

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


