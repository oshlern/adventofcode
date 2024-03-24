# https://www.codewars.com/kata/638b4205f418c4ab857f2692/train/python

import math

def f(m:int) -> int:
    print(m)
    n = 1
    pows = {}
    pow_k = 1
    
    i = 2
    if m%i == 0:
        pow = 0
        while m % i == 0:
            m //= i
            pow += 1
        pows[i] = pow
        n *= i
    m_rt3 = math.ceil(m**(1/3))
#     print(m_rt3)
    i = 3
    while i <= m_rt3:
        if m % i == 0:
            pow = 0
            while m % i == 0:
                m //= i
                pow += 1
            m_rt3 = math.ceil(m**(1/3))
            print(m_rt3)
            pows[i] = pow
            n *= i
        i += 2
    if m != 1:
        if (m_sq := m**0.5) % 1 == 0:
            pows[m_sq] = 2
            n *= m_sq
            m = 1

    n *= m
    print(n, pows)
#     over_pows = {p: math.ceil(pows[p] / n)}
#     if over_pows:
#         pi, max_over = max(over_pows.items(), key=lambda x: x[1])
#         n *= pi
#         over_pows[po]
    used_pows = {p: 1 for p in pows}
#     extra_pows = defaultdict(int)
#     if pows:
    while True:
        max_exp, max_p = -1, 0
        for p in pows:
            exp = pows[p] / used_pows[p]
            if max_exp < exp:
                max_exp, max_p = exp, p
        direct_increase = math.ceil(max_exp / n)
        if direct_increase <= 2: return n
        # try multiplying by pi
        used_pows[max_p] += 1
        n *= max_p
        next_max_exp = max(pows[p] / used_pows[p] for p in pows)
        p_increase = p*math.ceil(next_max_exp / n)
        if direct_increase < p_increase:
            n /= max_p
            n *= direct_increase
            return n
#             math.ceil(max_exp / n) * pi > increase:
#             n 
#         used_pows[,]
#         if (pows[p] / (used_pows[p] + 1)
#         print(max_exp, n)
#         if max_exp > max_p * n:
#             n *= max_p
#             used_pows[max_p] += 1
#         else:
#             if max_exp > n:
#                 n *= math.ceil(max_exp / n)
#             return n
            
#         pi, max_pow = max(pows.items(), key=lambda x: x[1] / (1+extra_pows[pi]))
#         if n < max_pow:
#             while math.ceil(max_pow / n) > pi:
#                 n *= pi
#                 extra_pows[pi] += 1
# #                 used_pows 
# #                 pows[pi**2] = math.ceil(pows[pi]/2)
# #                 del pows[pi]
#                 pi, max_pow = max(pows.items(), key=lambda x: x[1])
# #         over_pow = math.ceil(max_pow / out)
#         max_pow/ 
#             out *= math.ceil(max_pow / out)
#     print(out, pows)
#     return out