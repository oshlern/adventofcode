
def find_predecessor(goal: list[list[int]]) -> list[list[int]]:
    m = Map(goal)
    if m.is_feasible():
        print("num calls", m.counter)
        return m.export()

neighbors = lambda loc: {(loc[0]+di, loc[1]+dj) for di in [-1,0,1] for dj in [-1,0,1]} - {loc}
class Map:
    def __init__(self, goal):
        goal = [[0] + r + [0] for r in goal]
        goal = [[0]*len(goal[0])] + goal + [[0]*len(goal[0])]
        self.height, self.width = len(goal), len(goal[0])
        self.g = {(i,j) for i in range(self.height) for j in range(self.width)}
        self.g_alive = {loc for loc in self.g if goal[loc[0]][loc[1]] == 1}
        self.g_dead = {loc for loc in self.g if goal[loc[0]][loc[1]] == 0}
        self.unknown = {loc for loc in self.g}
        self.alive = set()
        self.dead = set()
        self.marked_stack = []
        self.queue = list(self.squares_iterator())
        self.counter = 0

    def is_feasible(self):
        self.counter += 1
        loc = None
        popped = []
        while loc not in self.unknown:
            if not self.queue: return True
            loc = self.queue.pop()
            popped.append(loc)
#         print(self)
#         print(loc)
        save = self.get_save()
        if self.mark(loc, 1) and self.is_feasible(): return True
        self.reset(save)
        if self.mark(loc, 0) and self.is_feasible(): return True
        self.reset(save)
        self.queue.append(loc)
        
        while popped:
            self.queue.append(popped.pop())
        return False

    def get_next_unknown(self):
        for i in range(self.height):
            for j in range(-1, self.width+1):
                loc = (i,j)
#         for loc in self.squares_iterator():
                if loc in self.unknown:
                    return loc

    def squares_iterator(self):
        for k in range(max(self.height, self.width)-1,-1,-1):
            if k < self.width:
                for i in range(min(k, self.height)):
                    yield (i,k)
            if k < self.height:
                for j in range(min(k, self.width),-1,-1):
                    yield (k,j)
#                 sqrt()

    def get_save(self):
        return len(self.marked_stack)

    def reset(self, save):
#         print(len(self.unknown))
        for _ in range(len(self.marked_stack)-save):
            loc = self.marked_stack.pop()
            if loc in self.alive:
                self.alive.remove(loc)
            else:
                self.dead.remove(loc)
            self.unknown.add(loc)
#         print(len(self.unknown))
    #     marked stack level
    #     checked


    # order by number of degrees of freedom? weird when dual edged
    def check_and_propagate(self, g_locs):
        queue = set()
        for g_loc in g_locs:
    #         if g_loc in checked: continue

    
            if g_loc in self.alive:
                min_l, max_l = 2, 3
            elif g_loc in self.dead:
                min_l, max_l = 3, 3
            if g_loc in self.unknown:
#                 if g_loc in g_alive:
                min_l, max_l = 2, 3
#                 else:
#                 print("checking unknown")
                # what if its in unknown? TODO
            ns = neighbors(g_loc)
            ns_unknown = ns & self.unknown
            ns_alive   = ns & self.alive
            n_live = len(ns_alive)
            n_left = len(ns_unknown)
            if g_loc in self.g_alive:
                if n_live > max_l or n_live + n_left < min_l:
                    return False
                else:
                    if n_live == max_l:
                        if not self.mark(ns_unknown, False):
                            return False
                    elif n_live+n_left == min_l:
                        if not self.mark(ns_unknown, True):
                            return False
            elif g_loc in self.g_dead:
                if n_live >= min_l and n_live + n_left <= max_l:
                    return False
                else:
                    if n_live >= min_l and n_live + n_left == max_l+1:
                        if not self.mark(ns_unknown, True):
                            return False
                    elif n_live == min_l-1 and n_live + n_left <= max_l:
                        if not self.mark(ns_unknown, False):
                            return False
        return True
        

    def mark(self, locs, as_alive):
        if not type(locs) == set: locs = set([locs])
        if as_alive:
            self.alive |= locs
        else:
            self.dead |= locs
        self.unknown -= locs
        self.marked_stack.extend(locs)
        ns = set()
        for loc in locs:
            ns.add(loc)
            ns |= neighbors(loc)
        return self.check_and_propagate(ns & self.g)

    def export(self):
        return [[1 if (i,j) in self.alive else 0 if (i,j) in self.dead else -8 for j in range(self.width)] for i in range(self.height)]

    def __str__(self):
        return '\n'.join(' '.join('X' if c==1 else '.' if c==0 else '?' for c in r) for r in self.export())