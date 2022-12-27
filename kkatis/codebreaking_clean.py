import math
import string
import sys
Ls = string.ascii_uppercase + " "
mod = 2**20

def decrypt(m, N, X):
    X_33 = pow(33, X, 32*mod)
    T = (pow(X_33, X, 32*mod * (X_33-1)) - 1) / (X_33 - 1) 
    p10s = [(10**j) for j in range(9)]
    n = 0
    p = 1
    for i in range(X-1,-1,-1):
        s = int((pow(33,i+1,32*mod)* T - X) / 32) % mod
        n += s * p
        p *= p10s[int(math.log(s,10)+1.0000000001) if s else 1]
    max_e = int(math.log(n) / math.log(27))
    p = 27 ** max_e
    o = ""
    for i,mi in enumerate(m):
        coef = int(n // p)
        n -= coef * p
        p = int(p // 27)
        o += Ls[(Ls.index(mi) + coef) % 27]
    return o

N, X = map(int, input().split(" "))
m = input()
print(decrypt(m, N, X))
# N, X = map(int, input().split(" "))
# m = input()
# N, X = map(int, sys.stdin[0].split(" "))
# m = sys.stdin[1]
# N, X=14, 4
# m = "JQ IRKEYFG EXQ"
# N, X=43, 100000
# m = "BLNAMOTPRRNIXRNMPIWHXDZTRQJXRKIAIEEIIPJLGZP"


# import time

# start = time.time()
# o = decrypt(m, N, X)
# print("time", time.time() - start)
# print(o)


