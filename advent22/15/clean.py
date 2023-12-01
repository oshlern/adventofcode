import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [int(l) for l in ll if len(l) > 0]
ss = []
bs = []
ds = []

y = 2000000 if len(sys.argv) == 1 else 10

Xs = []
for l in ll:
    l = l.split('=')
    sx = int(l[1].split(',')[0])
    sy = int(l[2].split(':')[0])
    bx = int(l[3].split(',')[0])
    by = int(l[4])
    s = sx + sy * 1.0j
    b = bx + by * 1.0j

    d = abs(sx - bx) + abs(sy - by)
    bs.append(b)
    ss.append(s)
    ds.append(d)

    dy = abs(sy - y)
    dx = d - dy
    if dx >= 0:
        rm = []
        x1, x2 = sx - dx, sx + dx
        if by == y:
            if bx == x1:
                x1 += 1
            if bx == x2:
                x2 -= 1
            if x1 > x2:
                continue

        for i in range(len(Xs)):
            X1, X2 = Xs[i]
            if (X1 >= x1 and X1 <= x2) or (X2 >= x1 and X2 <= x2):
                rm.append(i)
                x1 = min(x1, X1)
                x2 = max(x2, X2)
            if (x1 >= X1 and x2 <= X2):
                break
        else:
            for i in rm[::-1]:
                Xs.pop(i)
            Xs.append((x1, x2))
tot = sum([x2-x1+1 for x1, x2 in Xs])
print(tot)

ss = np.array(ss)
ds = np.array(ds)
n = 4000000 if len(sys.argv) == 1 else 20
attempts = []

def to_bound(c):
    to_bound_r = max(-c.real, max(c.real-n,0))
    to_bound_i = max(-c.imag, max(c.imag-n,0))
    return max(to_bound_r, to_bound_i)

def dot(a,b):
    return a.real * b.real + a.imag * b.imag

def scan(c1_1, c1_2, c2_1, c2_2):
    diag = c2_1 - c1_1
    diag = diag / np.abs(diag.real)
    c1 = c1_1 if dot(c1_1, diag) > dot(c1_2, diag) else c1_2
    c2 = c2_1 if dot(c2_1, diag) > dot(c2_2, diag) else c2_2

    l = np.abs((c1-c2).real)

    c1 += to_bound(c1) * diag # bound the search to perimeter
    c2 -= to_bound(c2) * diag
    # it's not obvious diag points c1,c2 towards the perimeter. But it does because the sensors are within the perimeter
    start = dot(c1, diag)
    end = dot(c2, diag)
    i = 0
    p = c1

    while i < end - start:
        diffs = ss - p
        dists = np.abs(np.real(diffs)) + np.abs(np.imag(diffs))
        attempts.append(p)
        less = dists <= ds
        if not np.any(less):
            return p
        else:
            sis = np.where(less)[0]
            dots = [dot(ss[si], diag) + ds[si] for si in sis]
            i = max(dots) + 1 - start
            p = c1 + i//2 * diag # diag is len 2

inds = np.arange(len(ds))
np.random.shuffle(inds)
# print(inds)
ds, ss = ds[inds], ss[inds]

atts = []
for i in range(len(ds)):
    s1, d1 = ss[i], ds[i]
    atts.append(len(ss[i+1:]))
    dists = np.abs(np.real(ss[i+1:]- s1)) + np.abs(np.imag(ss[i+1:]-s1))
    aligned = np.where(dists == ds[i+1:] + d1 + 2)[0] + i+1
    for j in aligned:
        s2, d2 = ss[j], ds[j]
        diff = s1 - s2
        sign_i = np.sign(diff.imag)
        sign_r = np.sign(diff.real)
        c1_1 = s1 - sign_i * (d1 + 1) * 1.0j
        c1_2 = s2 + sign_r * (d2 + 1)
        c2_1 = s1 - sign_r * (d1 + 1)
        c2_2 = s2 + sign_i * (d2 + 1) * 1.0j
        p = scan(c1_1, c1_2, c2_1, c2_2)
        if not p is None:
            print("\n\n", p)
            print(int(p.real * n + p.imag))
            break
    else:
        continue
    break

# print(attempts)
print(len(attempts), len(set(attempts)))
print(len(atts), sum(atts), atts)