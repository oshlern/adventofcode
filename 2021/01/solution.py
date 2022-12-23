import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
ll = [int(l) for l in ll if len(l) > 0]

l = np.array(ll)
# a = l
a = sum(l[i:len(l)-2+i] for i in range(3))
print(np.sum(a[1:] > a[:-1]))
