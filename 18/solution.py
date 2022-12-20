import sys
import numpy as np
import itertools

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip()
coords = np.array(eval('[[' + '], ['.join(ll.split('\n')) + ']]'))

coords -= np.min(coords, axis=0) - 1
shape = np.max(coords, axis=0) + 3
air = np.ones(shape, dtype=bool)
for c in coords:
    air[c[0], c[1], c[2]] = False

tot = 0
for c in coords:
    for i in range(3):
        c[i] += 1
        tot += air[c[0], c[1], c[2]]
        c[i] -= 2
        tot += air[c[0], c[1], c[2]]
        c[i] += 1
print("Part 1", tot)

lava = set([tuple(c) for c in coords])
outside = set()
queue = [(0,0,0)]
while queue:
    c = queue.pop()
    if c in outside or c in lava:
        continue
    outside.add(c)
    if c[0] > 0:
        queue.append((c[0] - 1, c[1], c[2]))
    if c[0] < shape[0] - 1:
        queue.append((c[0] + 1, c[1], c[2]))
    if c[1] > 0:
        queue.append((c[0], c[1] - 1, c[2]))
    if c[1] < shape[1] - 1:
        queue.append((c[0], c[1] + 1, c[2]))
    if c[2] > 0:
        queue.append((c[0], c[1], c[2] - 1))
    if c[2] < shape[2] - 1:
        queue.append((c[0], c[1], c[2] + 1))

print(np.product(shape) - len(outside) - len(lava), len(lava), len(outside), np.product(shape))

tot = 0
for c in coords:
    for i in range(3):
        c[i] += 1
        tot += tuple(c) in outside
        c[i] -= 2
        tot += tuple(c) in outside
        c[i] += 1
print("Part 2", tot)