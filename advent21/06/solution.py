import sys
import numpy as np
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
ns = [int(n) for n in ll[0].split(',')]

Ns = defaultdict(int)
for n in ns:
    Ns[n] += 1

for d in range(256):
    # print(ns)
    print(d)
    # print(Ns)
    new_Ns = defaultdict(int)
    for n in Ns:
        if n > 0:
            new_Ns[n-1 ] += Ns[n]
        else:
            new_Ns[6] += Ns[n]
            new_Ns[8] = Ns[n]
    Ns = new_Ns
    # for i in range(len(ns)):
    #     n = ns[i]
    #     if n == 0:
    #         ns[i] = 6
    #         ns.append(8)
    #     else:
    #         ns[i] = n-1
print(sum([Ns[n] for n in new_Ns]))
# print(len(ns))