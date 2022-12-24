import sys
import numpy as np
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
dots, instrs = open(filename).read().strip().split('\n\n')

dots = set([tuple([int(n) for n in l.split(',')]) for l in dots.split('\n')])
print( instrs.split('\n'))
instrs = [(ins.split('=')[0][-1] == 'x', int(ins.split('=')[1])) for ins in instrs.split('\n')]
print(dots)
print(instrs)

for instr in instrs:
    print(instr)
    print(len(dots))
    # for i in range(max(d[0] for d in dots)+1):
    #     print(''.join(['#' if (i,j) in dots else '.' for j in range(max(d[1] for d in dots)+1)]))

    # for i in range(max(d[0] for d in dots)):
    # grid = max(d[0] for d in dots)
    # for d in dots
    ind = int(instr[0])
    new_dots = set()
    for d in dots:
        if instr[0]:
            if d[0] < instr[1]:
                new_dots.add(d)
            else:
                new_dots.add((2*instr[1] - d[0], d[1]))
        else:
            if d[1] < instr[1]:
                new_dots.add(d)
            else:
                new_dots.add((d[0], 2*instr[1] - d[1]))
    dots = new_dots


for i in range(max(d[0] for d in dots)+1):
        print(''.join(['#' if (i,j) in dots else '.' for j in range(max(d[1] for d in dots)+1)]))
