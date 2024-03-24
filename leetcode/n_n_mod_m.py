# https://www.codewars.com/kata/638b4205f418c4ab857f2692/train/python
import math

def f(m:int) -> int:
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
    i = 3
    while i <= m_rt3:
        if m % i == 0:
            pow = 0
            while m % i == 0:
                m //= i
                pow += 1
            m_rt3 = math.ceil(m**(1/3))
            pows[i] = pow
            n *= i
        i += 2
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
        max_exp = pows[p] / used_pows[p]
        direct_increase = math.ceil(max_exp / n)
        if direct_increase == 1: return n
        # try multiplying by pi
        used_pows[max_p] += 1
        n *= max_p
        next_max_exp = max(pows[p] / used_pows[p] for p in pows)
        p_increase = max_p*math.ceil(next_max_exp / n)
        print(max_p, p_increase, direct_increase)
        if direct_increase < p_increase:
            n /= max_p
            n *= direct_increase
            return n