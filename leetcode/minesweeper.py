# https://www.codewars.com/kata/57ff9d3b8f7dda23130015fa/train/pythonfrom preloaded import open
import copy

def solve_mine(map, n):
    map = [r.split(' ') for r in map.split('\n')]
    h,w = len(map), len(map[0])
    fs, all_qs = get_frontiers(map)
    for f in fs:
        print(".....", f.adj_qs)
    
#     print(fs)
    # coding and coding...
    q = "INIT"
    while q is not None:
        [print(' '.join(r)) for r in map]
        for f in fs:
            print(f)
            q = f.find_safe_q()
#             print("_", q)
            if q is not None:
                num = open(q[0], q[1])
                all_qs.remove(q)
                print(q, num)
                map[q[0]][q[1]] = str(num)
                adj_qs = [loc for loc in neighbors(q,h,w) if loc in all_qs]
                f.update_opened(q, num, adj_qs)
#                 print(".....", f.adj_qs)
                for i in reversed(range(len(fs))):
                    f2 = fs[i]
                    if f2 is f:
                        continue
#                     print(q, i, f2.ns, f2.has_q(q))
                    if f2.has_q(q):
                        print("before", fs, f.ns)
                        f2.update_opened(q, num, adj_qs)
                        f.merge(f2)
                        fs.remove(f2)
                        print("after", fs, f.ns)
                break
#     q = any(f.find_safe_q() for f in fs)
#         print(q)
#         num = open(q[0], q[1])
        
#         q_fs = [f for f in fs if f.has_q(q)]
    assert q != "INIT"
    print("NONE")
#     open(0,1)
    [print(' '.join(r)) for r in map]
    if q is None:
        return '?'

class Frontier:
    def __init__(self, qs, ns, adj_ns, adj_qs):
        self.qs, self.ns = qs, ns
        self.adj_ns, self.adj_qs = adj_ns, adj_qs
        self.empties = set()
        self.bombs = set()

        print(self.adj_qs)
        print(self.empties)
        print(self.bombs)
        print('/')
        for n in self.ns:
            if len(self.adj_qs[n]) == self.ns[n]:
                for q in copy.copy(self.adj_qs[n]):
                    status = self.mark_bomb(q)
#                     assert status != "INVALID"
                    if status == "INVALID":
                        print("\n\n Failed initialization bombs \n\n")
            if self.ns[n] == 0:
                for q in copy.copy(self.adj_qs[n]):
                    status = self.mark_empty(q)
#                     assert status != "INVALID"
                    if status == "INVALID":
                        print("\n\n Failed initialization bombs \n\n")
#         Go over everything and see if it is forced. prune by seeing if during the search a q takes both values
        
        print(self.adj_qs)
        print(self.empties)
        print(self.bombs)
        print("-\n")
    
    def merge(self, f2):
        print(("-"*100 + "\n")*2)
        if self.bombs.intersection(f2.empties) or self.empties.intersection(f2.bombs):
            print('\n\n Failed intersection \n\n')
        self.bombs.update(f2.bombs)
        self.empties.update(f2.empties)
        self.qs = [q for q in self.qs if q not in self.bombs and q not in self.empties]
        self.qs += [q for q in f2.qs if q not in self.bombs and q not in self.empties and q not in self.qs]
        for n in f2.adj_qs:
            if n in self.adj_qs and self.adj_qs[n] != f2.adj_qs[n]:
                print('\n\n Failed adj qs \n\n')
            self.adj_qs[n] = f2.adj_qs[n]
        for q in f2.adj_ns:
            self.adj_ns[q] = self.adj_ns.get(q, []) + f2.adj_ns[q]
        for n in f2.ns:
            self.ns[n] = f2.ns[n]

    def has_q(self, q):
        if q == (4,3):
            print("\n\n4,3")
            print(self.qs)
            print(self.empties)
            print(self.bombs)
        return q in self.qs or q in self.empties or q in self.bombs


    def update_opened(self, q, num, adj_qs):
        assert q not in self.bombs
        # assert q in self.empties
        # combine if q in multiple frontiers
        if q in self.empties:
            self.empties.remove(q)
        else:
            print("q not in empties")
        if q in self.qs:
            print("q in qs")
            self.qs.remove(q)
            for n in self.adj_ns[q]:
                self.adj_qs[n].remove(q)
        self.ns[q] = num
#         del self.adj_ns[q]
        self.adj_qs[q] = []
        for q2 in adj_qs:
            if q2 not in self.empties and q2 not in self.bombs:
                if q2 not in self.qs:  
                    self.qs.append(q2)
                    self.adj_ns[q2] = []
                self.adj_qs[q].append(q2)
            if q not in self.adj_ns[q2]:
                self.adj_ns[q2].append(q)
                





    # mark off 100% certain bombs?

    def find_safe_q(self): # remember None answer if not changed. changed on merge or update_opened
        if self.empties:
            return next(iter(self.empties))

        save = self.get_save()
        for q in self.qs:
            print("\n\n\n pre mark")
            print(self.adj_qs)
            print(self.ns)
            print(self.empties, self.bombs, self.qs)
            status = self.mark_bomb(q)
            print("\n\n\n post mark")
            print(self.adj_qs)
            print(self.ns)
            print(self.empties, self.bombs, self.qs)
            if status == "INVALID" or not self.feasible():
                if q == (1, 5):
                    print(self.adj_qs)
                    print(self.ns)
                    print(status)
#                     print(self.feasible(pr=True))
                self.reset_to_save(save)
                status = self.mark_empty(q)
                if status == "INVALID" or not self.feasible():
                    print("FAILED empty\n\n\n")
                    print(q)
                    print(self.qs)
                    print(self.empties)
                    print(self.bombs)
                    print("__")
                    print(self.adj_qs)
                    print(self.ns)
                    print(status)
#                     print(self.feasible(pr=True))
                    assert False
                return q
            self.reset_to_save(save)
        return None

    def feasible(self, pr=False):
        if len(self.qs) == 0:
            return all(self.ns[n] == 0 for n in self.ns)

        q = self.qs[0]       
        old_adjs = copy.deepcopy(self.adj_qs)
        save = self.get_save()
        status = self.mark_empty(q)
        if status != "INVALID" and self.feasible(pr=pr):
            if pr: print(q, "empty", status, "success")
            self.reset_to_save(save)
            return True
        self.reset_to_save(save)

        save = self.get_save()
        status = self.mark_bomb(q)
        if status != "INVALID" and self.feasible(pr=pr):
            if pr: print(q, "bomb", status, "success")
            self.reset_to_save(save)
            return True
        self.reset_to_save(save) # or just unmark marked qs

        if pr:
            print(q, "failed")
            print('\t', self.qs)          
            print('\t', self.empties, self.bombs)
            print('\t', self.ns)
            print('\t', {n: len(self.adj_qs[n]) for n in self.ns})
            print('\t', {n: self.adj_qs[n] for n in self.ns})
            print('\t', {n: old_adjs[n] for n in self.ns})
        
        return False

    def mark_empty(self, q): # does this preserve our constraint len(adj_qs[n]) > ns[n] and ns[n] >= 0
        if q in self.empties: return "OK"
        if q in self.bombs: return "INVALID"
        before = self.check()
                    
        self.qs.remove(q)
        self.empties.add(q)
        for n in self.adj_ns[q]:
            self.adj_qs[n].remove(q)
        after = self.check()
        if before != after:
            print("\n"*3 + "^^^.."*100 + "\n")
            print("q", q)
            for n in self.adj_ns[q]:
                print(q in self.adj_qs[n], self.adj_qs[n])
            print(self.adj_qs)
            print(self.qs)
        for n in self.adj_ns[q]:
            if len(self.adj_qs[n]) < self.ns[n]:
                print("small list")
                return "INVALID"
            if len(self.adj_qs[n]) == self.ns[n]:
                for b in copy.copy(self.adj_qs[n]):
                    status = self.mark_bomb(b)
                    if status == "INVALID": return status
        return "OK"

    def mark_bomb(self, q): # mark and propagate. if invalid, break (garbled state) 
        if q in self.empties: return "INVALID"
        if q in self.bombs: return "OK"
        before = self.check()
        self.qs.remove(q)
        self.bombs.add(q)
        for n in self.adj_ns[q]:
            if q not in self.adj_qs[n]:
                print('\n\n\n &&&&&--------------&&&&&')
                print(n, q)
            self.adj_qs[n].remove(q)
            self.ns[n] -= 1
        after = self.check()
        if before != after:
            print("\n"*3 + "^^^.."*100 + "\n")
            print(before, after)
            print("q", q)
            print(self.adj_ns[q])
            for n in self.adj_ns[q]:
                print(q in self.adj_qs[n], n, self.adj_qs[n])
            print(self.adj_qs)
            print(self.qs)
        for n in self.adj_ns[q]:
            if self.ns[n] < 0:
                print("below zero")
                return "INVALID"
            if self.ns[n] == 0:
                for b in copy.copy(self.adj_qs[n]):
                    status = self.mark_empty(b)
                    if status == "INVALID": return status
        return "OK"

    def get_save(self):
        saved_attrs = ["qs", "empties", "bombs", "adj_qs", "ns", "adj_ns"]
        save = {attr: copy.deepcopy(getattr(self, attr)) for attr in saved_attrs}
        return save
    
    def reset_to_save(self, save):
        for attr, val in save.items():
            setattr(self, attr, val)

    def check(self):
        for N in self.adj_qs:
            for Q in self.adj_qs[N]:
                if Q not in self.qs:
                    return "ALERT"
        return "all clear"
def get_frontiers(map):
    h, w = len(map), len(map[0])

    comps, comp_map = {}, {}
    adj_qs, ns = {}, {}
    all_qs = []
    c_id = 0
    for i in range(h):
        for j in range(w):
            loc = (i,j)
            if map[loc[0]][loc[1]] == '?':
                all_qs.append(loc)
                continue

            if loc in comp_map:
                ci = comp_map[loc]
            else:
                ci = (c_id := c_id + 1)
                comps[ci] = [loc]
                comp_map[loc] = ci
            loc_adj_qs = []
            for n in neighbors(loc, h, w):
                if map[n[0]][n[1]] == '?':
                    loc_adj_qs.append(n)
                else:
                    if n in comp_map:
                        if comp_map[n] != ci:
                            n_comp = comps.pop(comp_map[n])
                            for u in n_comp:
                                comp_map[u] = ci
                            comps[ci].extend(n_comp)
                    else:
                        comp_map[n] = ci
                        comps[ci].append(n)
            if loc_adj_qs:
                adj_qs[loc] = loc_adj_qs
                # ns[loc] = int(map[loc[0]][loc[1]])
            else:
                assert int(map[loc[0]][loc[1]]) == 0
#     print("NS__", adj_qs[(2,3)])
    fs = []
    for ci,comp in comps.items():
        c_qs = []
        c_ns = {} # coord to num
        c_adj_ns = {} # q coord to neighboring n coords
        c_adj_qs = {}
        for loc in comp:
            if loc not in adj_qs:
                continue # not on border
            c_adj_qs[loc] = adj_qs[loc]
            for q in adj_qs[loc]:
                if q not in c_adj_ns:
                    if q == (1,5):
                         print("\t_________\n"*3)
                    c_adj_ns[q] = []
                    c_qs.append(q)
                c_adj_ns[q].append(loc)
            c_ns[loc] = int(map[loc[0]][loc[1]])
        if (1,5) in c_adj_ns:
            print("\t_________\n"*3, c_adj_ns[(1,5)])
        fs.append(Frontier(c_qs, c_ns, c_adj_ns, c_adj_qs))

    return fs, all_qs

def neighbors(loc, h, w):
    ns = []
    for di in [-1,0,1]:
        ni = loc[0] + di
        if ni < 0 or ni >= h: continue
        for dj in [-1,0,1]:
            if di==0 and dj==0: continue
            nj = loc[1] + dj
            if nj < 0 or ni >= w: continue
            ns.append((ni,nj))
    return ns