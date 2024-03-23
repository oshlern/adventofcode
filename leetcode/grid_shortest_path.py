# https://www.codewars.com/kata/5573f28798d3a46a4900007a/train/python

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