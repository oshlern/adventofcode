import math
from random import randint, randrange
from functools import cache
from collections import defaultdict

def pisano_period(n):
    return math.lcm(*[pi**(ki-1) * pisano_period_p(pi) for pi,ki in prime_factorisation(n).items()])

@cache
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
    print("N:", n)
#     F = []
    F = defaultdict(int)
    for p in base_ps:
        while n%p == 0:
            n //= p
            F[p] += 1
    print("--- Factored base_ps.")
    print("F:", F)
    k = out_of_base[1]
    i = 1
    while k**3 <= n:
        while n%k == 0:
            n //= k
            F[k] += 1
        k += intervals[i]
        i += 1
        if i == len(intervals):
            i = 0
    print("--- Wheel factored to n^1/3. k:", k)
    print("F:", F)

    while n > 1:
        print("Pollard factoring")
        d = pollard_rho(n)
        if not d:
            print("Failed Pollard, trying MR")
            if miller_rabin_ptest(n, 100):
                print("\t prime")
                F[n] += 1
                return F
            else:
                print("\t composite, trying pollard")
                for c in range(2,100):
                    d = pollard_rho(n, c)
                    if d:
                        print("found at c=", c, "d:", d)
                        break
                if not d:
                    print("POLLARD FAILED")
        else:
            n //= d
            F[d] += 1
        print(d)
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
        d = math.gcd(abs(x-y), n)

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
    
#     r, s = s, d

    for _ in range(k):
        a = randint(2, n - 2)  # n is always a probable prime to base 1 and n − 1
        x = a**d % n
        
        for __ in range(s):
            y = x**2 % n
            if y == 1 and x != 1 and x != n - 1: # nontrivial square root of 1 modulo n
                return False
            x = y
        if y != 1:
            return False
    return True
