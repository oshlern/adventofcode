# https://www.codewars.com/kata/638b4205f418c4ab857f2692/train/python
import math
from itertools import cycle

base_ps = [2,3,5,7,9,11]
wheel_m = math.prod(base_ps)
h = [j for j in range(wheel_m) if all(j%p!=0 for p in base_ps)]
intervals = [h[i+1]-h[i] for i in range(len(h)-1)] + [h[0]+wheel_m - h[-1]]

def f(m:int) -> int:
    n = 1
    pows = {}

    for i in base_ps:
        if m % i == 0:
            pow = 0
            while m % i == 0:
                m //= i
                pow += 1
            pows[i] = pow
            n *= i

    iter = cycle(intervals)
    i = h[0] + next(iter)
    m_rt3 = math.ceil(m**(1/3))
    while i <= m_rt3:
        if m % i == 0:
            pow = 0
            while m % i == 0:
                m //= i
                pow += 1
            m_rt3 = math.ceil(m**(1/3))
            pows[i] = pow
            n *= i
        i += next(iter)
        
    if m != 1:
        if (m_sq := m**0.5) % 1 == 0:
            pows[m_sq] = 2
            n *= m_sq
            m = 1

    n *= m
    used_pows = {p: 1 for p in pows}
    if not pows: return n
    while True:
        max_exp, max_p = -1, 0
        for p in pows:
            exp = pows[p] / used_pows[p]
            if max_exp < exp:
                max_exp, max_p = exp, p
        max_p = max(pows, key=lambda p: pows[p] / used_pows[p])
        max_exp = pows[max_p] / used_pows[max_p]
        direct_increase = math.ceil(max_exp / n)
        if direct_increase == 1: return n
        # try multiplying by pi
        used_pows[max_p] += 1
        n *= max_p
        next_max_exp = max(pows[p] / used_pows[p] for p in pows)
        p_increase = max_p*math.ceil(next_max_exp / n)
        if direct_increase < p_increase:
            n /= max_p
            n *= direct_increase
            return n
        


# import math
# from itertools import cycle
# import numpy as np

# # base_ps = [2,3,5,7,9,11]
# base_ps = [2,3,5]
# wheel_m = math.prod(base_ps)
# h = [j for j in range(wheel_m) if all(j%p!=0 for p in base_ps)]
# # intervals = [h[i+1]-h[i] for i in range(len(h)-1)] + [h[0]+wheel_m - h[-1]]    
# # H = numpy.array(h)

# def f(m:int) -> int:
#     print(m)
#     n = 1
#     pows = {}

#     for i in base_ps:
#         if m % i == 0:
#             pow = 0
#             while m % i == 0:
#                 m //= i
#                 pow += 1
#             pows[i] = pow
#             n *= i
#     print(pows, m)
# #     iter = cycle(intervals)
# #     i = h[0] + next(iter)
    
#     m_rt3 = math.ceil(m**(1/3))
# #     H = np.array(h, dtype=np.int64)
#     H = np.array(h, dtype=int)
# #     H_mod = H % m
# #     x = np.where(H_mod[1:] == 0)
# #     print(len(x), type(x), H_mod.shape)
# #     for idx in np.where(np.mod(m,H[1:]) == 0)[0]:
# # #         print(idx, H)
# #         i = H[idx+1]
# #         pow = 0
# #         while m % i == 0:
# #             m //= i
# #             pow += 1
# #         m_rt3 = math.ceil(m**(1/3))
# #         pows[i] = pow
# #         n *= i
# #     H += wheel_m
# #     H_mod = np.mod(m, wheel_m)
# #     H_mod %= m
    
#     while H[0] <= m_rt3:
#         for i in H[np.mod(m,H) == 0]:
# #             i = H[idx]
#             if i == 1: continue
#             i = int(i)
#             pow = 0
#             if m % i != 0:
#                 print(m, i, type(m), type(i))
#                 print(m%i)
#             while m % i == 0:
#                 if type(m//i) == np.float64:
#                     print(m)
#                     print(i)
#                     print("before",type(m), type(i))#, type(m//i),m)
#                 m //= i
# #                 print("after",type(m))#, type(i), type(m//i),m)
#                 pow += 1
#             m_rt3 = math.ceil(m**(1/3))
#             pows[i] = pow
#             n *= i
#             print(i, m, pows)
#         H += wheel_m
        
#     if m != 1:
#         if (m_sq := m**0.5) % 1 == 0:
#             pows[m_sq] = 2
#             n *= m_sq
#             m = 1

#     n *= m
#     used_pows = {p: 1 for p in pows}
#     if not pows: return n
#     while True:
#         max_exp, max_p = -1, 0
#         for p in pows:
#             exp = pows[p] / used_pows[p]
#             if max_exp < exp:
#                 max_exp, max_p = exp, p
#         max_p = max(pows, key=lambda p: pows[p] / used_pows[p])
#         max_exp = pows[max_p] / used_pows[max_p]
#         direct_increase = math.ceil(max_exp / n)
#         if direct_increase == 1: return n
#         # try multiplying by pi
#         used_pows[max_p] += 1
#         n *= max_p
#         next_max_exp = max(pows[p] / used_pows[p] for p in pows)
#         p_increase = max_p*math.ceil(next_max_exp / n)
#         if direct_increase < p_increase:
#             n /= max_p
#             n *= direct_increase
#             return n