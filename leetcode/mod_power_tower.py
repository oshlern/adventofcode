# https://www.codewars.com/kata/5a08b22b32b8b96f4700001c/train/python
import math

def tower(b, h, m):
    """Return base ** base ** ... ** base, where the height is h, modulo m. """
    if m == 1: return 0
    if b == 1 or h == 0: return 1
    if h == 1: return b % m
    return CRT([(p_tower(b, h, p, k), p**k) for p,k in factors(m)])

def p_tower(b, h, p, k): # tower(b, h, p^k)
    B = b % (p**k)
    if B <= 1 or h == 1: return B
    if B % p == 0:
        B, r = divide_repeatedly(B, p)
        E = 1
        if any((E:=b**E) * r >= k for i in range(h-1)): return 0
        return pow(B, E, p**(k-E*r)) * p**(E*r)                    # (a * p^r) ^ e % p^k = a^e % p^(k-r*e) * p^(r*e)

    out = 1
    for i in range(max(0,k-h), k):
        exp = CRT([(tower(b, h-k + i, p-1), p-1), (out, p**i)])
        out = pow(b, exp, p**(i+1))
    return out

def factors(m):
    fs = []
    for i in range(2, int(m**0.5)+1):
        m, k = divide_repeatedly(m, i)
        if k: fs.append((i, k))
    if m != 1: fs.append((m, 1))
    return fs

def CRT(bs_ns):
    N = math.prod(n for b,n in bs_ns)
    return sum(b*Beizout(N//n, n)[0]*N//n for b,n in bs_ns) % N

def Beizout(a,b): # find x,y s.t. ax+by=gcd(a,b)
    if b == 0: return 1, 0, a
    q, r = divmod(a,b)
    x, y, g = Beizout(b, r)
    return y, x-y*q, g

def divide_repeatedly(m, p):
    r = 0
    while m % p == 0:
        m //= p
        r += 1
    return m, r
    

# print(Beizout(3,17))
# print(CRT([(1,4),(2,5),(4,7)]))
# print(p_tower(2, 3, 7, 2))
# print(p_tower(2, 3, 2, 10))

#     ax + b(qx+r)
#     (a+bq)x + br = gcd
#     b = b
#     a = a + bq
    #     [(pi, ki)]= factorize(p - 1)

#     pass

# n % 34

# n % pi^ki

# # split into pi^ki
# for relatively prime, just need to find power % phi(n)
# ap (a^m % p) * p^m.  a^k p^k = 0
# (p-1) * k

# base, mod
# a * gcd(base, mod)
# a * d **exp % m
# a ** d % m   * d**exp % m

# a * p^r
# a ** exp % p  *  p^exp*r if exp*r > k: 0
# exp % p-1, exp > k/r

# a ** exp % p^r
# M = (p-1) * p^(k-1)
# exp % M





 
# seqs = []
# for i in range(10):
#     x = 1
#     seqs.append([(x:= (x*i)%10) for _ in range(4)])
    
# def is_zero(lst):
#     i = 0 # counts consequtive zeros
#     while i < len(lst) and lst[i] == 0:
#         i += 1
#     return i % 2

# def last_digit(lst, m=10):
#     if len(lst) == 0:
#         return 1
#     b, lst = lst[0], lst[1:]
#     if is_zero(lst):                                    # e=0 --> b^e = 1
#         return 1
#     elif b == 0:
#         return 0                                        # b=0 --> b^e = 0

#     if m == 10:
#         return seqs[b%10][(last_digit(lst, 4)-1)%4] # (b^e)%10 from precomputed period-4 seqs
#     elif m == 4:
#         match b % 4:                                    # logical casework
#             case 0:
#                 return 0
#             case 1:
#                 return 1
#             case 2:                                     # e>1 --> (2^e)%4 = 0
#                 return 0 if (lst and lst[0] > 1 and not is_zero(lst[1:])) else 2
#             case 3:                                     # e%2 determines if (3^e)%4 = 3 or 1
#                 return 3 if last_digit(lst, 2) else 1
#     elif m == 2:
#         return b % 2 # (b^e)%2 = (b)%2  note: ruled out e=0 earlier


#     2^ 2 % 5^3
#     2^(2 % 4*5^2)
#     2^(2 % 4 -- 2    % 5^2)
#                 2^(1 % 4*5^1)
#                 2^(1 % 4 -- 1 % 5^1)
