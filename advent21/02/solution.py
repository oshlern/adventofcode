import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [int(l) for l in ll if len(l) > 0]

h, d = 0, 0
a = 0
for l in ll:
    print(l)
    if l.startswith('for'):
        h += int(l.split(' ')[-1])
        d += a*int(l.split(' ')[-1])
    if l.startswith('down'):
        a -= int(l.split(' ')[-1])
    if l.startswith('up'):
        a += int(l.split(' ')[-1])

print(h*d)