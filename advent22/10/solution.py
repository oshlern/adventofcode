import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')


tot = 0
X = 1
c = 0

sc = ""
def update():
    global tot, c, X, sc
    sc += "#" if abs(c%40 - X) <= 1 else '.'
    if len(sc) == 40:
        print(sc)
        sc = ""
    c += 1
    if c % 40 == 20:
        tot += c * X

for l in ll:
    l = l.split(' ')
    update()
    if l[0] != "noop":
        update()
        X += int(l[1])

print(tot)