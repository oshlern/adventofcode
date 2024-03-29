from preloaded import open

def solve_mine(map, n):
    m = Map(map, num_mines=n, debug=False)
    while (q := m.get_next()) is not None:
        m.mark_opened(q, open(q[0], q[1]))
    return '?' if '?' in (s:=str(m)) else s

class Map:
    def __init__(self, map, num_mines, debug=False):
        self.debug = debug
        self.map = [[c for c in r.split(' ')] for r in map.split('\n')]
        self.h, self.w = len(self.map), len(self.map[0])
        self.marked_stack, self.empties, self.bombs = [], [], []
        self.num_mines = num_mines - map.count('x')
        self.num_unmarked = map.count('?')
        self.unsearched_qs = set(self.get_border_qs())

    def get_next(self):
        if not self.empties: # search unsearched area
            self.search_forced(exhaustive=False)
        if not self.empties: # search all borders together
            self.unsearched_qs = self.get_border_qs()
            self.search_forced(exhaustive=True)
        if not self.empties: # search ? beyond border against all borders
            if (q := self.get_nonborder_q()): # symmetric problem, 1 sample is enough
                self.unsearched_qs = [q]
                self.search_forced(exhaustive=True)
                match self.map[q[0]][q[1]]:
                    case '?':
                        pass
                    case 'o':
                        for q2 in self.get_nonborder_qs():
                            self.mark_empty(q2)
                    case 'x':
                        for q2 in self.get_nonborder_qs():
                            self.mark_bomb(q2)
            
        if self.empties:
            q = self.empties.pop()[0]
            self.map[q[0]][q[1]] = 'C'
            return q

    def search_forced(self, exhaustive):
        forced, seen = set(), {True: set(), False: set()}
        level = self.save_level()
        for q in self.unsearched_qs:
            for is_bomb in [True, False]:
                if q in forced: continue
                if q not in seen[is_bomb]:
                    self.mark(q, is_bomb)
                    if self.propagate(q, queue:=set()) and self.feasible(queue, exhaustive):
                        for Q in self.marked_stack[level:]:
                            seen[self.map[Q[0]][Q[1]] == 'x'].add(Q)
                        self.unmark(level)
                    else:
                        self.unmark(level)
                        self.mark(q, not is_bomb)
                        assert self.propagate(q)
                        for Q in self.marked_stack[level:]:
                            forced.add(Q)
                        level = self.save_level()
        self.unsearched_qs = set()

    def propagate(self, q, queue=None): # mutate map. Return False if invalid
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
            elif queue is not None:
                queue.update(n_qs)

        return all(self.propagate(next_q, queue) for next_q in next_qs)

    def feasible(self, queue, exhaustive): # leaves map in example feasible state, or return False and reset
        if not self.check_mines(): return False
        if not queue and exhaustive and (q:=self.get_border_q()):
            queue = [q]    

        level = self.save_level()
        for q in queue:
            if self.map[q[0]][q[1]] != '?': continue
            
            self.mark_bomb(q)
            if self.propagate(q, next_queue:=set()) and self.feasible(next_queue, exhaustive): continue
            self.unmark(level)

            self.mark_empty(q)
            if self.propagate(q, next_queue:=set()) and self.feasible(next_queue, exhaustive): continue
            self.unmark(level)
            return False

        return True

    def check_mines(self):
        mines_left = self.num_mines - len(self.bombs)
        unmarked_left = self.num_unmarked - len(self.marked_stack)
        return 0 <= mines_left <= unmarked_left
    

    def mark_empty(self, q): self.mark(q, is_bomb=False)

    def mark_bomb(self, q):  self.mark(q, is_bomb=True)

    def mark(self, q, is_bomb):
        assert self.map[q[0]][q[1]] == '?'
        if self.debug: print("marking", q, "is_bomb", is_bomb, '\n', self)
        self.marked_stack.append(q)
        if is_bomb:
            self.map[q[0]][q[1]] = 'x'
            self.bombs.append((q, self.save_level()))
        else:
            self.map[q[0]][q[1]] = 'o'
            self.empties.append((q, self.save_level()))

    def unmark(self, level):
#         self.empties = bisect.bisect_right()
        while len(self.marked_stack) > level:
            q = self.marked_stack.pop()
            self.map[q[0]][q[1]] = '?'
        self.empties = [(q,l) for q,l in self.empties if l <= level]
        self.bombs = [(q,l) for q,l in self.bombs if l <= level]
#         qs = self.marked_stack[level:]

    def save_level(self):
        return len(self.marked_stack)

    def mark_opened(self, loc, num):
        assert self.map[loc[0]][loc[1]] == 'C' 
        self.map[loc[0]][loc[1]] = str(num)
        self.unsearched_qs.update(self.find_affected_qs(loc))

    def find_affected_qs(self, n):
        seen_ns, seen_qs = set(), set()
        ns = {n}
        while ns:
            qs = set()
            for n in ns:
                for q in self.qs_near(n):
                    if q not in seen_qs:
                        seen_qs.add(q)
                        qs.add(q)
            ns = set()
            for q in qs:
                for n in self.ns_near(q):
                    if n not in seen_ns:
                        seen_ns.add(n)
                        ns.add(n)
        return seen_qs

    def ns_near(self, q):
        return [n for n in self.neighbors(q) if self.map[n[0]][n[1]].isdigit()]

    def qs_near(self, n):
        return [q for q in self.neighbors(n) if self.map[q[0]][q[1]] == '?']

    def num_bombs_near(self, n):
        return len([q for q in self.neighbors(n) if self.map[q[0]][q[1]] == 'x'])

    def get_qs(self):
        for i in range(self.h):
            for j in range(self.w):
                if self.map[i][j] == '?':
                    yield (i, j)

    def get_border_qs(self):
        for q in self.get_qs():
            if self.ns_near(q):
                yield q

    def get_nonborder_qs(self):
        for q in self.get_qs():
            if not self.ns_near(q):
                yield q

    def get_q(self):           return next(self.get_qs(), None)
    def get_border_q(self):    return next(self.get_border_qs(), None)
    def get_nonborder_q(self): return next(self.get_nonborder_qs(), None)

    def neighbors(self, loc):
        nis = [loc[0] + d for d in [-1,0,1] if 0 <= loc[0] + d < self.h]
        njs = [loc[1] + d for d in [-1,0,1] if 0 <= loc[1] + d < self.w]
        ns = [(ni, nj) for ni in nis for nj in njs if not (ni==loc[0] and nj==loc[1])]
        return ns

    def __str__(self):
        return '\n'.join(' '.join(r) for r in self.map)