# https://www.codewars.com/kata/5ea6a8502186ab001427809e/train/python

neighbors = lambda loc: {(loc[0]+di, loc[1]+dj) for di in [-1,0,1] for dj in [-1,0,1]}

def find_predecessor(goal: list[list[int]]) -> list[list[int]]:
    height, width = len(goal), len(goal[0])
    g = {(i,j) for i in range(height) for j in range(width)}
    g_alive = {loc for loc in g if goal[loc[0]][loc[1]] == 1}
    g_dead = {loc for loc in g if goal[loc[0]][loc[1]] == 0}
    w_unknown = {(i,j) for i in range(-1,height+1) for j in range(-1,width+1)}
    w_alive = set()
    w_dead = set()
#     checked = set()
    marked_stack = []

    if is_feasible():
        return [1 if (i,j) in w_alive else 0 for i in range(-1,height+1) for j in range(-1,width+1)]

def is_feasible():
#     while level loc_in  level=0  skip ahead squares iterator
    w_loc = get_next_unknown()
    if w_loc is None: return True
    save = get_save()
    if mark_alive(w_loc) and is_feasible(): return True
    reset(save)
    if mark_dead(w_loc) and is_feasible(): return True
    reset(save)
    return False

def get_next_unknown():
    for loc in squares_iterator(height, width):
        if loc in w_unknown:
            return loc
def squares_iterator():#(height, width):
    for k in range(max(height, width)):
        if k < width:
            for i in range(min(k, height)):
                yield (i,k)
        if k < height:
            for j in range(min(k, width),-1,-1):
                yield (k,j)
#             sqrt()

def get_save():
    return len(marked_stack)

def reset(save):
    for _ in range(len(marked_stack)-save):
        loc = marked_stack.pop()
        w_alive.remove(loc)
        w_dead.remove(loc)
        w_unknown.add(loc)
#     marked stack level
#     checked


# order by number of degrees of freedom? weird when dual edged
def check_and_propagate(g_locs):
    queue = set()
    for g_loc in g_locs:
#         if g_loc in checked: continue

        if g_loc in w_alive:
            min_l, max_l = 2, 3
        elif g_lov in w_dead:
            min_l, max_l = 3, 3
        else:
            print("checking unknown")
            # what if its in w_unknown?
        ns = neighbors(g_loc)
        ns_unknown = ns & w_unknown
        ns_alive   = ns & w_alive
        n_live = len(ns_alive)
        n_left = len(ns_unknown)
        if g_loc in g_alive:
            if n_live > max_l or n_live + n_left < min_l:
                return False
            else:
#                 checked.add(g_loc)
                if n_live == max_l:
                    w_set(ns_unknown, to_alive=False)
                elif n_live+n_left == min_l:
                    w_set(ns_unknown, to_alive=True)
#             else:
#                 queue.update(ns_unknown)
        elif g_loc in g_dead:
            if n_live >= min_l and n_live + n_left <= max_l:
                return False
            else:
#                 checked.add(g_loc)
                if n_live >= min_l and n_live + n_left == max_l+1:
                    w_set(ns_unknown, to_alive=True)
                elif n_live == min_l-1 and n_live + n_left <= max_l:
                    w_set(ns_unknown, to_alive=False)
#             else:
#                 queue.update(ns_unknown)
#     return queue

def w_set(w_locs, to_alive):
    assert w_locs.issubset(w_unknown)
    w_unknown -= w_locs
    if to_alive:
        w_alive += w_locs
    else:
        w_dead += w_locs
    marked_stack.extend(w_locs)
    to_check = g & neighbors(w_locs) # union
#     checked -= to_check
    check_and_propagate(to_check)

# def w_set_one(w_loc, to_alive):
#     assert w_loc in w_unknown
#     w_unknown.remove(w_loc)
#     if to_alive:
#         w_alive.add(w_locs)
#     else:
#         w_dead.add(w_locs)
#     checked -= neighbors(w_loc) 
    


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
