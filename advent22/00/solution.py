import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))