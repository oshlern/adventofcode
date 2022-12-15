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

nss = []
def convert_coords
for s in ss:


ss = np.array([list(s) for s in ss])
ds = np.array(ds)
n = 4000000 if len(sys.argv) == 1 else 20
# for x in range(n+1):
#     if x % 10 == 0:
#         print(x)
#     for y in range(n+1):
#         # if dist(x, y, cx, )
#         # print(ss - )
#         dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
#         if np.all(dists > ds):
#             print(x,y)

x0 = n
y0 = 0
x = n
y = 0
dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
diffs = dists <= ds
while np.any(diffs):
    # print(diffs.shape)
    # print(np.where(diffs), i)
    i = np.where(diffs)[0][0]


# for i, di in enumerate(dists):
#     if di < ds[i]:
    sx, sy = ss[i]
    # d_perp = abs((x - y)  - (sx -sy))
    # d_ort = ds[i] - d_perp
    # x += d_ort
    # y += d_ort
    m = sx + sy + d
    m1 = max(x + y - m, 0)
    x += m1//2+1
    y += m1//2+1
    if x > n or y > n:
        if x0 % 100 == 0 and y0 % 100 == 0:
            print(x0, y0)
        if x0 > 0:
            x0 -= 1
        else:
            y0 += 1
        x = x0
        y = y0
    dists = np.sum(np.abs(ss - np.array([[x,y]])), axis=1)
    diffs = dists <= ds
print(x, y)
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


    
# print(o)
