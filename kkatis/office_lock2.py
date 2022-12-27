import time
import heapq
import random


# n, m = tuple(map(int, input().split(" ")))
n, m = 300000, 10**7
t_start = time.time()

Rs = []
rs = []
for ri in range(n):
    x = (random.randint(1, 10**8), random.randint(1, 10**8))
    # x = tuple(map(int, input().split(" ")))
    rs.append(x)
    heapq.heappush(Rs, x)
old = len(Rs)
# print(Rs)
rs.sort(key=lambda x: x[0])
# print([(r[0]/10**7,r[1]/10**7) for r in Rs])
print("Setup", time.time() - t_start)
t_start = time.time()



Ss = []
t = 0
used = 0
starts = []
ends = []
while Rs:
    start, stay = heapq.heappop(Rs)
    dt = start - t
    Ss = [s - dt for s in Ss]
    # while Ss and Ss[0] < -m:
    #     heapq.heappop(Ss)
    #     used += 1
    if Ss and -m <= Ss[0] <= 0:
        heapq.heappop(Ss)
    heapq.heappush(Ss, stay)
    t = start
tot = used + len(Ss)
print("Rest", time.time() - t_start)

print(old - tot)


# s1, s2, s3, s4, s5
# e1, e2, e3, e4, e5
# e1, e2, e3, e4+m, e5+m

si, ei = 0, 0
# for i, s in enumerate(starts):
# iter
ss = iter(starts)
es = iter(ends)
s = next(ss)
e = next(es)
saved = 0
try:
    while True:
# while si < len(starts) and ei < len(ends):
    # s, e = starts[si], ends[ei]
        if e > s:
            s = next(ss)
        elif s > e + m:
            e = next(es)
        else:
            saved += 1
            s = next(ss)
            e = next(es)
except StopIteration:
    print(saved)





# s1, s2, e2, s3, s4, e2+m s5
# s1, s2, e2, e1, s3, s4, e2+m s5

# start + stay + m
# start ^
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