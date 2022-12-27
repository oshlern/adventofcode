n, m = tuple(map(int, input().split(" ")))
print(n,m)

rs = []
for ri in range(n):
    start, stay = tuple(map(int, input().split(" ")))
    for i in range(len(rs)):
        if start < rs[i][0]:
            rs.insert(i, (start, stay))
            break
    else:
        rs.append((start, stay))

old = len(rs)

stations = []
t = 0
used = 0
for start, stay in rs:
    dt = start - t
    # for i, s in enumerate(stations):
    seated = False
    for i in range(len(stations)-1,-1,-1):
        s = stations[i]
        ns = s - dt
        if ns < -m:
            stations.pop(i)
            used += 1
        elif ns <= 0 and not seated:
            print(ns)
            stations.pop(i)
            seated = True
        else:
            stations[i] = ns
    for i, s in enumerate(stations):
        if stay > s:
            stations.insert(i, stay)
            break
    else:
        stations.append(stay)
    print((start, stay), dt, stations)
    t = start
tot = used + len(stations)
print(old, tot)
print(old - tot)

# for start, stay in rs:
#     dt = start - t
#     # for i, s in enumerate(stations):
#     for i in range(len(stations)-1,-1,-1):
#         s = stations[i]
#         if s < -m:
#             continue
#         ns = s - dt
#         if -m <= ns <= 0:
#             stations[i] = stay
#         else:
#             stations[i] = ns