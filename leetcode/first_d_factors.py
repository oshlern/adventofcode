# https://www.codewars.com/kata/638af78312eae9a23c9ec5d6/train/python

# from collections import defaultdict
#     1, 2, 5, 10
#     2^k * 5^l
#    (k+1) * (l+1)
def f(d:int) -> int:
    fs = reversed(prime_factors(d))
    ps = get_primes()
    out = 1
    print(d)
    print(prime_factors(d))
    Fs = {}
    p = next(ps)
    for f in fs:
        print(p, f-1)
        k = p**(f-1)
        for P,F in Fs.items():
            F*last_F
            for i in range(len(Fs)):
                if new_F < 
            if P**(F*(f-1)) < k:
#                 k = P**(F*(f-1))
                out *= P**(F*(f-1))
                Fs[P] = F*f
                print("  ", p, F*f, F, f)
                break
        else:
            Fs[p] = f
            out *= k
            p = next(ps)
            
#         min()
#         K
#         out *= 
#         if P**(F*(f-1)) < p**(f-1):
    print(Fs)
    print(out)
    return out
# 840/5/2/2/2/3/7 11 or 2^(2*(2-1))
# 2^i*j-1

def prime_factors(n):
    fs = []
    p = 2
    while n%p == 0:
        fs.append(p)
        n //= p
    p += 1
    while p*p <= n:
        while n%p == 0:
            fs.append(p)
            n //= p
        p += 2
    if n != 1:
        fs.append(n)
    return fs

def get_primes():
    yield 2
    p = 3
    while True:
        if len(prime_factors(p)) == 1:
            yield p
        p += 2


# def prime_factors(n):
#     fs = defaultdict(int)
#     p = 2
#     while n%p == 0:
#         fs[p] += 1
#         n //= p
#     p += 1
#     while p*p <= n:
#         while n%p == 0:
#             fs[p] += 1
#             n //= p
#         p += 2
#     if n != 1:
#         fs[n] += 1
#     return fs


# primes = [2]
# for p in range(3,1000,2):
#     if len(prime_factors)