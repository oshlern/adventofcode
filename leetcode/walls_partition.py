# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python
from collections import namedtuple
Point = namedtuple("Point", "x y")

# class Graph:
#     def __init__(self):
#         self.comps = {}
#         self.es = set()
#         self.n_cycles = 0

#     def push_edge(self, v1, v2):
#         if (e:=(v1, v2)) in self.es: return
#         self.es.add(e)
#         if not v1 in self.comps: self.comps[v1] = set([v1])
#         if not v2 in self.comps: self.comps[v2] = set([v2])

#         if (c1 := self.comps[v1]) != (c2 := self.comps[v2]):
#             c1.update(c2) # merge components
#             for v in c2: self.comps[v] = c1
#             del c2
#         else:
#             self.n_cycles += 1

# def has_partitions(width, height, walls):
#     border = [Point(0,0), Point(width,0), Point(width,height), Point(0,height)]
#     borders = list(zip(border, border[1:] + [border[0]]))
#     walls = [w_trunc for w in walls if (w_trunc:=truncate(w,borders,width,height))]
#     walls = sorted(set(walls + borders))

#     G = Graph()
#     for w in walls:
#         vs = sorted(set(p for u in walls if u!=w and (p:=intersection(u,w))))
#         for v1,v2 in zip(vs, vs[1:]):
#             G.push_edge(v1, v2)
#     return G.n_cycles >= 2

# def truncate(wall, borders, width, height):
#     out = [p for b in borders if (p := intersection(wall, b))] # add interesections with border
#     out += [p for p in wall if 0<=p.x<=width and 0<=p.y<=height] # remove out of bounds points
#     out = tuple(sorted(set(out))) 
#     return out if len(out)==2 else False


# def on_segment(p, A, B):
#     det = lambda A, B: A[0]*B[1] - A[0]*B[1]
#     p_minus_A = (p.x-A.x, p.y-A.y)
#     p_minus_B = (p.x-B.x, p.y-B.y)
#     det((p.x-A.x, p.y-A.y), (p.x-B.x, p.y-B.y)) != 0 and (A.x<=p.x<=B.x or A.x>=p.x>=B.x) and (A.y<=p.y<=B.y or A.y>=p.y>=B.y) 


#     (a.x - c.x)*(c.y - b.y) == (c.x - b.x)*(a.y - c.y)
#     p - A = (B-a)*c  0<=c<=1
#     (p - A)

def intersection(w, u): # sort
    (A,B), (C,D) = sorted([w, u])
    # det = lambda A, B: A.x*B.y - A.y*B.x
    dist = lambda A, B: ((A.x-B.x)**2 + (A.y-B.y)**2)**0.5
    on_segment = lambda p, A, B: dist(A,p) + dist(p, B) == dist(A,B)
    det = lambda A, B: A[0]*B[1] - A[1]*B[0]
    # on_segment = lambda p, A, B: abs(det((p.x-A.x, p.y-A.y), (p.x-B.x, p.y-B.y))) < 1e-16 and (A.x<=p.x<=B.x or A.x>=p.x>=B.x) and (A.y<=p.y<=B.y or A.y>=p.y>=B.y) 
    x_diffs = (A.x-B.x, C.x-D.x)
    y_diffs = (A.y-B.y, C.y-D.y)
    denom = det(x_diffs, y_diffs)
    if denom != 0:
        d = (det(A,B), det(C,D))
        p = Point(det(d, x_diffs) / denom, det(d, y_diffs) / denom)
        if on_segment(p, A, B) and on_segment(p, C, D):
            return p
    else:
        if on_segment(A, C, D): return A
        if on_segment(B, C, D): return B
        if on_segment(C, A, B): return C
        if on_segment(D, A, B): return D




def intersection2(w, u):
    (A,B), (C,D) = w, u
    dist = lambda A, B: ((A.x-B.x)**2 + (A.y-B.y)**2)**0.5
    on_segment = lambda p, A, B: abs(dist(A,p) + dist(p, B) - dist(A,B)) < 1e-10
    det = lambda A, B: A[0]*B[1] - A[1]*B[0]
#     on_segment = lambda p, A, B: abs(det((p.x-A.x, p.y-A.y), (p.x-B.x, p.y-B.y))) < 1e-10 and (A.x<=p.x<=B.x or A.x>=p.x>=B.x) and (A.y<=p.y<=B.y or A.y>=p.y>=B.y) 

    x_diffs = (A.x-B.x, C.x-D.x)
    y_diffs = (A.y-B.y, C.y-D.y)
    denom = det(x_diffs, y_diffs)
    if denom != 0:
        d = (det(A,B), det(C,D))
        px = round(det(d, x_diffs) / denom, 14)
        py = round(det(d, y_diffs) / denom, 14)
        ps = [Point(px, py)]
    else:
        ps = [A,B,C,D]

    ps = [p for p in ps if on_segment(p, A, B) and on_segment(p, C, D)]
    return min(ps) if ps else False