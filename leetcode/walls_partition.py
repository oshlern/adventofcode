# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python
from collections import namedtuple
Point = namedtuple("Point", "x y")

class Graph:
    def __init__(self):
        self.comps = {}
        self.es = set()
        self.n_cycles = 0

    def push_edge(self, v1, v2):
        if (e:=(v1, v2)) in self.es: return
        self.es.add(e)
        if not v1 in self.comps: self.comps[v1] = set([v1])
        if not v2 in self.comps: self.comps[v2] = set([v2])

        if (c1 := self.comps[v1]) != (c2 := self.comps[v2]):
            c1.update(c2) # merge components
            for v in c2: self.comps[v] = c1
            del c2
        else:
            self.n_cycles += 1

def has_partitions(width, height, walls):
    border = [Point(0,0), Point(width,0), Point(width,height), Point(0,height)]
    borders = list(zip(border, border[1:] + [border[0]]))
    walls = [w_trunc for w in walls if (w_trunc:=truncate(w,borders,width,height))]
    walls = sorted(set(walls + borders))

    G = Graph()
    for w in walls:
        vs = sorted(set(p for u in walls if u!=w and (p:=intersection(u,w))))
        for v1,v2 in zip(vs, vs[1:]):
            G.push_edge(v1, v2)
    return G.n_cycles >= 2

def truncate(wall, borders, width, height):
    out = [p for b in borders if (p := intersection(wall, b))] # add interesections with border
    out += [p for p in wall if 0<=p.x<=width and 0<=p.y<=height] # remove out of bounds points
    out = tuple(sorted(set(out))) 
    return out if len(out)==2 else False

def intersection(w, u): # sort
    (A,B), (C,D) = sorted([w, u])
    AB = Point(A.x - B.x, A.y - B.y)
    CD = Point(C.x - D.x, C.y - D.y)
    BD = Point(B.x - D.x, B.y - D.y)
    denom  = AB.y*CD.x - AB.x*CD.y
    numer  = AB.y*BD.x - AB.x*BD.y
    numer2 = CD.y*BD.x - CD.x*BD.y
    if denom == 0: # parallel
        if numer != 0 or numer2 != 0: return False # not colinear
        # Find where C,D fall along line AB
        magAB = AB.x*AB.x+AB.y*AB.y
        tC = ((C.x-B.x)*AB.x + (C.y-B.y)*AB.y) # (C - B) * (A-B)   /|AB|^2
        tD = ((D.x-B.x)*AB.x + (D.y-B.y)*AB.y) # (D - B) * (A-B)   /|AB|^2

        options = [] # find all endpoints within the intersection
        if 0<=tC<=magAB: options.append(C)
        if 0<=tD<=magAB: options.append(D)
        if min(tC,tD)<=0<=max(tC,tD): options.append(B)
        if min(tC,tD)<=magAB<=max(tC,tD): options.append(A)
        return min(options) if options else False # min not necessary

    t = numer / denom
    t2 = numer2 / denom
    if not (0<=t<=1 and 0<=t2<=1): return False
    p = Point(round(D.x + t*CD.x, 10), round(D.y + t*CD.y, 10))
    return p