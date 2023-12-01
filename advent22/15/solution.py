import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
# ll = [int(l) for l in ll if len(l) > 0]
ss = []
bs = []
ds = []

def dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


dxs = []
y = 2000000 if len(sys.argv) == 1 else 10
# y = 10
tot = 0

Xs = []
for l in ll:
    l = l.split('=')
    # sx = 
    # c, l = 
    # print()
    sx = int(l[1].split(',')[0])
    sy = int(l[2].split(':')[0])
    bx = int(l[3].split(',')[0])
    by = int(l[4])
    # l = l.split('=')[-1]
    # c, l = l.split(':')
    # sy = int(c)
    # l = l.split('=')[-1]
    # c, l = l.split(',')
    # bx = int(c)
    # c = l.split('=')[-1]
    # by = int(c)
    # bx, by = by, bx
    # sx, sy = sy, sx

    # x1 = bx
    # x2 = sx - bx 
    d = abs(sx - bx) + abs(sy - by)
    bs.append((bx, by))
    ss.append((sx, sy))
    ds.append(d)

    dy = abs(sy - y)
    dx = d - dy
    if dx >= 0:
        dxs.append((sx, dx))
        # print('\t', sx,sy,  bx, by, dx)
        # tot += 1 + 2 * dx
        # print(sx - dx, "to", sx+dx)
        # Xs.append(sx - dx)
        rm = []
        x1, x2 = sx - dx, sx + dx
        if by == y:
            if bx == x1:
                x1 += 1
            if bx == x2:
                x2 -= 1
            if x1 > x2:
                continue
        # print('\t\t', (x1, x2))
        for i in range(len(Xs)):
            X1, X2 = Xs[i]
            if (X1 >= x1 and X1 <= x2) or (X2 >= x1 and X2 <= x2):
                # Xs.pop(i)
                rm.append(i)
                x1 = min(x1, X1)
                x2 = max(x2, X2)
            if (x1 >= X1 and x2 <= X2):
                break
        else:
            for i in rm[::-1]:
                temp = Xs.pop(i)
            #     print("removed", temp)
            # print("added", (x1, x2))
            Xs.append((x1, x2))
    # else:
        # print(sx, sy, bx, by)
    # if by == y:
    #     print('_', '\t', sx,sy,  bx, by, dx)

    #     tot -= 1

    # bs 
    # bx
    # x1, x2 = 

    # d = dist(sx, sy, bx, by)
    
print(Xs)
# print(tot)
tot = sum([x2-x1+1 for x1, x2 in Xs])
print(tot)

rms = set()
for i in range(len(ds)):
    s1x, s1y = ss[i]
    for j in range(i+1, len(ds)):
        s2x, s2y = ss[j]
        d = dist(s1x, s1y, s2x, s2y)
        if ds[i] - ds[j] >= d:
            # print(i, ss[i], j, ss[j])
            rms.add(j)
        elif ds[j] - ds[i] >= d:
            # print(j, ss[j], i, ss[i])
            rms.add(i)
print(ds)
# print()
for i in rms:
    print(ds[i], ss[i])
    ss.pop(i)
    ds.pop(i)
    bs.pop(i)
print(ds)

# nss = []
# def convert_coords
# for s in ss:


ss = np.array([list(s) for s in ss])
ds = np.array(ds)
n = 4000000 if len(sys.argv) == 1 else 20




def boundary(s, d):
    d = d+1
    p = np.expand_dims(s, 0) + d * np.array([[-1,0]])
    yield p
    diags = [np.array([[1,1]]), np.array([[1,-1]]), np.array([[-1,-1]]), np.array([[-1,1]])]
    for dp in diags:
        for _ in range(d):
            p += dp
            yield p

del dist

def bound(c):
    c -= min(c.real, 0)
    c -= min(c.imag, 0)*1.0j
    c -= max(c.real - n, 0)
    c -= max(c.imag - n, 0)*1.0j
    return c

def to_bound(c):
    to_bound_r = max(-c.real, max(c.real-n,0))
    to_bound_i = max(-c.imag, max(c.imag-n,0))
    return max(to_bound_r, to_bound_i)

def dot(a,b):
    return a.real *b.real + a.imag * b.imag
# def scan(c1, c2):
def scan(c1_1, c1_2, c2_1, c2_2):
    # c1, c2 = bound(c1), bound(c2)
    print(c1_1, c1_2, c2_1, c2_2)

    diag = c2_1- c1_1
    l = np.abs(diag.real)
    # print("L", l)
    diag = diag / l
    c1 = c1_1 if dot(c1_1, diag) > dot(c1_2, diag) else c1_2
    c2 = c2_1 if dot(c2_1, diag) > dot(c2_2, diag) else c2_2
    # print(c1_1, c1_2, c2_1, c2_2)
    # print('scanning {} to {}'.format(c1, c2))
    # print(c1)
    l = np.abs((c1-c2).real)

    print("L", l, diag)
    c1 += to_bound(c1) * diag
    c2 -= to_bound(c2) * diag
    if to_bound(c1) > 0.1 or to_bound(c2) > 0.1:
        print("OUT OF BOUNDS")
        return
    start = dot(c1, diag)
    end = dot(c2, diag)
    i = 0
    p = c1
    # print("A", dot(p, diag.real * 1.0j - diag.imag1+1.0j))
    # print("B", dot(p, 1-1.0j))
    # to_b = to_bound(p)
    # if to_b > 0:
    #     i += to_b
    while i < end - start:
        # print(i, p)
        diffs = ss - p
        # print(diffs)
        dists = np.abs(np.real(diffs)) + np.abs(np.imag(diffs))
        # print(p, dists)
        less = dists <= ds
        # print(np.any(less), list(zip(dists, ds)))
        if not np.any(less):
            # print(p)
            yield p
            i += 2
            p += diag

        else:
            sis = np.where(less)[0][0]
            o = i
            i = dot(ss[sis], diag) + ds[sis] + 1 - start
            # print(o, i,ss[sis],ds[sis],diag, dot(ss[sis], diag), start , c1)
            p = c1 + i//2 * diag
            # print(p)
            # skip =  - dot(p[sis], diag) 
            # p += skip * diag
            # i += diag

# print(ss)
# print([s[0] + s[1]*j for s in ss])
print('aaa')
# print([ s[1]*j for s in ss])
ss = np.array([float(s[0]) + s[1]*1.0j for s in ss], dtype=complex)
# print(ss)
for i in range(len(ds)):
    s1, d1 = ss[i], ds[i]
    for j in range(i+1, len(ds)):
        s2, d2 = ss[j], ds[j]
        diff = s1 - s2
        dist = np.abs(np.real(diff)) + np.abs(np.imag(diff))
        # if dist < d1 + d2 + 10:
        #     print(dist,  d1 + d2 + 1, diff, d1, d2)
        if dist == d1 + d2 + 2:
            # print(s1, s2)
            sign_i = np.sign(diff.imag)
            sign_r = np.sign(diff.real)
            # if abs(diff.real) < abs(diff.imag):
            c1_1 = s1 - sign_i * (d1 + 1) * 1.0j
            c1_2 = s2 + sign_r * (d2 + 1)
            c2_1 = s1 - sign_r * (d1 + 1)
            c2_2 = s2 + sign_i * (d2 + 1) * 1.0j
            # else:
            #     c1 = s1 - sign_r * (d1 + 1)
            #     c2 = s2 + sign_r * (d2 + 1)
            print("Ss", s1, d1, s2, d2)
            # print(c1, c2)
            ps = scan(c1_1, c1_2, c2_1, c2_2)
            ps = list(ps)
            if len(ps):
                print("\n\n", ps)
                print(int(ps[0].real * n + ps[0].imag))
    # print(i, d1)
# for (sx, sy), d in zip(ss, ds):
    # for p in boundary(s, d):
    #     if np.any(p > n) or np.any(p < 0):
    #         continue
    #     if np.all(np.sum(np.abs(ss - p), axis=1) > ds):
    #         print("_)_____", p, p[0,0]*n + p[0,1])



# a = np.zeros((n, n))
# coords = np.arange(n)
# xcoords = np.tile(coords, (n, 1))
# ycoords = np.tile(coords.T, (1, n))
# cs = np.array([xcoords, ycoords])
# cs = np.transpose(cs, axes=(n, n, 1))
# dists = np.sum(np.abs(cs - ss - np.array([[x,y]])), axis=1)


# for x in range(n+1):
#     if x % 10 == 0:
#         print(x)
#     for y in range(n+1):
#         i = 2 - 2
        # if dist(x, y, cx, )
        # print(ss - )
        # dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
        # if np.all(dists > ds):
        #     print(x,y)

# x0 = n
# y0 = 0
# x = n
# y = 0
# dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
# diffs = dists <= ds
# while np.any(diffs):
#     # print(diffs.shape)
#     # print(np.where(diffs), i)
#     i = np.where(diffs)[0][0]


# # for i, di in enumerate(dists):
# #     if di < ds[i]:
#     sx, sy = ss[i]
#     # d_perp = abs((x - y)  - (sx -sy))
#     # d_ort = ds[i] - d_perp
#     # x += d_ort
#     # y += d_ort
#     m = sx + sy + d
#     m1 = max(x + y - m, 0)
#     x += m1//2+1
#     y += m1//2+1
#     if x > n or y > n:
#         if x0 % 100 == 0 and y0 % 100 == 0:
#             print(x0, y0)
#         if x0 > 0:
#             x0 -= 1
#         else:
#             y0 += 1
#         x = x0
#         y = y0
#     dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
#     diffs = dists <= ds
# print(x, y)
    # break
    # if 
    # d_orth  = x + y  - (sx+sy)
# if 

# dxs = np.array([list(a) for a in dxs])
# print(dxs)

# # tot = np.sum(dxs[:,1])
# print(tot)

# for i in range(len(dxs)):
#     x1, dx1 = dxs[i]
#     ends1 = []
#     for j in range(i+1, len(dxs)):
#         x2, dx2 = dxs[j]
#         if abs(x1-x2) <= dx1 + dx2:
#             ends = [x1 - dx1, x1 + dx1, x2 - dx2, x2 + dx2]
#             ends.sort()
#             overlap = abs(ends[2] - ends[1]) + 1
#             tot -= overlap 
#             print(overlap, "overlap", x1 - dx1, "to", x1+dx1, "overlaps", x2 - dx2, "to", x2+dx2)
# print(tot)
# # tot += 

# print(bs)
# print(ss)
# print(ds)

# o = 0
# print(len(ds))
# print

# for x in range(min(bx for bx, by in bs) - 4*max(ds), max(bx for bx, by in bs) +4*max(ds)):
#     for i in range(len(ds)):
#         sx, sy = ss[i]
#         bx, by = bs[i]
#         if bx == y and by == x:
#             continue
#         if dist(y, x, sx, sy) <= ds[i]:
#             # print(x, y, i, ss[i], bs[i], ds[i])
#             o += 1
#             break
#     if x % 100000 == 0:
#         print(x)


# def boundary(s, d):
#     d = d+1
#     p = np.expand_dims(s, 0) + d * np.array([[-1,0]])
#     yield p
#     diags = [np.array([[1,1]]), np.array([[1,-1]]), np.array([[-1,-1]]), np.array([[-1,1]])]
#     for dp in diags:
#         for _ in range(d):
#             p += dp
#             yield p
    
# for i in range(len(ds)):
#     s, d = ss[i], ds[i]
#     print(i, d)
# # for (sx, sy), d in zip(ss, ds):
#     for p in boundary(s, d):
#         if np.any(p > n) or np.any(p < 0):
#             continue
#         if np.all(np.sum(np.abs(ss - p), axis=1) > ds):
#             print("_)_____", p, p[0,0]*n + p[0,1])

# def check(x,y):
#     return np.all(np.sum(np.abs(ss - np.array([[x,y]])), axis=1) > ds)
    # diffs = dists <= ds

    
# print(o)


# cleared = set()
# coord = x


# frontier = []

# def pm_coords(pos):
#     x,y = pos
#     plus = x + y
#     minus = x - y
# def xy_coords(pos):
#     x,y = pos
#     plus = x + y
#     minus = x - y


# def get_box(pos): # which coords
#     return b, d

# # first, build tiangleas.
# # Maybe shorter way. Keep building to all 4 corners
# # def get_next(frontier):
# while True:
#     # p1, p2 = frontier[0], frontier[1]
#     f1pm, f1m = frontier[0]
#     x1, y1 = xy_coords(frontier[0])
#     # f1m, f1p = 
#     if y1 > 0:
#         # from the top
#         p = (f1m,0)
#         p = xy_coords
#     else:
#         x2, y2 = frontier[1]
#         mid = (x1 + y1, x2-y2)
#         p = mid
#     b, d = get_box(mid)
#     bx, by = b
#     bp, bm = b
#     np, nm = bp + d, bm + d
#     if np >= f2p:
#         rm(2)
#         np = f2p
#     if nm >= f1m:
#         rm(1)
#         nm = f2m
#     add((np, nm))

# rotate(4)
    
    
# check first
# find box
# add frontier

# cleared
#loop :
    # check next
    # find box
    # clear behind

# clear behind:
# check first
# find box
# clear behind
# def clear_behind():
    
