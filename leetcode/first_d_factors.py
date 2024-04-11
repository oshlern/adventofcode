# https://www.codewars.com/kata/638af78312eae9a23c9ec5d6/train/python

import bisect

class Primes:
    def __init__(self):
        self.ps = [2,3]

    def __getitem__(self, i):
        if i >= len(self.ps):
            self.generate_to(i)
        return self.ps[i]
    
    def generate_to(self, i):
        k = self.ps[-1] 
        while len(self.ps) <= i:
            k += 2
            for p in self.ps:
                if k % p == 0:
                    break
                if p*p > k:
                    self.ps.append(k)
                    break

    def smallest_factors(self, n):
        fs = []
        for i in range(n):
            p = self[i]
            if p*p > n:
                break
            while n % p == 0:
                fs.append(p)
                n //= p
        if n > 1:
            fs.append(n)
        return fs

    def to_power_of(self, fs):
        out = 1
        for i,f in enumerate(fs):
            out *= self[i] ** (f-1)
        return out

P = Primes()
def f(d:int) -> int:
    fs = list(reversed(P.smallest_factors(d)))
    out = P.to_power_of(fs)
    out_fs = fs
    while True: # merge pair of exponents that leads to smallest number
        for i in range(len(fs)-1):
            for j in range(i+1,len(fs)):
                new_fs = fs[:i] + fs[i+1:j] + fs[j+1:]
                bisect.insort(new_fs, fs[i]*fs[j], key=lambda x: -x)
                if (v := P.to_power_of(new_fs)) < out:
                    out = v
                    out_fs = new_fs
        if fs == out_fs: # no merge decreases out
            break
        fs = out_fs
    return out