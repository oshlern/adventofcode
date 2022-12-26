import math
import string
Ls = string.ascii_uppercase + " "
mod = 2**20

def fn(x, n):
    o = 0
    # coef = pow(33, n, mod)
    # coef = 1
    # comb_c = 1
    # xp = 1
    # for i in range(n+1):
    #     o += (coef * comb_c * xp) % mod
    #     comb_c = int(comb_c * (n-i) / (i+1) ) % mod
    #     coef = (coef * 33) % mod
    #     xp = (xp * x) % mod
    #     print(i, coef, comb_c, coef * comb_c * xp)
    # return o
    # return (1 - pow(33, n, mod)) // (1-33)
    (pow(33, i, mod) (1 + ) + pow(33, X, mod) + pow(33, 2X, mod) + ... i + X*(X-1)) - X/32
    (1 - pow(pow(33, X, mod), X, mod)) // (1-pow(33, X, mod))

def decrypt(m):
    clipped_X = round(((1+len(m)) * math.log(27)/math.log(10)) / 6)
    col_sums = [0 for _ in range(clipped_X)]
    fi = 1
    
    for i in range(X*X):
        col_sums[i % X] = (col_sums[i % X] + fi) % mod
        fi = int((1 - pow(33, n, mod)) // (1-33))
        fi = (33*fi + 1) % mod
    # print(col_sums)
    n = int("".join([str(n) for n in col_sums]))
    # print(n)
    # dig27 = []
    dig27 = ""
    max_e = int(math.log(n) / math.log(27))
    p = 27 ** max_e
    for e in range(max_e, -1, -1):
        coef = int(n // p)
        # print(n / p, n // p, int(n//p), e, Ls[coef], p, n)

        # print(coef)
        n -= coef * p
        p = p // 27
        # dig27.append(1)
        dig27 += Ls[coef]
    # print(dig27)

    o = ""
    for i,mi in enumerate(m):
        o += Ls[(Ls.index(mi) + Ls.index(dig27[i])) % 27]
    return o
# m = "THIS IS A TEST"
# N, X = map(int, input().split(" "))
# m = input()
X = 4
print(fn(0, X), fn(0, X+1))
for i in range(1):
    print("IIII", i)
    [print(fn(0, X*i + j)) for j in range(X)]

# print(decrypt(m))
