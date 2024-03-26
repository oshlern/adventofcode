import math

def tower(b, h, m):
    """Return base ** base ** ... ** base, where the height is h, modulo m. """
    if m == 1: return 0
    if b == 1 or h == 0: return 1
    if h == 1: return b % m
    return CRT([(p_tower(b, h, p, k), p**k) for p,k in factors(m)])

def p_tower(b, h, p, k): # b^b^b % p^k
    b = b % (p**k)
    if b == 0: return 0
    if b == 1: return 1
    if h == 1: return b
    if b % p == 0:
        r = 0
        a = b
        while a % p == 0:
            a //= p
            r += 1
#         if r >= k: return 0

        e = b
        if e*r >= k: return 0
        for i in range(h-2):
            e = e**b
            if r*e >= k: return 0
#         t_power = e*r
#         (a * p^r) ^ e % p^k = a^e % p^(k-r*e) * p^(r*e)
        return pow(a, e, p**(k-r*e)) * p**(r*e)
#     k -= e*r
#     M = p ** (r*e)
#     a^b^b^b * M % p^k
#     = a^b^b % p^(k-e*b_k) * M
#     return pow(a, tower(b,h-1,(p-1)*p^(k-1)), p**k)
    

#         r = n_powers(b, p)
#         t = 1
#         for i in range(h):
#             t *= b
#             if t > thresh:
#                 return True
#         if gt_tower(b,h-1,k/r):
#             return 0
#         p *= t
#         a = coprime, 
        
    # coprime part
    out = 0
    for i in range(max(0,k-h), k):
        exp = CRT([(tower(b, h-k + i, p-1), p-1), (out, p**i)])
        print(i, h-k, exp)
        out = pow(b, exp, p**(i+1))
    print("p tower", b, h, p, k, out)
    return out

def gt_tower(b,h,thresh):
    if b <= 1: return b > thresh
    t = 1
    for i in range(h):
        t *= b
        if t > thresh:
            return True
    return False

#     if h == 0:
#         return 1 > thresh
#     else


def factors(m):
    fs = []
    for i in range(2, math.ceil(m**0.5)):
        k = 0
        while m % i == 0:
            print(i,m)
            m //= i
            k += 1
        if k: fs.append((i, k))
    if m != 1: fs.append((m, 1))
    return fs

# def factors(m):
#     return [(p, n_powers(m,p)) for p in range(2,m) if m%p==0]
def n_powers(m, p):
    pow = 0
    while m % p == 0:
        m //= p
        pow += 1
    return pow

# print(factors(120))

def CRT(bs_ns):
    N = math.prod(n for b,n in bs_ns)
    return sum(b*Beizout(N//n, n)[0]*N//n for b,n in bs_ns) % N

def Beizout(a,b): # find x,y s.t. ax+by=gcd(a,b)
    if b == 0: return 1, 0, a
    q, r = divmod(a,b)
    x, y, g = Beizout(b, r)
    return y, x-y*q, g

# print(Beizout(3,17))
# print(CRT([(1,4),(2,5),(4,7)]))
print(p_tower(2, 3, 3, 1))