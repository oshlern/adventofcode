def maximize_earnings(earnings,k):
    ms = [0] * (k+1)
    for e in earnings:
        ms = [max(ms)] + [m + e for m in ms[:-1]]
    return max(ms)




# import functools

# def maximize_earnings(earnings,k):
#     return me(earnings, k, 0)

# @functools.cache
# def me(earnings, k, d):
#     if d + len(earnings) <= k:
#         return sum(earnings)
#     return min(me(earnings[1:], k, 0), me(earnings[1:], k, d+1) + earnings[0])


