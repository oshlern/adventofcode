# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python
# from collections import namedtuple
# Point = namedtuple("Point", "x y")


# remove duplicates
# trace path to see if it goes through box

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