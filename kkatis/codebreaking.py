import math
import string
import time
Ls = string.ascii_uppercase + " "
mod = 2**20

def decrypt(m, N, X):
    times = {}
    true_start = time.time()
    start = time.time()
    T = int(((pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X)-1)))
    times["T"] = time.time() - start
    print("__________", math.log(T)/math.log(10))

    col_sums = [int((pow(33,i+1,32*mod)* T - X) / 32) % mod for i in range(X)]
    # col_sums = list(reversed(col_sums))
    print(len(col_sums))

    n_digs10 = [int(math.log(c)/math.log(10))+1 for c in col_sums]
    p10s = [(10**n) for n in n_digs10]


    n = 0
    p = 1
    start = time.time()
    for ni in reversed(col_sums):
        n += int(ni) * p
        p *= pow(10,len(str(ni)))
    times["n"] = time.time() - start
    # c_p10s = []
    # p10 = 1
    # for i,n_digs in enumerate(n_digs10):
    #     c_p10s.append(col_sums[i])
    #     p_10 *= 10 ** n_digs
    sums_ndigs = list(list(x) for x in zip(col_sums, n_digs10))
    OTP_len10 = sum(n_digs10)
    OTP_len = int((OTP_len10-1)/math.log(27))
    digs27 = []
    p27 = 1
    print(OTP_len)
    for i in range(OTP_len):
        p27 *= 27
        p10s_mod_p27 = [(10**j) % p27 for j in range(7)]
        p10 = 1
        coef = 0
        print(i)
        print(col_sums)
        print(n)
        # printsums_ndigs)
        mod27s = [col_sums[i] % 27 for i in range(len(col_sums))]
        # for x in (sums_ndigs):
        for i in reversed(range(len(col_sums))):
            # ,c in enumerate(col_sums):
            coef = (coef + (mod27s[i] * p10)) % 27
            p10 = (p10 * p10s_mod_p27[n_digs10[i]]) % 27
        remainder = 0
        for i in range(len(col_sums)):
            remainder = remainder * p10s[i]
            x = col_sums[i] + remainder
            col_sums[i] = x// 27
            # if col_sums[i] > p10s[i]:
            #     # print("AA__", i, p10s[i], col_sums[i], remainder*27, remainder-next_remainder)
            #     col_sums[i-1] += 1
            #     col_sums[i] -= p10s[i]
            # x[0] += remainder - next_remainder
            remainder = x % 27 
            # print(remainder, mod27s[i])
            # x[0] = int(x[0] // 27)
            # x[1] = int(x[1] // 27)
        # print("coef", Ls[coef], coef, n %27)
        # print((n - col_sums[-1])//27, col_sums[-1]//27)
        n =int(n //27)

        digs27.append(coef)
    dig27 = ""
    for coef in reversed(digs27):
        dig27 += Ls[coef]
    print(dig27)
    print("*"*30)
    
    n = 0
    p = 1
    start = time.time()
    for ni in reversed(col_sums):
        n += int(ni) * p
        p *= pow(10,len(str(ni)))
    times["n"] = time.time() - start
    start = time.time()
    # OTP_len = int(math.log(n) / math.log(27))
    print(OTP_len, len(m))
    n = n // (27 ** max(0,OTP_len - (len(m)+2)))
    times["shortened"] = time.time() - start
    start = time.time()

    max_e = int(math.log(n) / math.log(27))
    print("exp", max_e)
    p = 27 ** max_e
    dig27 = ""
    for e in range(max_e, -1, -1):
        coef = int(n // p)
        n -= coef * p
        p = int(p // 27)
        dig27 += Ls[coef]
    print(dig27)

    o = ""
    for i,mi in enumerate(m):
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

# X = 4
# print(fn(0, X), fn(0, X+1))
# for i in range(1):
#     print("IIII", i)
#     [print(fn(0, X*i + j)) for j in range(X)]
# X = 50000
print(decrypt(m, N, X))
