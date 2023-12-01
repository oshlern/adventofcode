import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
ll = np.array([[int(a) for a in l] for l in ll if len(l) > 0])

n = len(ll)
# print(ll.shape, ll)
# ins = [l for l in ll]
# outs = [l for l in ll]
# out = []
# for i in range(ll.shape[1]):
#     o = int(np.sum(ll[:,i]) >= n/2)
#     print(o, np.sum(ll[:,i]) >= n/2)
#     out.append(o)
#     ins = [x for x in ins if x[i] == o]
#     outs = [x for x in outs if x[i] == 1-o]

#     print(ins, outs)

ins = [l for l in ll]
for i in range(ll.shape[1]):
    if len(ins) == 1:
        break
    o = int(np.sum(np.array(ins)[:,i]) >=len(ins)/2)
    # print(o, np.array(ins)[:,i])

    ins = [x for x in ins if x[i] == o]
    # print(ins)
a1 = ins[0]
ins = [l for l in ll]
for i in range(ll.shape[1]):
    if len(ins) == 1:
        break
    o = int(np.sum(np.array(ins)[:,i]) >= len(ins)/2)
    ins = [x for x in ins if x[i] == 1-o]
a2 = ins[0]

print(a1, a2)
def to10(a):
    out = 0
    for i, c in enumerate(a[::-1]):
        out += c * 2**i
    return out
print(to10(a1) * to10(a2))
    # print(ins, outs)
# b = [1 - o for o in out]

print(to10(out) * to10(b))