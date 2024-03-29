# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/pythonfrom preloaded import open
from preloaded import open
# import copy
import bisect

def solve_mine(map, n):
    m = Map(map, num_mines=n, debug=False)
    while (q := m.get_next()) is not None:
#         m.get_next_exhaustive()
#         print(q)
#         print(m)
        num = open(q[0], q[1])
        m.mark_opened(q, num)
    m.expand_forced()
    s = str(m)
    if '?' not in s:
        return s
    print(s)
    return '?'    

class Map:
    def __init__(self, map, num_mines, debug=False):
        self.map = [[c for c in r.split(' ')] for r in map.split('\n')]
        self.h, self.w = len(self.map), len(self.map[0])
        self.unsearched_qs = set(self.get_border_qs())
        self.marked_stack = []
        self.empties, self.bombs = [], []
#         self.num_marked_bomb = 0#sum([1 for r in map for c in r if c =='x'])
        self.num_mines = num_mines
        self.num_unmarked = map.count('?')
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
        self.empties.append((q, self.save_level()))
    
    def mark_bomb(self, q):
        if self.map[q[0]][q[1]] != '?':
            print("\n\n--------BAD BOMB--------\n\n")
            1/0
        if self.debug:
            print("marking bomb", q)
            print(self)
        self.map[q[0]][q[1]] = 'x'
        self.marked_stack.append(q)
        self.bombs.append((q, self.save_level()))

    def mark(self, q, is_bomb):
        if self.map[q[0]][q[1]] != '?':
            print("\n\n--------BAD mark--------\n\n")
            print(q, is_bomb, self.marked_stack)
            print(self)
            1/0
        val = 'x' if is_bomb else 'o'
        if self.debug:
            print("marking", q, val)
            print(self)
        self.map[q[0]][q[1]] = val
        self.marked_stack.append(q)
        if not is_bomb:
            self.empties.append((q, self.save_level()))
        else:
            self.bombs.append((q, self.save_level()))

    def unmark(self, level):
#         self.empties = bisect.bisect_right()
        while len(self.marked_stack) > level:
            q = self.marked_stack.pop()
#             if v == 'o':
#                 self.empties.remove
#             for i in range()
            self.map[q[0]][q[1]] = '?'
        self.empties = [(q,l) for q,l in self.empties if l <= level]
        self.bombs = [(q,l) for q,l in self.bombs if l <= level]
            
#         qs = self.marked_stack[level:]

    def save_level(self):
        return len(self.marked_stack)

    def feasible(self): # leaves map in example feasible state, or return False and reset
        level = self.save_level()
        q = self.get_border_q()
        if q is None:
            if self.debug:
                print("NONE", q)
                print(self)
            return self.check_filled()
            
        if self.map[q[0]][q[1]] != '?': [print("Checking non ?", q), 1/0]

        self.mark_bomb(q)
        if self.propagate(q) and self.feasible(): return True
        self.unmark(level)

        self.mark_empty(q)
        if self.propagate(q) and self.feasible(): return True
        self.unmark(level) # maybe skip?

        return False

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

    def propagate_queue(self, q, queue): # mutate map. Return False if invalid
        next_qs = set()
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
                next_qs.update(n_qs)
            else:
                queue.update(n_qs)

        return all(self.propagate_queue(next_q, queue) for next_q in next_qs)

    def feasible_queue(self, queue): # leaves map in example feasible state, or return False and reset
        if not queue:
            if self.debug:
                print("NONE")
                print(self)
            return self.check_filled()
        level = self.save_level()
        for q in queue:
            if self.map[q[0]][q[1]] != '?': continue #[print("Checking non ?", q), 1/0]
            
            self.mark_bomb(q)
            if self.propagate_queue(q, next_queue:=set()) and self.feasible_queue(next_queue): continue
            self.unmark(level)

            self.mark_empty(q)
            if self.propagate_queue(q, next_queue:=set()) and self.feasible_queue(next_queue): continue
            self.unmark(level) # maybe skip?
            return False

        return True

    def check_filled(self):
        mines_left = self.num_mines - len(self.bombs)
        unmarked_left = self.num_unmarked - len(self.marked_stack)
#         print(mines_left, unmarked_left)
        return 0 <= mines_left <= unmarked_left
    
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

    def get_q(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j] == '?':
                    return (i, j)

    def get_qs(self):
        return [(i, j) for i in range(self.h) for j in range(self.w) if self.map[i][j] == '?']

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
#         print("marked open", loc, num, "was", self.map[loc[0]][loc[1]])
        self.map[loc[0]][loc[1]] = str(num)
        self.unsearched_qs.update(self.find_affected_qs(loc))

    def __str__(self):
        return '\n'.join(' '.join(r) for r in self.map)
    
    
    

    def expand_forced(self):
#         level = self.save_level()
        for q in self.get_border_qs():
            self.propagate(q)

    def find_affected_qs(self, n):
        seen_ns, seen_qs = set(), set()
        ns = [n]
        while ns:
            qs = set()
            for n in ns:
                for q in self.qs_near(n):
                    if q in seen_qs: continue
                    if self.map[q[0]][q[1]] != '?': continue
                    seen_qs.add(q)
                    qs.add(q)
            ns = set()
            for q in qs:
                for n in self.ns_near(q):
                    if n in seen_ns: continue
                    seen_ns.add(n)
                    ns.add(n)
        return seen_qs
            
            
    def get_next(self):
        if self.empties:
            q, level = self.empties.pop()
            return q
        qs = self.unsearched_qs
        forced = set()
        seen_as_bomb, seen_as_empty = set(), set()
        seen = {True: set(), False: set()}
        level = self.save_level()
        for q in qs:
            for is_bomb in [True, False]:
                if q in forced: continue
                if q not in seen[is_bomb]:
                    self.mark(q, is_bomb)
    #                 propagate, get neighbors. feasible, get neighbors
                    if self.propagate_queue(q, queue:=set()) and self.feasible_queue(queue):
                        for Q in self.marked_stack[level:]:
                            seen[self.map[Q[0]][Q[1]] == 'x'].add(Q)
                        self.unmark(level)
                    else:
                        self.unmark(level)
                        self.mark(q, not is_bomb)
                        self.propagate(q)
                        for Q in self.marked_stack[level:]:
#                             seen[self.map[Q[0]][Q[1]] == 'x'].add(Q)
                            forced.add(Q)
                        level = self.save_level()
        self.unsearched_qs = set()
        if self.empties:
            q, level = self.empties.pop()
            return q
        
        return self.get_next_exhaustive()

    def feasible_exhaustive(self): # leaves map in example feasible state, or return False and reset
        if not self.check_filled(): return False
        level = self.save_level()
        q = self.get_q()
        if q is None:
            if self.debug:
                print("NONE", q)
                print(self)
            return True
        
            
        if self.map[q[0]][q[1]] != '?': [print("Checking non ?", q), 1/0]

        self.mark_bomb(q)
        if self.propagate(q) and self.feasible_exhaustive(): return True
        self.unmark(level)

        self.mark_empty(q)
        if self.propagate(q) and self.feasible_exhaustive(): return True
        self.unmark(level) # maybe skip?

        return False
    
    def get_next_exhaustive(self):
        if self.empties:
            q, level = self.empties.pop()
            return q
        print("get exhaustive")
        print(self)
        qs = self.get_qs()
        forced = set()
        seen_as_bomb, seen_as_empty = set(), set()
        seen = {True: set(), False: set()}
        level = self.save_level()
        for q in qs:
            for is_bomb in [True, False]:
                if q in forced: continue
                if q not in seen[is_bomb]:
                    self.mark(q, is_bomb)
    #                 propagate, get neighbors. feasible, get neighbors
                    if self.propagate(q) and self.feasible_exhaustive():
                        for Q in self.marked_stack[level:]:
                            seen[self.map[Q[0]][Q[1]] == 'x'].add(Q)
                        self.unmark(level)
                    else:
                        self.unmark(level)
                        self.mark(q, not is_bomb)
                        self.propagate(q)
                        for Q in self.marked_stack[level:]:
#                             seen[self.map[Q[0]][Q[1]] == 'x'].add(Q)
                            forced.add(Q)
                        level = self.save_level()
        self.unsearched_qs = set()
        if self.empties:
            q, level = self.empties.pop()
            return q
        print("failed exhaustive search")
#         def find_empty(self):
#         level = self.save_level()
#         for i in range(self.h):
#             for j in range(self.w):
#                 q = (i, j)
#                 if self.map[i][j] == 'o': return q
#                 if self.map[i][j] == '?' and self.ns_near(q):
#                     if self.debug: print('\n\n\nTrying', q)
#                     self.mark_bomb(q)
#                     valid = self.propagate(q) and self.feasible()
#                     self.unmark(level)
#                         # don't reset
# #                     if (i,j) == (1,1): self.debug = False

# #                     print(i, j, self.ns_near((i,j)))
# #                     for n in self.ns_near((i,j)):
# #                         print(n, self.map[n[0]][n[1]])
# #                     print("empty stat", self.mark_empty((i,j)))
#                     if not valid:
#                         self.mark_empty(q)
#                         if not self.propagate(q):
#                             print("CONTRADICTION")
#                             1/0
#                         return q
#         leftover_qs = [(i,j) for i in range(self.h) for j in range(self.w) if self.map[i][j] == '?']
#         self.unsearched_qs = self.get_border_qs()
        
#         if '?' in str(self):
#             return '?'
#         return str(self)


