# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python
from collections import namedtuple
Point = namedtuple("Point", "x y")

from collections import namedtuple
Point = namedtuple("Point", "x y")


class Graph:
    def __init__(self):
        self.comps = {}
        self.es = set()
        self.n_cycles = 0

    def push_edge(self, v1, v2):
        if (v1, v2) in self.es: return
        self.es.add((v1, v2))

        for v in (v1, v2):
            if not v in self.comps:
                self.comps[v] = set([v])

        
        if (c1 := self.comps[v1]) == (c2 := self.comps[v2]):
            print(v1,v2, self.comps[v1])

            self.n_cycles += 1
        else:
            c1.update(c2)
            for v in c2: self.comps[v] = c1
            del c2
            
#         print(v1,v2)
#         for v in self.comps:
#             print(v, self.comps[v])
        

def has_partitions(width, height, walls):
    borders = [
        (Point(0, 0), Point(width,0)),
        (Point(0, 0), Point(0,height)),
        (Point(width, 0), Point(width, height)),
        (Point(0, height), Point(width, height)),
    ]
    walls = [u for w in walls if (u:=truncate(w,borders,width, height))]
    walls = set(walls + borders)
    
    G = Graph()
    for w in walls:
        vs = sorted(set(p for u in walls if u!=w and (p:=intersection(u,w))))
        for i in range(1,len(vs)):
            G.push_edge(vs[i-1], vs[i])
#             if G.n_c Compress wall points to one "point" then find first cycle
    return G.n_cycles >= 2


def truncate(wall, borders, width, height):
    out = [p for b in borders if (p := intersection(wall, b))]
    out += [p for p in wall if 0<=p.x<=width and 0<=p.y<=height]
    out = tuple(sorted(set(out)))
    if len(out) != 2: return False
    return out

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
#         if A == B:
#             if C == D:
#                 return A if A == C else False
#             (A,B), (C,D), AB = (C,D), (A,B), CD
        # Find where C,D fall along line AB
        magAB = AB.x*AB.x+AB.y*AB.y
        tC = ((C.x-B.x)*AB.x + (C.y-B.y)*AB.y) # (C - B) * (A-B)   /|AB|^2
        tD = ((D.x-B.x)*AB.x + (D.y-B.y)*AB.y) # (D - B) * (A-B)   /|AB|^2

        options = [] # find all endpoints within the intersection
        if 0<=tC<=magAB: options.append(C)
        if 0<=tD<=magAB: options.append(D)
        if min(tC,tD)<=0 and magAB<=max(tC,tD): options += [A,B]
        return min(options) if options else False

    t = numer / denom
    t2 = numer2 / denom
    if not (0<=t<=1 and 0<=t2<=1): return False
    p = Point(D.x + t*CD.x, D.y + t*CD.y)
    return p


# class Graph:
#     def __init__(self):
#         self.comps = {}
#         self.es = set()
#         self.n_cycles = 0

#     def push_edge(self, v1, v2):
#         if (v1, v2) in self.es:
#             return
#         self.es.add((v1, v2))
#         for v in (v1, v2):
#             if not v in self.comps:
#                 self.comps[v] = set([v])

#         comp1, comp2 = self.comps[v1], self.comps[v2]
#         if comp1 == comp2:
#             self.n_cycles += 1
#         else:
#             comp1.update(comp2)
#             for v in comp2:
#                 self.comps[v] = comp1
#             del comp2

# # class Graph:
# #     def __init__(self):
# #         self.es = set()
# #         self.vs = {}
# #         self.components = []

# #     def push_edge(self, v0, v1):
# #         if (v0, v1) in self.es: return
# #         self.es.add((v0, v1))
# #         for v in (v0, v1):
# #             if not v in self.vs:
# #                 self.vs[v] = len(self.components)
# #                 self.components.append([v])
# # #         print(self.components, self.vs)
        
# #         if self.vs[v0] == self.vs[v1]:
# #             n_cycles += 1
# #         else:
# #             self.vs[v0].update(self.vs[v1])
# #             for 
# #         if self.vs[v0] != self.vs[v1]:
# #             self.components[self.vs[v0]] += self.components[self.vs[v1]]
# # #             print(self.components)
# #             del self.components[self.vs[v1]]
# # #             self.components = self.components[:self.vs[v1]] + self.components[self.vs[v1]+1:]
# #             for v in self.components[self.vs[v0]]:
# #                 self.vs[v] = self.vs[v0]
# # #             del self.components[self.vs[v1]]
# #         print(v0, v1, self.components)
# # #         print(self.vs)
    
# #     def n_cycles(self):
# #         E = len(self.es)
# #         V = sum(map(len, self.components))
# #         n_comp = len(self.components)
# #         return E - V + n_comp
        

# def has_partitions(width, height, walls):
#     borders = [
#         (Point(0, 0), Point(width,0)),
#         (Point(0, 0), Point(0,height)),
#         (Point(width, 0), Point(width, height)),
#         (Point(0, height), Point(width, height)),
#     ]
#     walls = [u for w in walls if (u:=truncate(w,borders,width, height))]
#     walls = set(walls + borders)
    
#     G = Graph()
#     for w in walls:
#         vs = sorted(set(p for u in walls if u!=w and (p:=intersection(u,w))))
#         for i in range(len(vs)):
# #             Vs.add(vs[i]) # compare equality with precision? turn into id? sort vs?
#             if i > 0:
# #                 Es.add((vs[i-1], vs[i]))
# #                 print(vs[i-1], vs[i])
#                 G.push_edge(vs[i-1], vs[i])
# #     for v in Vs:
# #         print(v)
# #     for e in Es:
# #         print(e)
# #     print("^^")
# #     for c in G.components:
# #         print(c)
# #     print(G.n_cycles)
#     return G.n_cycles >= 2


# def truncate(wall, borders, width, height):
#     out = [p for b in borders if (p := intersection(wall, b))]
# #     for b in borders:
# #         if intersection(wall, b):
# #             print("____")
# #             print(wall, b)
# #             print(intersection(wall, b))
# #             print("____")

# #     print("truncating", out, wall)
#     out += [p for p in wall if 0<p.x<width and 0<p.y<height]
#     if len(out) != 2: return False
#     return tuple(out)

# def within(p, w, h):
#     return 0<=p.x<=w and 0<=p.y<=h

# def intersection(w, u): # sort
#     w, u = sorted([w, u])
#     A, B = w
#     C, D = u
#     AB = Point(A.x - B.x, A.y - B.y)
#     CD = Point(C.x - D.x, C.y - D.y)
#     BD = Point(B.x - D.x, B.y - D.y)
#     denom  = AB.y*CD.x - AB.x*CD.y
#     numer  = AB.y*BD.x - AB.x*BD.y
#     numer2 = CD.y*BD.x - CD.x*BD.y
#     if denom == 0:
#         if numer == 0:
# #             print("INTERSECTING colinear", w, u)
#             mag = AB.x*AB.x+AB.y*AB.y
#             tC = ((C.x-B.x)*AB.x + (C.y-B.y)*AB.y) # (C - A) * AB   /|AB|^2
#             tD = ((D.x-B.x)*AB.x + (D.y-B.y)*AB.y) # (D - A) * AB   /|AB|^2
# #             print(tC, tD, C)
#             if 0<=tC<=mag: return C
#             if 0<=tD<=mag: return D
#             if min(tC,tD)<=0<=max(tC,tD): return B
#         return False
#     t = numer / denom
#     t2 = numer2 / denom
# #     t = (q − p) × s / (r × s)
# #     print("doing", w,u,t)
#     if 0<=t<=1 and 0<=t2<=1: return Point(D.x + t*CD.x, D.y + t*CD.y)
#     return False
    

# def n_partitions(edges, vs):
# #     return len(edges)//2 - len(vs) + 1
#     return len(edges) - len(vs) + 1


    # return len(edges) - len(vs) + 1

# Vs, Es = set(), set()
# def connect(v1, v2):
    



# turn border into 4 walls
# truncate walls to border


# for w in walls:
#     vs = sorted(set(p for u in walls if (p:=intersection(u,w))))
#     for i in range(len(vs)-1):
#         Vs.add(vs[i]) # compare equality with precision? turn into id? sort vs?
#         if i > 0:
#             Es.add((vs[i-1], vs[i]))
            
            

# while walls:
#     w = walls.pop()
#     vs = set([intersection(w,u) for u in walls if do_intersect(u,w)])
# #     connect vs by pairs

# # for w in walls:
# #     for u in walls:
# #         if w == u: continue
# #         if not v:=intersection(w,u): continue
# #         connect(w,v)
# #         connect(u,v) # not collinear

# truncate walls to border
# turn border into 4 walls

# for w in walls:
#     vs = set([intersection(w,u) for u in walls if do_intersect(u,w)])
#     sort(vs)
#     connect(vs[i], vs[i+1]) # like set, ignores duplicates
    
# n_partition = n_cycles(graph)
# return n_partition >= 2

# def intersection # symmetric for float precision
#     connect vs by pairs
# # for w in walls:
#  find intersection 
# # trace path to see if it goes through box

# # cycle if connected but not by the same guy

# def has_partitions(width, height, walls):
#     print(walls)
# #     Expand connected component. If found a cycle, true
# # Remove connected component, try next
#     while walls:
#         w = walls[0]
#         q = deque(w)
#         sources = {w: None}
#         while q:                   #NVM if doesn't work, DFS should find all cycles through source
#             v = q.popleft()
#             for n in neighbors(v, walls):
#                 if n in sources:
#                     path = reconstruct_path(v,n,sources)
#                     if not is_outside(path, width, height):
#                         return True
#                 else:
#                     sources[n] = v
#                     q.append(n)
#         walls = [w for w in walls if w not in sources]
#     return False
            
    

    
# def neighbors(v, walls):
#     return [w for w in walls if intersect(v, w)]

# def intersect(v, w):
#     return ccw(v[0], w[0], w[1]) != ccw(v[1], w[0], w[1]) \
#        and ccw(w[0], v[0], v[1]) != ccw(w[1], v[0], v[1])

# def ccw(A, B, C): # slope AB < slope BC
#     return (B.y-A.y)(C.x-B.x) < (B.x-A.x)(C.y-B.y)


from collections import namedtuple
Point = namedtuple("Point", "x y")



class Graph:
    def __init__(self):
        self.comps = {}
        self.es = set()
        self.n_cycles = 0

    def push_edge(self, v1, v2):
        if (v1, v2) in self.es: return False
        self.es.add((v1, v2))

        for v in (v1, v2):
            if not v in self.comps:
                self.comps[v] = set([v])

        if (c1 := self.comps[v1]) == (c2 := self.comps[v2]):
            self.n_cycles += 1
            return True

        c1.update(c2)
        for v in c2: self.comps[v] = c1
        del c2
        return False

def has_partitions(width, height, walls):
    borders = [
        (Point(0, 0), Point(width,0)),
        (Point(0, 0), Point(0,height)),
        (Point(width, 0), Point(width, height)),
        (Point(0, height), Point(width, height)),
    ]
#     [tuple(Point(x,y) for x in [0, width]) for y in [0, height]] \
#            + [tuple(Point(x,y) for x in [0, width]) for y in [0, height]]
    walls = [u for w in walls if (u:=truncate(w,borders,width, height))]
    walls = sorted(set(walls + borders))
#     print(walls)
    
    on_border = lambda p: (p.x==0 or p.x==width) and (p.y==0 or p.y==height)
    
#     Vs, Es = set(), set()
    G = Graph()
    for w in walls:
        ps = [p for u in walls if u!=w and (p:=intersection(u,w))]
        vs = [Point(0,0) if on_border(p) else p for p in ps]
        print(vs, w)
        vs = sorted(set(vs))
        for v1,v2 in zip(vs, vs[1:]):# in range(1,len(vs)):
#             print(v1, v2, Vs, Es)
#             if (v1,v2) in Es: continue
#             if v1 in Vs and v2 in Vs:
#                 print(v1, v2, w, Vs)
#                 print(Es)
#                 return True
#             Vs.add(v1); Vs.add(v2)
#             Es.add((v1,v2))
            

            if G.push_edge(v1, v2):
                return True
#             if G.n_c Compress wall points to one "point" then find first cycle
#     return G.n_cycles >= 2
    return False


def truncate(wall, borders, width, height):
    out = [p for b in borders if (p := intersection(wall, b))]
    out += [p for p in wall if 0<=p.x<=width and 0<=p.y<=height]
    out = tuple(sorted(set(out)))
    if len(out) != 2: return False
    return out

def intersection(w, u): # sort
    (A,B), (C,D) = sorted([w, u])
    AB = Point(A.x - B.x, A.y - B.y)
    CD = Point(C.x - D.x, C.y - D.y)
    BD = Point(B.x - D.x, B.y - D.y)
    denom  = AB.y*CD.x - AB.x*CD.y
    numer  = AB.y*BD.x - AB.x*BD.y
    numer2 = CD.y*BD.x - CD.x*BD.y
    if denom == 0: # parallel
        print(numer, numer2)
        if numer != 0 or numer2 != 0: return False # not colinear
        # Find where C,D fall along line AB
        magAB = AB.x*AB.x+AB.y*AB.y
        tC = ((C.x-B.x)*AB.x + (C.y-B.y)*AB.y) # (C - B) * (A-B)   /|AB|^2
        tD = ((D.x-B.x)*AB.x + (D.y-B.y)*AB.y) # (D - B) * (A-B)   /|AB|^2

        options = [] # find all endpoints within the intersection
        if 0<=tC<=magAB: options.append(C)
        if 0<=tD<=magAB: options.append(D)
        if min(tC,tD)<=0 and magAB<=max(tC,tD): options += [A,B]
        return min(options) if options else False

    t = numer / denom
    t2 = numer2 / denom
    if not (0<=t<=1 and 0<=t2<=1): return False
    p = Point(D.x + t*CD.x, D.y + t*CD.y)
    return p