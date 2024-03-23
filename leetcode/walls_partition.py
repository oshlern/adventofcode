# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python
# from collections import namedtuple
# Point = namedtuple("Point", "x y")


# remove duplicates, truncate to within walls, remove collinear?
# Make sure intersection is not overlapping


while walls:
    w = walls.pop()
    vs = set([intersection(w,u) for u in walls if do_intersect(u,w)])
#     connect vs by pairs

# for w in walls:
#     for u in walls:
#         if w == u: continue
#         if not v:=intersection(w,u): continue
#         connect(w,v)
#         connect(u,v) # not collinear

truncate walls to border
turn border into 4 walls

for w in walls:
    vs = set([intersection(w,u) for u in walls if do_intersect(u,w)])
    sort(vs)
    connect(vs[i], vs[i+1]) # like set, ignores duplicates
    
n_partition = n_cycles(graph)
return n_partition >= 2

def intersection # symmetric for float precision
    connect vs by pairs
# for w in walls:
 find intersection 
# trace path to see if it goes through box

# cycle if connected but not by the same guy

def has_partitions(width, height, walls):
    print(walls)
#     Expand connected component. If found a cycle, true
# Remove connected component, try next
    while walls:
        w = walls[0]
        q = deque(w)
        sources = {w: None}
        while q:                   #NVM if doesn't work, DFS should find all cycles through source
            v = q.popleft()
            for n in neighbors(v, walls):
                if n in sources:
                    path = reconstruct_path(v,n,sources)
                    if not is_outside(path, width, height):
                        return True
                else:
                    sources[n] = v
                    q.append(n)
        walls = [w for w in walls if w not in sources]
    return False
            
    

    
def neighbors(v, walls):
    return [w for w in walls if intersect(v, w)]

def intersect(v, w):
    return ccw(v[0], w[0], w[1]) != ccw(v[1], w[0], w[1]) \
       and ccw(w[0], v[0], v[1]) != ccw(w[1], v[0], v[1])

def ccw(A, B, C): # slope AB < slope BC
    return (B.y-A.y)(C.x-B.x) < (B.x-A.x)(C.y-B.y)