import sys
import re
# from functools import cache
import functools
import time
filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

p = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

def explore(mats, robs, t):
    # print(robs, mats, t)
    if t == 0:
        # print(robs, mats)
        return mats[-1]
    global costs
    affordable = np.all(np.greater_equal(mats, costs), axis=1)
    mats += robs
    t -= 1
    best = explore(mats, robs, t)
    for i in np.where(affordable)[0]:
        # if t > 10:
        #     print(t, robs, mats, i)
        # print(i, costs.shape, costs[i].shape, mats.shape)
        mats -= costs[i]
        robs[i] += 1
        val = explore(mats, robs, t)
        best = max(best, val)
        mats += costs[i]
        robs[i] -= 1
    mats -= robs
    return best

@functools.cache
def explore_n2(o, c, b, ro, rc, rb, t):
    global ro_o, rc_o, rb_o, rb_c, rg_o, rg_b
    if t == 3:
        if o >= rg_o and b >= rg_b:
            return 2
        if o + ro >= rg_o and b + rb >= rg_b:
            return 1
        else:
            return 0
    no = o + ro
    nc = c + rc
    nb = b + rb
    nt = t - 1
    best = explore_n2(no, nc, nb, ro, rc, rb, nt)
    if o >= ro_o and t - 2 >= ro_o:
        v = explore_n2(no-ro_o, nc, nb, ro+1, rc, rb, nt)
        if best < v:
            best = v
    if o >= rc_o and t >= 5:
        v = explore_n2(no-rc_o, nc, nb, ro, rc+1, rb, nt)
        if best < v:
            best = v
    if o >= rb_o and c >= rb_c:
        v = explore_n2(no-rb_o, nc-rb_c, nb, ro, rc, rb+1, nt)
        if best < v:
            best = v
    if o >= rg_o and b >= rg_b:
        v = explore_n2(no-rg_o, nc, nb-rg_b, ro, rc, rb, nt) + nt
        if best < v:
            best = v
    return best

@functools.cache
def explore_n(o, c, b, ro, rc, rb, t):
    global ro_o, rc_o, rb_o, rb_c, rg_o, rg_b
    if t == 2:
        if o >= rg_o and b >= rg_b:
            return 1
        else:
            return 0
    no = o + ro
    nc = c + rc
    nb = b + rb
    nt = t - 1
    best = explore_n(no, nc, nb, ro, rc, rb, nt)
    if o >= ro_o:
        v = explore_n(no-ro_o, nc, nb, ro+1, rc, rb, nt)
        if best < v:
            best = v
    if o >= rc_o:
        v = explore_n(no-rc_o, nc, nb, ro, rc+1, rb, nt)
        if best < v:
            best = v
    if o >= rb_o and c >= rb_c:
        v = explore_n(no-rb_o, nc-rb_c, nb, ro, rc, rb+1, nt)
        if best < v:
            best = v
    if o >= rg_o and b >= rg_b:
        v = explore_n(no-rg_o, nc, nb-rg_b, ro, rc, rb, nt) + nt
        if best < v:
            best = v
    return best

@functools.cache
def explore_l(o, c, b, g, ro, rc, rb, rg, t):
    if t == 0:
        return g
    global ro_o, rc_o, rb_o, rb_c, rg_o, rg_b
    no = o + ro
    nc = c + rc
    nb = b + rb
    ng = g + rg
    nt = t - 1
    best = explore_l(no, nc, nb, ng, ro, rc, rb, rg, nt)
    if o >= ro_o:
        best = max(best, explore_l(no-ro_o, nc, nb, ng, ro+1, rc, rb, rg, nt))
    if o >= rc_o:
        best = max(best, explore_l(no-rc_o, nc, nb, ng, ro, rc+1, rb, rg, nt))
    if o >= rb_o and c >= rb_c:
        best = max(best, explore_l(no-rb_o, nc-rb_c, nb, ng, ro, rc, rb+1, rg, nt))
    if o >= rg_o and b >= rg_b:
        best = max(best, explore_l(no-rg_o, nc, nb-rg_b, ng, ro, rc, rb, rg+1, nt))
    return best

def explore_L(o, c, b, g, ro, rc, rb, rg, t):
    if t == 0:
        return g
    global ro_o, rc_o, rb_o, rb_c, rg_o, rg_b
    no = o + ro
    nc = c + rc
    nb = b + rb
    ng = g + rg
    nt = t - 1
    best = explore_L(no, nc, nb, ng, ro, rc, rb, rg, nt)
    if o >= ro_o:
        best = max(best, explore_L(no-ro_o, nc, nb, ng, ro+1, rc, rb, rg, nt))
    if o >= rc_o:
        best = max(best, explore_L(no-rc_o, nc, nb, ng, ro, rc+1, rb, rg, nt))
    if o >= rb_o and c >= rb_c:
        best = max(best, explore_L(no-rb_o, nc-rb_c, nb, ng, ro, rc, rb+1, rg, nt))
    if o >= rg_o and b >= rg_b:
        best = max(best, explore_L(no-rg_o, nc, nb-rg_b, ng, ro, rc, rb, rg+1, nt))
    return best

@functools.cache
def explore_l2(o, c, b, g, ro, rc, rb, rg, t):
    if t == 0:
        return g
    global ro_o, rc_o, rb_o, rb_c, rg_o, rg_b
    aff_o = o >= ro_o
    aff_c = o >= rc_o
    aff_b = o >= rb_o and c >= rb_c
    aff_g = o >= rg_o and b >= rg_b

    o += ro
    c += rc
    b += rb
    g += rg
    t -= 1

    best = explore_l2(o, c, b, g, ro, rc, rb, rg, t)
    if aff_o:
        best = max(best, explore_l2(o-ro_o, c, b, g, ro+1, rc, rb, rg, t))
    if aff_c:
        best = max(best, explore_l2(o-rc_o, c, b, g, ro, rc+1, rb, rg, t))
    if aff_b:
        best = max(best, explore_l2(o-rb_o, c-rb_c, b, g, ro, rc, rb+1, rg, t))
    if aff_g:
        best = max(best, explore_l2(o-rg_o, c, b-rg_b, g, ro, rc, rb, rg+1, t))
    return best

tot_q = 0
tot_G = 1
T = 24
o = c = b = g = 0
rc = rb = rg = 0
ll = ll[:3]
T = 32
for i,l in enumerate(ll):
    r = re.search(p, l)
    ro_o = int(r[2])
    rc_o = int(r[3])
    rb_o = int(r[4])
    rb_c = int(r[5])
    rg_o = int(r[6])
    rg_b = int(r[7])
    ro = 1

    start = time.time()
    G = explore_n2(o, c, b, ro, rc, rb, T)
    end = time.time()
    print("{} mark2 collected {} gs in {}s".format(i+1, G, end - start))
    print(explore_n2.cache_info())
    explore_n2.cache_clear()

    # start = time.time()
    # G = explore_n(o, c, b, ro, rc, rb, T)
    # end = time.time()
    # print("{} mark1 collected {} gs in {}s".format(i+1, G, end - start))
    # print(explore_n.cache_info())
    # explore_n.cache_clear()
    q = (i+1) * G
    tot_q += q
    tot_G *= G
print("TOT Q", tot_q)
print("TOT G", tot_G)



# start = time.time()
# G = explore_l2(o, c, b, g, ro, rc, rb, rg, T)
# end = time.time()
# print("l2 collected {} gs in {}s".format(G, end - start))

# import numpy as np

# robs = np.zeros((4,), dtype=int)
# mats = np.zeros((4,), dtype=int)
# costs = np.zeros((4,4), dtype=int)
# robs[0] = 1
# costs[0,0] = int(r[2])
# costs[1,0] = int(r[3])
# costs[2,0] = int(r[4])
# costs[2,1] = int(r[5])
# costs[3,0] = int(r[6])
# costs[3,2] = int(r[7])
# start = time.time()
# g = explore(mats, robs, T)
# end = time.time()
# print("vec collected {} gs in {}s".format(g, end - start))

# print(explore(mats, robs, T))

    
# produce()










# # @memoize
# def update(ss, rs, t):
    
# if ore > c1o:
#     resources[0] -= c1o
#     resources
#     gs = best_geodes(t-1)
#     robots[0] += 1
#     resources[0] -= 1
# # if ore > c1o:
# #     resources[0] -= c1o
# #     resources
# #     gs = best_geodes(t-1)
# #     robots[0] += 1
# #     resources[0] -= 1
# if 


    


# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))
