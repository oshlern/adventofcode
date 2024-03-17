import math
import functools

def pisano_period(n):
    return math.lcm(*[pi**(ki-1) * pisano_period_p(pi) for pi,ki in prime_factorisation(n)])

@functools.cache
def pisano_period_p(p):
    F1, F2 = 1, 1
    iters = 1
    while not (F1 == 0 and F2 == 1):
        temp = F1
        F1 = F2
        F2 = (F2 + temp) % p
        iters += 1
    return iters

base_ps = [2,3,5,7]#,17,19,23]
w_max = math.prod(base_ps)
out_of_base = [i for i in range(w_max) if all([i%p for p in base_ps])]
intervals = [out_of_base[i] - out_of_base[i-1] for i in range(1,len(out_of_base))]
intervals.append(out_of_base[0] + w_max - out_of_base[-1])
# def wheel_factorisation(n):
def prime_factorisation(n):
    F = []
    for p in base_ps:
        if n%p == 0:
            exp = 1
            n //= p
            while n%p == 0:
                exp += 1
                n //= p
            F.append((p, exp))
    k = out_of_base[1]
    i = 1
#     while k*k <= n:
    while k**3 <= n:
        if n%k == 0:
            exp = 1
            n //= k
            while n%k == 0:
                exp += 1
                n //= k
            F.append((k, exp))
        k += intervals[i]
        i += 1
        if i == len(intervals):
            i = 0
    
    while n > 1:
        d = pollard_rho(n)
        if not d:
            if miller_rabin_ptest(n, 100):
                F.append((n, 1))
                return n
            else:
                for c in range(2,100):
                    d = pollard_rho(n, c)
                    if d:
                        break
        n //= d
        Fs.append(d)
        
            
            
    if n > 1:
        F.append((n, 1))
    return F


# runtime O(n^1/4)
def pollard_rho(n, c=1):
    x = 2
    y = x
    d = 1

    while d == 1:
        x = (x*x + c) % n
        y = (y*y + c) % n
        y = (y*y + c) % n
        d = math.gcd(math.abs(x-y), n)

    if d == n: 
        return False
    return d

    
# Primality test, catches with prob (3/4)^k. Runtime O(k log^3(n))
def miller_rabin_ptest(n, k):
#     let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
    s = 0
    d = n-1
    while not (d & 1):
        d >>= 1
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)  # n is always a probable prime to base 1 and n − 1
        x = a*d % n
        for __ in range(s):
            y = x**2 % n
            if y == 1 and x != 1 and x != n - 1: # nontrivial square root of 1 modulo n
                return False
            x = y
        if y != 1:
            return False
    return True
