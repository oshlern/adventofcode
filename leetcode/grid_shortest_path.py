# https://www.codewars.com/kata/5573f28798d3a46a4900007a/train/python

from preloaded import Node, print_grid # Use print_grid function to visualize a given path on the given grid. 
from collections import deque


def find_shortest_path(grid:list[list[Node]], start_node:Node, end_node:Node):
    if not grid: return []
    x_len, y_len = len(grid), len(grid[0])
    S, E = start_node.position, end_node.position
    S, E = (S.x, S.y), (E.x, E.y)

    def get_ns(x,y):
        return [(nx,ny) for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] \
            if 0<=nx<x_len and 0<=ny<y_len and grid[nx][ny].passable]
            
    q = deque([(0,S,[S])])
    while deque:
        d, v, path = q.popleft()
        if v == E: return path
        for n in get_ns(*v):
            q.append((d+1,n,path+[grid[n[0]][n[1]]]))