import sys
import numpy as np
from collections import defaultdict

ll = open('shapes').read().strip().split('\n\n')
ss = [np.array([[c == "#" for c in row] for row in l.split('\n')][::-1]) for l in ll]
# ss = np.array([[[c == "#" for c in row] for row in l.split('\n')[::-1]] for l in ll])

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
l = open(filename).read().strip().split('\n')[0]
li = 0
# ll = [int(l) for l in ll if len(l) > 0]

width = 7
max_y = 0
# tower = np.concatenate(np.ones((1,7)), np.zeros((3,7)))
tower = np.zeros((7,7), dtype=bool)

def display(tower):
    for r in tower[-20:-5][::-1]:
        string = ''.join(['#' if ri else '.' for ri in r])
        print('|' + string + '|')
    print('+-------+')
# tower = 
# tower = {}
# display(tower)
# n = 2022
# n = 2022
min_n = len(l)*len(ss)
N = 1000000000000

vis = set()
vis2 = {}
vis3 = defaultdict(list)
# print(n)
print("LLLL", len(l))
# def advance(_n, l0=0, s0=0):
#     global tower, max_y, width, ss, li, l
# # for n in [10000000]:#[min_n, min_n,N % min_n]:
#     for rock_i in range(_n):
#         # print(li % len(l))
#         if li % len(l) == l0:
#             print("L", li)
#         # if rock_i % len(ss):
#         #     print("S", li)
#         if li % len(l) == l0 and rock_i % len(ss) == s0:
#             print(li, rock_i)
#             display(tower)
#         if rock_i % 10000 == 0:
#             print(rock_i)
#         s = ss[rock_i % len(ss)]
#         if rock_i % len(ss) == 0:
#             v = (rock_i % len(ss), li % len(l))
#             if v in vis:
#                 print(v, rock_i)
#                 print(max_y - vis2[v][0])
#                 print(rock_i - vis2[v][1])
#             vis2[v] = (max_y, rock_i)
#             vis.add(v)
#         sw, sh = s.shape[1], s.shape[0]
#         x = 2
#         y = max_y + 3
#         dropping = True
#         while dropping:
#             t = np.copy(tower)
#             # print(t.shape, y,x,sh,sw,t[y:y+sh,x:x+sw].shape,s.shape)
#             t[y:y+sh,x:x+sw] |= s
#             # display(t)
#             shift = 1 if l[li % len(l)] == ">" else -1
#             li += 1
#             x += shift
#             # print(s, sh, sw)
#             # print(tower.shape, y, x)
#             # print(tower[y:y+sh,x:x+sw].shape)
#             if x < 0 or x + sw > width or np.any(s & tower[y:y+sh,x:x+sw]):
#                 x -= shift
#             y -= 1
#             # print(s, sh, sw)
#             # print(tower.shape, y, x, y+sh, x+sw)
#             # print(tower[y:y+sh,x:x+sw].shape)
#             if y < 0 or np.any(s & tower[y:y+sh,x:x+sw]):
#                 y += 1
#                 dropping = False
#             # print(x,y, l[li], shift)
#         tower[y:y+sh,x:x+sw] |= s
#         dy = y + sh - max_y
#         if dy > 0:
#             # print(y, sh, dy, max_y)
#             tower = np.concatenate((tower, np.zeros((dy,7), dtype=bool)))
#             max_y += dy
#     mid_y = max_y
#     display(tower)
#     return rock_i

# advance(min_n)
# l0 = li % len(l)
# advance(min_n)
# l0 = li % len(l)

# advance(min_n)


# print((N // min_n) * mid_y + max_y)
# print((N // min_n - 1) * mid_y + max_y)
# print(max_y)




# once = True
# rock_i = 0

once = True
rock_i = 0
# while rock_i < len(l)*10:
#     s = ss[rock_i % len(ss)]
#     sw, sh = s.shape[1], s.shape[0]
#     x, y = 2, max_y + 3
#     while True:
#         shift = 1 if l[li % len(l)] == ">" else -1
#         li += 1
#         x += shift
#         if x < 0 or x + sw > width or np.any(s & tower[y:y+sh,x:x+sw]):
#             x -= shift
#         y -= 1
#         if y < 0 or np.any(s & tower[y:y+sh,x:x+sw]):
#             y += 1
#             break
#         # print(x,y, l[li], shift)
#     tower[y:y+sh,x:x+sw] |= s
#     dy = y + sh - max_y
#     if dy > 0:
#         # print(y, sh, dy, max_y)
#         tower = np.concatenate((tower, np.zeros((dy,7), dtype=bool)))
#         max_y += dy
#     rock_i += 1

while rock_i < N:
    s = ss[rock_i % len(ss)]
    if once:
        if rock_i % len(ss) == 0:
            v = (rock_i % len(ss), li % len(l))
            if v in vis3:

                # print(v, rock_i)
                if len(vis3[v]) == 65:
                    y_diff = max_y - vis3[v][5][0]
                    i_diff = rock_i - vis3[v][5][1]
                    n_skip = (N - rock_i) // i_diff
                    rock_i += n_skip * i_diff
                # print(vis3[v], max_y, rock_i)
                # o = [vis3[v][i][0] - vis3[v][i-1][0] for i in range(1, len(vis3[v]))]
                # o2 = [vis3[v][i][1] - vis3[v][i-1][1] for i in range(1, len(vis3[v]))]
                # print(max_y, rock_i, o, o2)
                # once = False

            vis2[v] = (max_y, rock_i)
            vis3[v].append((max_y, rock_i))
            
            # vis.add(v)
    sw, sh = s.shape[1], s.shape[0]
    x, y = 2, max_y + 3
    while True:
        shift = 1 if l[li % len(l)] == ">" else -1
        li += 1
        x += shift
        if x < 0 or x + sw > width or np.any(s & tower[y:y+sh,x:x+sw]):
            x -= shift
        y -= 1
        if y < 0 or np.any(s & tower[y:y+sh,x:x+sw]):
            y += 1
            break
        # print(x,y, l[li], shift)
    tower[y:y+sh,x:x+sw] |= s
    dy = y + sh - max_y
    if dy > 0:
        # print(y, sh, dy, max_y)
        tower = np.concatenate((tower, np.zeros((dy,7), dtype=bool)))
        max_y += dy
    rock_i += 1

print(n_skip, y_diff, max_y)
print(n_skip * y_diff + max_y)
print(1514285714288)
display(tower)



        # t = np.copy(tower)
        # t[y:y+sh,x:x+sw] |= s
        # display(t)