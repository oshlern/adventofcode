# https://www.codewars.com/kata/638b4205f418c4ab857f2692/train/python

import math

import math

def f(m:int) -> int:
    print(m)
    out = 1
    pows = {}
    pow_k = 1
    
    i = 2
    m, m_rt3, pow, cube_steps = decrement_and_rt3(m, i)
    if pow:
        pows[i] = pow
        out *= i
    pow_k *= 3**cube_steps
    i = 3
    while i <= m_rt3:
        if m % i == 0:
            m, m_rt3, pow, cube_steps = decrement_and_rt3(m, i)
            pows[i] = pow * pow_k
            out *= i
            pow_k *= 3**cube_steps
        i += 2
    if m != 1:
        if (m_sq := m**0.5) % 1 == 0:
            out *= m_sq
            pows[m_sq] = 2*pow_k
            m = 1

    out *= m

    
    if pows:
        pi, max_pow = max(pows.items(), key=lambda x: x[1])
        if out < max_pow:
            while math.ceil(max_pow / out) > pi:
                pows[pi**2] = math.ceil(pows[pi]/2)
                del pows[pi]
                pi, max_pow = max(pows.items(), key=lambda x: x[1])

            out *= math.ceil(max_pow / out)
    print(out)
    return out

def decrement_and_rt3(m, i):
    pow = 0
    while m % i == 0:
        m //= i
        pow += 1
    cube_steps = 0
    if m != 1:
        while (m_rt3 := m**(1/3)) % 1 == 0:
            m = int(m_rt3)
            cube_steps += 1
    else:
        m_rt3  = 1
    return m, m_rt3, pow, cube_steps


# def f(m:int) -> int:
#     M = m
#     # Your Code Here
#     out = 1
# #     return 0

#     max_pow = 0
#     pow_k = 1
#     if m % 2 == 0:
#         while m % 2 == 0:
#             m //= 2
#             pow += 1
#     m_cube_root_floored = floor(m**(1/3))
#     while i < m_cube_root_floored:
#         if m % i == 0:
#             m //= i
#             pow = pow_k
#             while m % i == 0:
#                 m //= i
#                 pow += pow_k
#             if pow > max_pow:
#                 max_pow = pow

#             out *= i

#             m_cube_root = m**(1/3)
#             while m_cube_root % 1  == 0:
#                 m = m_cube_root
#                 m_cube_root = m**(1/3)
#                 pow_k *= 3
#             m_cube_root_floored = floor(m_cube_root)
#         i += 2
#     m_sq = m**(1/2)
#     if m_sq % 1 == 0:
#         out *= m_sq
#         pow = 2*pow_k
#         if pow > max_pow:
#             max_pow = pow
#         m = 1

#     out *= m
    
#     if out < max_pow:
#         out *= math.ceil(max_pow / out)
    
#     return out
#     i += 2
# if m**(1/3)
# m = P pi^ki
# n = pj ^ kj n
# kj>=ki
# max(ki)
# P pi
# if max(ki) > P pi
# *= ceil(max(ki) / P pi)
# multiply by 2 until 

# k^k == 0 % m
# k+1
# k^(k-1) * k == mg
# a Ppi, b Ppi

# p^2 = 

# n, no factors < m
# p^2*q 