
def find_predecessor(goal: list[list[int]]) -> list[list[int]]:
    m = Map(goal)
    if m.is_feasible():
        print("feasible")
        print(m)
        print(m.w_unknown)
        return m.export()

neighbors = lambda loc: {(loc[0]+di, loc[1]+dj) for di in [-1,0,1] for dj in [-1,0,1]}
class Map:
    def __init__(self, goal):
#         goal = [[0] + r + [0] for r in goal]
#         goal = [0]*len(goal[0]) + goal + [0]*len(goal[0])
        self.height, self.width = len(goal), len(goal[0])
        self.g = {(i,j) for i in range(self.height) for j in range(self.width)}
        self.g_alive = {loc for loc in self.g if goal[loc[0]][loc[1]] == 1}
        self.g_dead = {loc for loc in self.g if goal[loc[0]][loc[1]] == 0}
        for i in range(-1,self.height+1):
            for j in [-1,self.width]:
                self.g.add(i,j)
        self.w_unknown = {(i,j) for i in range(-1,self.height+1) for j in range(-1,self.width+1)}
        self.w_alive = set()
        self.w_dead = set()
    #     checked = set()
        self.marked_stack = []

    def is_feasible(self):
        print(self)
        print(self.w_unknown)
        print("__")
    #     while level loc_in  level=0  skip ahead squares iterator
        w_loc = self.get_next_unknown()
        if w_loc is None: return True
        save = self.get_save()
        if self.mark_alive(w_loc) and self.is_feasible(): return True
        self.reset(save)
        if self.mark_dead(w_loc) and self.is_feasible(): return True
        self.reset(save)
        return False

    def get_next_unknown(self):
        for i in range(-1, self.height+1):
            for j in range(-1, self.width+1):
                loc = (i,j)
#         for loc in self.squares_iterator():
                if loc in self.w_unknown:
                    return loc

    def squares_iterator(self):
        for k in range(max(self.height, self.width)):
            if k < self.width:
                for i in range(min(k, self.height)):
                    yield (i,k)
            if k < self.height:
                for j in range(min(k, self.width),-1,-1):
                    yield (k,j)
    #             sqrt()

    def get_save(self):
        return len(self.marked_stack)

    def reset(self, save):
#         print(len(self.w_unknown))
        for _ in range(len(self.marked_stack)-save):
            loc = self.marked_stack.pop()
            if loc in self.w_alive:
                self.w_alive.remove(loc)
            else:
                self.w_dead.remove(loc)
            self.w_unknown.add(loc)
#         print(len(self.w_unknown))
    #     marked stack level
    #     checked


    # order by number of degrees of freedom? weird when dual edged
    def check_and_propagate(self, g_locs):
        queue = set()
        for g_loc in g_locs:
    #         if g_loc in checked: continue

            if g_loc in self.w_alive:
                min_l, max_l = 2, 3
            elif g_loc in self.w_dead:
                min_l, max_l = 3, 3
            else:
                min_l, max_l = 2, 3
#                 print("checking unknown")
                # what if its in w_unknown? TODO
            ns = neighbors(g_loc)
            ns_unknown = ns & self.w_unknown
            ns_alive   = ns & self.w_alive
            n_live = len(ns_alive)
            n_left = len(ns_unknown)
            if g_loc in self.g_alive:
                if n_live > max_l or n_live + n_left < min_l:
                    return False
                else:
    #                 checked.add(g_loc)
                    if n_live == max_l:
                        if not self.w_set(ns_unknown, to_alive=False):
                            return False
                    elif n_live+n_left == min_l:
                        if not self.w_set(ns_unknown, to_alive=True):
                            return False
    #             else:
    #                 queue.update(ns_unknown)
            elif g_loc in self.g_dead:
                if n_live >= min_l and n_live + n_left <= max_l:
                    return False
                else:
    #                 checked.add(g_loc)
                    if n_live >= min_l and n_live + n_left == max_l+1:
                        if not self.w_set(ns_unknown, to_alive=True):
                            return False
                    elif n_live == min_l-1 and n_live + n_left <= max_l:
                        if not self.w_set(ns_unknown, to_alive=False):
                            return False
        return True
    #             else:
    #                 queue.update(ns_unknown)
    #     return queue
        

    def w_set(self, w_locs, to_alive):
#         assert w_locs.issubset(self.w_unknown)
        if not w_locs.issubset(self.w_unknown): 1/0
        self.w_unknown -= w_locs
        if to_alive:
            self.w_alive |= w_locs
        else:
            self.w_dead |= w_locs
        self.marked_stack.extend(w_locs)
        print(len(w_locs), len(self.w_unknown), len(self.w_alive), len(self.w_dead))
        print(w_locs)
#         print(self.marked_stack)
#         print('\n')
        ns = set()
        for w_loc in w_locs:
            ns |= neighbors(w_loc)
        to_check = self.g & ns
    #     checked -= to_check
        return self.check_and_propagate(to_check)

    def mark_alive(self, w_loc):
        return self.w_set(set([w_loc]), to_alive=True)

    def mark_dead(self, w_loc):
        return self.w_set(set([w_loc]), to_alive=False)

    def export(self):
        return [[1 if (i,j) in self.w_alive else 0 if (i,j) in self.w_dead else -8 for i in range(-1,self.height+1)] for j in range(-1,self.width+1)]

    def __str__(self):
        return '\n'.join(' '.join('X' if c==1 else '.' if c==0 else '?' for c in r) for r in self.export())