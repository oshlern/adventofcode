def solution(map):
    w, h = len(map), len(map[0])
    big_dist = w*h
    def neighbors(v):
        orths = [
            (v[0]+1, v[1]),
            (v[0]-1, v[1]),
            (v[0], v[1]+1),
            (v[0], v[1]-1),
        ]
        ns = [n for n in orths if (0 <= n[0] < w and 0 <= n[1] < h) and (map[n[0]][n[1]] == 0)]
        return ns

    def dist_map(v0):
        d = 1
        dists = {}
        visited = []
        q = [v0]
        while q:
            next_q = []
            for v in q:
                dists[v] = d
                next_q += [n for n in neighbors(v) if (not n in next_q) and (not n in dists)]
            d += 1
            q = next_q
        return dists

    start = (0, 0)
    end = (w-1, h-1)
    s_dists = dist_map(start)
    e_dists = dist_map(end)

    min_d = w*h
    if end in s_dists:
        min_d = s_dists[end]
        assert s_dists[end] == e_dists[start]

    for i in range(w):
        for j in range(h):
            if map[i][j] == 0:
                continue
            ns = neighbors((i,j))
            s_ds = [s_dists[n] for n in ns if n in s_dists]
            e_ds = [e_dists[n] for n in ns if n in e_dists]
            if not s_ds or not e_ds:
                continue
            tot_dist = min(s_ds) + min(e_ds) + 1
            if tot_dist < min_d:
                min_d = tot_dist
    return min_d



# 




test_m1 = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
test_m2 = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(test_m1))
print(solution(test_m2))