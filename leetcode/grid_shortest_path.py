# https://www.codewars.com/kata/5573f28798d3a46a4900007a/train/python

# A*
from preloaded import Node, print_grid # Use print_grid function to visualize a given path on the given grid. 
import heapq, math

class ComparableNode(Node):
    __lt__ = lambda self, other: True

def find_shortest_path(grid:list[list[Node]], start_node:Node, end_node:Node):
    if not grid: return []

    h = lambda n: abs(n.position.x - end_node.position.x) + abs(n.position.y - end_node.position.y)

    def reconstruct_path(v):
        path = [v]
        while v is not start_node:
            v = v.parent
            path.append(v)
        return list(reversed(path))

    def get_ns(v):
        x, y = v.position.x, v.position.y
        return [grid[nx][ny] for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] \
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny].passable]

    for r in grid:
        for v in r:
            v.h = h(v)
            v.g = math.inf
            v.__class__ = ComparableNode

    start_node.g = 0
    q = [(start_node.h, start_node)]

    while q:
        v = heapq.heappop(q)[1]
        if v is end_node: return reconstruct_path(v)

        for n in get_ns(v):
            if (g := v.g + 1) < n.g:
                n.g = g
                n.parent = v
                heapq.heappush(q, (n.g + n.h, n))


#  BFS
from preloaded import Node, print_grid # Use print_grid function to visualize a given path on the given grid. 
from collections import deque

def find_shortest_path(grid:list[list[Node]], start_node:Node, end_node:Node):
    if not grid: return []

    def get_ns(v):
        x, y = v.position.x, v.position.y
        # ns =  [(x-1,y),(x+1,y)] if end_node.position.x < x else [(x+1,y),(x-1,y)]
        # ns += [(x,y-1),(x,y+1)] if end_node.position.y < y else [(x,y+1),(x,y-1)]
        # return [grid[nx][ny] for nx,ny in ns  \
        #     if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny].passable]
#             [(x-1,y),(x+1,y)]
#         ns = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
        return [grid[nx][ny] for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] \
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny].passable]
            
    q = deque([(start_node,[start_node])])
    visited = set()
    while deque:
        v, path = q.popleft()
        visited.add(v)
        if v == end_node: return path
        for n in get_ns(v):
            if n not in visited:
                q.append((n,path+[n]))