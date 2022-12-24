import sys
import numpy as np
from collections import defaultdict

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
l = [int(n) for n in ll[0].split(',')]

ns = defaultdict(int)
for n in l:
    ns[n] += 1

print(ns)
# mean = sum([i * n for i,n in ns.items()])/sum([n for i,n in ns.items()])
# print(mean)
# mean = round(mean)
# print(mean)
# out = sum([abs(i-mean) * n for i,n in enumerate(l)])
# print(out)
t = 0
ts = [(t:=t+i) for i in range(max(l)+2)]
print(ts)
# m = int(np.median(l))
# d = sum([abs(n -m) for n in l])
# print(m,d) 
# def dist(ns, m):
#     out = 0
#     for n in ns:
#         out += 

ds = [sum([ts[abs(n-m)] for n in l]) for m in range(max(l))]
print(ds)
print(np.argmin(ds))
print(ds[np.argmin(ds)])


# sum(i*abs(n - m))

