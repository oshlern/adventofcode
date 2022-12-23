import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n\n')
# ll = [int(l) for l in ll if len(l) > 0]

ns = eval('['+ll[0]+']')

bs = []
for b in ll[1:]:
    bo = []
    for l in b.split('\n'):
        # print(l)
        r = []
        for i in range(5):
            r.append(int(l[3*i:3*(i+1)]))
        bo.append(r)
    bs.append(np.array(bo))

Bs = [np.zeros((5,5), dtype=bool) for _ in bs]

def fin(B):
    for i in range(5):
        if np.all(B[i,:]) or np.all(B[:,i]):
            return True
    return False

fins = []
last_score = 0
for n in ns:
    # print(n)
    for i,b in enumerate(bs):
        if i in fins:
            continue
        Bs[i] |= b == n
        # print(n, i, Bs[i], b == n)
        if fin(Bs[i]):
            a1 = np.sum(b * (1-Bs[i]))
            print(a1 * n, a1, n)
            last_score = a1*n
            fins.append(i)
            # break
    # else:
    #     continue
    # break
print(last_score)
    