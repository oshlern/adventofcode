import heapq
import random

n, m = tuple(map(int, input().split(" ")))

starts = []
ends = []
for ri in range(n):
    start, stay = tuple(map(int, input().split(" ")))
    starts.append(start)
    ends.append(start + stay)
starts.sort()
ends.sort()

ss = iter(starts)
es = iter(ends)
s = next(ss)
e = next(es)
saved = 0
try:
    while True:
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


# n, m = 300000, 10**7
    # x = (random.randint(1, 10**8), random.randint(1, 10**8))
