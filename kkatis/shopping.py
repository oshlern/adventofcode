import statistics

T = int(input())
for ti in range(T):
    n = int(input())
    xs = list(map(int, input().split(" ")))
    dist = 2*(max(xs) - min(xs))
    print(dist)
    # m = statistics.median(xs)
    # print(xs, m)
    # dist = 0
    # for x in xs:
    #     dist += abs(x - m)
