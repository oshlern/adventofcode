# https://www.codewars.com/kata/58f58dc3663082a4ba000033/train/python
from collections import defaultdict
ARROWS = "↑↗→↘↓↙←↖"
DIRS = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]
Ds = {a: d for a,d in zip(ARROWS, DIRS)}

def is_within_90(D1, D2):
    return D1[0]*D2[0] + D1[1]*D2[1] >= 0

ALLOWABLE_Ds = { a1: 'S'+''.join([a2 for a2,d2 in Ds.items() if is_within_90(d1, d2)]) for a1,d1 in Ds.items() }
ALLOWABLE_Ds['S'] = ARROWS

def dance(dance_map):
    dance_map = dance_map.split('\n')
    L, W = len(dance_map), len(dance_map[0])
    coords = [(x,y) for x in range(L) for y in range(W)]
    neighbors = defaultdict(list)
    for c in coords:
        for a, d in Ds.items():
            if dance_map[c[0]][c[1]] not in ALLOWABLE_Ds[a]:
                continue
            n = (c[0]+d[0], c[1]+d[1])
            if not ((0 <= n[0] < L) and (0 <= n[1] < W)):
                continue
            if dance_map[n[0]][n[1]] not in ALLOWABLE_Ds[a]:
                continue
            neighbors[c].append((n, a))

#     s = (L//2, W//2)
    for x in range(L):
        for y in range(W):
            if dance_map[x][y] == "S":
                s = (x, y)
    unvisited = set(coords)
    longest_path = ""
#     while unvisited:
#         for n,a in neighbors[c].items():
#         for n in unvisited & neighbors[c].keys():
#             if n not in unvisited:
#                 continue
#             path += a
#             if n == start:
#                 if len(longest_path) < len(path):
#                     longest_path = path
#             else:


    def find_longest_path_to_s(c):
        nonlocal s, unvisited, neighbors
#         print(c, unvisited, neighbors[c])
        longest_path = ""

        unvisited.remove(c)
        for n,a in neighbors[c]:
            if n == s:
                new_path = a
#                 print("S", c, n, new_path)
            else:
                if n not in unvisited:
                    continue
                rest_path = find_longest_path_to_s(n)
                if not rest_path:
                    continue
                new_path = a + rest_path
#                 print("N", c, n, new_path)

            if len(new_path) > len(longest_path):
                longest_path = new_path
        unvisited.add(c)
#         print(c, longest_path)
        return longest_path

    l = find_longest_path_to_s(s)
    print("LLLL", l)
    return l


#     i_len paths to S
#








    print(neighbors)


#         for X in range(max(0, x-1), min(L, x+1)):
#             for Y in range(max(0, y-1), min(W, y+1)):
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                 X, Y = x + dx, y + dy
#                 if (X, Y) == (x, y):
#                     continue
#                 if dance_map[x][y]:


#         ns = [(X, Y), ]
#         neighbors[(x,y)] = ns

#     print(neighbors)

    pass
