# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/pythonfrom preloaded import open

from preloaded import open

def solve_mine(map, n):
    m = Map(map, debug=False)
    while (q := m.find_empty()) is not None:
#         print("map", q)
#         print(m)
        num = open(q[0], q[1])
        m.mark_opened(q, num)
    s = str(m)
    if '?' not in s:
        return s
    return '?'    

class Map:
    def __init__(self, map, debug=False):
        self.map = [[c for c in r.split(' ')] for r in map.split('\n')]
        self.h, self.w = len(self.map), len(self.map[0])
#         self.qs = []
        self.marked_stack = []
        self.debug = debug
        
    def mark_empty(self, q):
        if self.map[q[0]][q[1]] != '?':
            print("\n\n--------BAD EMPTY--------\n\n")
            print(q, self.qs)
            1/0
        if self.debug:
            print("marking empty", q)
            print(self)
        self.map[q[0]][q[1]] = 'o'
        self.marked_stack.append(q)
    
    def mark_bomb(self, q):
        if self.map[q[0]][q[1]] != '?':
            print("\n\n--------BAD BOMB--------\n\n")
            1/0
        if self.debug:
            print("marking bomb", q)
            print(self)
        self.map[q[0]][q[1]] = 'x'
        self.marked_stack.append(q)

    def unmark(self, level):
        while len(self.marked_stack) > level:
            q = self.marked_stack.pop()
            self.map[q[0]][q[1]] = '?'
#         qs = self.marked_stack[level:]

    def save_level(self):
        return len(self.marked_stack)

    def feasible(self):
    #     if ns:
    #         for n in ns:
    #             if map[n] < len(q_neighbors(n))
        level = self.save_level()
        q = self.get_border_q()
        if q is None:
            if self.debug:
                print("NONE", q)
                print(self)
            return self.check_filled()
            
        assert self.map[q[0]][q[1]] == '?'
    #     queue += neighbor_qs
        self.mark_bomb(q)
        valid = self.propagate(q) and self.feasible()
        self.unmark(level)
        if valid: return True
        self.mark_empty(q)
        valid = self.propagate(q) and self.feasible()
        self.unmark(level) # maybe skip?
        if valid: return True
        return False
        
#         if self.mark_bomb(q) and self.feasible():
#             self.unmark(level)
#             return True
#         else:
#             self.unmark(level)
#             if self.mark_empty(q) and self.feasible():
#                 self.unmark(level)
#                 return True
#             else:
#                 self.unmark(level)
#                 return False

    def propagate(self, q): # mutate map. Return False if invalid
        next_qs = set()
    #     if map[q] == 'x':
        for n in self.ns_near(q):
            leftover = int(self.map[n[0]][n[1]]) - self.num_bombs_near(n)
            n_qs = self.qs_near(n)
            if leftover < 0 or leftover > len(n_qs):
                return False
            elif leftover == 0:
                for next_q in n_qs:
                    self.mark_empty(next_q)
                next_qs.update(n_qs)
            elif leftover == len(n_qs):
                for next_q in n_qs:
                    self.mark_bomb(next_q)
                    # next_qs.add(next_q)
                next_qs.update(n_qs)
    #         else:
    #             queue += next_qs
    # optimize by collecting ns?
        return all(self.propagate(next_q) for next_q in next_qs)

    def check_filled(self):
        return True
    
    def ns_near(self, q):
        for n in self.neighbors(q):
            if n[0] >= len(self.map) or n[1] >= len(self.map[n[0]]):
                print(q, n, self.h, self.w)
        return [n for n in self.neighbors(q) if self.map[n[0]][n[1]].isdigit()]

    def qs_near(self, n):
        return [q for q in self.neighbors(n) if self.map[q[0]][q[1]] == '?']

    def num_bombs_near(self, n):
        return len([q for q in self.neighbors(n) if self.map[q[0]][q[1]] == 'x'])

    def get_border_q(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j] == '?' and self.ns_near((i,j)):
                    return (i, j)

    def get_border_qs(self):
        return [(i, j) for i in range(self.h) for j in range(self.w) if self.map[i][j] == '?' and self.ns_near((i,j))]
#         for i in range(self.h):
#             for j in range(self.w):
#                 if self.map[i][j] == '?' and self.ns_near((i,j)):
#                     qs.append((i, j))

    def neighbors(self, loc):
        ns = []
        for di in [-1,0,1]:
            ni = loc[0] + di
            if ni < 0 or ni >= self.h: continue
            for dj in [-1,0,1]:
                if di==0 and dj==0: continue
                nj = loc[1] + dj
                if nj < 0 or nj >= self.w: continue
                ns.append((ni,nj))
        return ns

    def find_empty(self):
        level = self.save_level()
        for i in range(self.h):
            for j in range(self.w):
                q = (i, j)
                if self.map[i][j] == 'o': return q
                if self.map[i][j] == '?' and self.ns_near(q):
                    if self.debug: print('\n\n\nTrying', q)
                    self.mark_bomb(q)
                    valid = self.propagate(q) and self.feasible()
                    self.unmark(level)
                        # don't reset
#                     if (i,j) == (1,1): self.debug = False

#                     print(i, j, self.ns_near((i,j)))
#                     for n in self.ns_near((i,j)):
#                         print(n, self.map[n[0]][n[1]])
#                     print("empty stat", self.mark_empty((i,j)))
                    if not valid:
                        self.mark_empty(q)
                        if not self.propagate(q):
                            print("CONTRADICTION")
                            1/0
                        return q

    def mark_opened(self, loc, num):
        print("marked open", loc, num, "was", self.map[loc[0]][loc[1]])
        self.map[loc[0]][loc[1]] = str(num)

    def __str__(self):
        return '\n'.join(' '.join(r) for r in self.map)
    