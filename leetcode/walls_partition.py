# https://www.codewars.com/kata/60f5868c7fda34000d556f30/train/python   
def has_partitions(width, height, walls):
    
#     Expand connected component. If found a cycle, true
# Remove connected component, try next
    while walls:
        q = deque(walls[0])
        connnected = set()
        while q:
            v = q.popleft()
            for n in neighbors(v, walls):
                if n in connected: return True
                connected.add(n)
                q.append(n)
        walls = [w for w in walls if w not in connected]
    return False
            
        
        if v in connected:
        
    path += [w]
    ns =  neighbors(walls, w)
    if set_intersection(path, ns):
        return True
    for n in ns:
        if search(path, n, walls):
            
        
    for n in:
        
    pass