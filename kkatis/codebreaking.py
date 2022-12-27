import math
import string
import time
Ls = string.ascii_uppercase + " "
mod = 2**20

def decrypt(m, N, X):
    times = {}
    true_start = time.time()
    # start = time.time()
    # X_33 = pow(33, X, 32*mod)
    # T = 1
    # p = 1
    # for i in range(X-1):
    #     p = (p * X_33) % (32 *mod)
    #     T = (T+p)% (32 *mod)
    # times["T"] = time.time() - start

    # start = time.time()
    # X_33 = pow(33, X, 32*mod)
    # T3 = sum(pow(X_33, i, 32*mod) for i in range(X))
    # times["T3"] = time.time() - start

    # start = time.time()
    # X_33 = pow(33, X, 32*mod)
    # T4 = (pow(X_33, X, 32*mod * (X_33-1)) - 1) / (X_33 - 1) 
    # times["T4"] = time.time() - start

    # start = time.time()
    # T2 = int(((pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X)-1))) % (32*mod)
    # times["T2"] = time.time() - start
    # print(times)
    # print(T == T2, T == T3, T3 == T2, T == T4)
    # print(T - T2, T - T3, T3 - T2, T- T4, T3-T4)
    # pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X)-1))
    # 33^X*X / (33^X-1) 
    # 33^X*X / 33^X * 33^X /(33^X-1) 
    # 33^X*(X-1) * (1 + 1 /(33^X-1) 
    # 33^X*(X-1) /(33^X-1)  + 33^X*(X-1)
    # 33^X*(X-1) / 33^X * 33^X  /(33^X-1)  + 33^X*(X-1)
    # 33^X*(X-2) * (1 + 1 /(33^X-1))   + 33^X*(X-1)
    # 33^X*(X-2)  /(33^X-1) + 33^X*(X-2) + 33^X*(X-1)
    # 33^X*(X-n)  /(33^X-1) + 33^X*(X-n) + 33^X*(X-2) + 33^X*(X-1)

    # 33^X*X / (33^X-1) * 33^X+1/33^X+1 
    # 33^X*X / (33^2X-1)  * 33^X+1
    # 33^X*X / (33^X-1) * 33^-X+1/33^-X+1 
    # 33^X*X / (33^X-33^-X)  * 33^-X+1

    # 33^i * 33^X*X / (33^X-1) - X / 32
    # 33^i * 33^X*X / (33^X-1) - X / 32
    # X^2 * log(33) - log(33^X - 1)
    # 
    start = time.time()
    X_33 = pow(33, X, 32*mod)
    T = (pow(X_33, X, 32*mod * (X_33-1)) - 1) / (X_33 - 1) 
    times["T"] = time.time() - start
    # print("__________", math.log(T)/math.log(10))
    # start = time.time()
    # col_sums = [int((pow(33,i+1,32*mod)* T - X) / 32) % mod for i in range(X)]
    # col_sums = list(reversed(col_sums))
    # print(len(col_sums))
    print("*"*30)
    
    n = 0
    p = 1

    # col_sums = [ % mod for i in range(X)]

    # for ni in reversed(col_sums):
    # ss = [int((pow(33,i+1,32*mod)* T - X) / 32) % mod for i in range(X,-1,-1)]

    p10s = [(10**j) for j in range(9)]
    for i in range(X-1,-1,-1):
        # s = int((pow(33,i+1,32*mod)* T - X) / 32)
        s = int((pow(33,i+1,32*mod)* T - X) / 32) % mod
        n += s * p
        # p *= pow(10,len(str(s)))
        # print(s)
        p *= p10s[int(math.log(s,10)+0.0000000001) if s else 1]
        # x =  int((math.log(s,10))+0.00000001)+1 if s else 1
        # if p10s[x] != 10**len(str(s)):
        #     print(x, len(str(s)), s, math.log(s,10))
        # print()
    times["n"] = time.time() - start
    # start = time.time()
    # OTP_len = int(math.log(n) / math.log(27))
    # print(OTP_len, len(m))
    # n = n // (27 ** max(0,OTP_len - (len(m)+2)))
    # times["shortened"] = time.time() - start
    start = time.time()

    max_e = int(math.log(n) / math.log(27))
    print("exp", max_e)
    p = 27 ** max_e
    dig27 = ""
    # e = max_e
    for _ in range(len(m)):
        coef = int(n // p)
        dig27 += Ls[coef]
        n -= coef * p
        p = int(p // 27)

    # p27 = p
    # for _ in range(len(m)):
    #     coef = int(n // p)
    #     dig27 += Ls[coef]
    #     n -= coef * p
    #     p = int(p // 27)

    #     #  27
    #     p10s_mod_p27 = [(10**j) % p27 for j in range(8)]
    #     p10 = 1
    #     coef = 0
        
    #     # print(mod27s)
    #     # print(n)
    #     # printsums_ndigs)
    #     mod27s = [col_sums[i] % 27 for i in range(len(col_sums))]
    #     # for x in (sums_ndigs):
    #     for i in reversed(range(len(col_sums))):
    #         # ,c in enumerate(col_sums):
    #         coef = (coef + (mod27s[i] * p10)) % 27
    #         # if i >= len(n_digs10):
    #         #     print("X", i, len(n_digs10))
    #         # elif n_digs10[i] >= len(p10s_mod_p27):
    #         #     print("Z", n_digs10[i], len(p10s_mod_p27))
    #         p10 = (p10 * p10s_mod_p27[n_digs10[i]]) % 27
    #     remainder = 0
    #     for i in range(len(col_sums)):
    #         remainder = remainder * p10s[i]
    #         x = col_sums[i] + remainder
    #         col_sums[i] = x// 27
    #         remainder = x % 27
    #     if col_sums[0] == 0:
    #         col_sums.pop(0)
    #         n_digs10.pop(0)
    #         p10s.pop(0)

    # for e in range(max_e, -1, -1):
    #     coef = int(n // p)
    #     n -= coef * p
    #     p = int(p // 27)
    #     dig27 += Ls[coef]
    print(dig27)

    o = ""
    for i,mi in enumerate(m):
        # print(mi, dig27[i], Ls)
        o += Ls[(Ls.index(mi) + Ls.index(dig27[i])) % 27]
    times["conversion"] = time.time() - start
    times["Total"] = time.time() -true_start
    for ti in times:
        print(ti, times[ti])
    return o
# m = "THIS IS A TEST"
# N, X = map(int, input().split(" "))
# m = input()
N, X=14, 4
m = "JQ IRKEYFG EXQ"
N, X=43, 100000
m = "BLNAMOTPRRNIXRNMPIWHXDZTRQJXRKIAIEEIIPJLGZP"

# X = 4
# print(fn(0, X), fn(0, X+1))
# for i in range(1):
#     print("IIII", i)
#     [print(fn(0, X*i + j)) for j in range(X)]
# X = 50000
print(decrypt(m, N, X))
