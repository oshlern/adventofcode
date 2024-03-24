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