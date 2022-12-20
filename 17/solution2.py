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
N = 1000000000000

print("LLLL", len(l))
once = True
rock_i = 0
S = []
S2 = []
li_0 = 7 if len(sys.argv) == 1 else 5
print(li_0)
while rock_i < N:
    s = ss[rock_i % len(ss)]
    if rock_i % len(ss) == 0 and li % len(l) == li_0:
        if S:
            print(max_y - S[-1], S[:10])
            print(rock_i - S2[-1], S2[:10])
            y_diff = max_y - S[-1]
            i_diff = rock_i - S2[-1]
            n_skip = (N - rock_i) // i_diff
            rock_i += n_skip * i_diff
        S.append(max_y)
        S2.append(rock_i)
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
    tower[y:y+sh,x:x+sw] |= s
    dy = y + sh - max_y
    if dy > 0:
        tower = np.concatenate((tower, np.zeros((dy,7), dtype=bool)))
        max_y += dy
    rock_i += 1

print(n_skip, y_diff, max_y)
display(tower)
print(n_skip * y_diff + max_y)
