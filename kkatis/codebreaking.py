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
    # (pow(33, i, mod) (1 + ) + pow(33, X, mod) + pow(33, 2X, mod) + ... i + X*(X-1)) - X/32
    # 1 + (1- pow(33, i, mod))/-32 (1 + ) + pow(33, X, mod) + pow(33, 2X, mod) + ... i + X*(X-1)) - X/32
    # 
# for i in sys.stdin:
#     ab = i.split()
#     a = int(ab[0])
#     b = int(ab[1])
def decrypt(m, N, X):
    # X = 4
    # clipped_X = round(((1+len(m)) * math.log(27)/math.log(10)) / 6)
    # clipped_X = round(((1+len(m)) * 2) / 6)
    # print(len(m), X, clipped_X)
    # col_sums = [0 for _ in range(clipped_X)]
    # big_mod = mod * 32
    # X_33 = pow(33, X, big_mod)
                        # 1
    # row_multiplier = int((pow(33, X+1, mod*32)-1)/32)
    # row_multiplier = int((pow(33, 2*(X+1), mod*32)-1)/32)
    # row_multiplier = int((pow(33, i*(X+1), mod*32)-1)/32)

        # r^1-1/r-1
        # r^X+1-1/r-1
        # r^iX+1) - 1 /r-1

        # -X/32
        # (r^X+1)^X - 1 / ((r^X+1)-1) - X )/ r-1


        # r^i-1/r-1
        # r^X+i-1/r-1
        # r^iX+i) - 1 /r-1

        # -X/32
        # (r^X+1)^X - 1 / ((r^X+1)-1) - X )/ r-1
    # row_mult_sum =  (r^X+1)^X - 1 / ((r^X+1)-1)
    # X_33 = pow(33, X+1, mod*32)
    # X_33 = pow(33, X+1, mod)
    # X_33 = pow(33, X+1)
    # row_mult_sum =  (r^X+1)^X - 1 / ((r^X+1)-1)
    # col_sum = (int((pow(X_33, X, mod * ((32 * (X_33 - 1)) % mod)) - 1) / (X_33-1) % mod) - X) / 32
    # col_sum = (((pow(X_33, X) - 1) / (X_33-1) - X) / 32) % mod
    # col_sum = (sum([(pow(33,i*X+1) - 1) for i in range(X)])/32) % mod
    # print()
    # print([i*X+1 for i in range(X)])
    # print("COL", col_sum)

    # -X*32
    # print(row_multiplier)
    # col_sum =  int((pow(row_multiplier, X, mod * ((row_multiplier - 1) % mod)) - 1) / (row_multiplier-1) % mod)
    # print(sum([row_multiplier**i for i in range(X)]) % mod)
    # x = [int((33*pow(33,i*X) - 1)/32) % mod for i in range(X)]
    # x = [((33*pow(33,i*X) - 1)/32) % mod for i in range(X)]
    # print(x)
    # print(sum(x) % mod)

    # X = 4
    # print(X)
    # print(((33*sum([pow(33,i*X,32*mod)  for i in range(X)]) - X)/32) % mod)
    # print(((sum([33*pow(33,i*X,32*mod) -1 for i in range(X)]))/32) % mod)
    # print(((sum([33*pow(33,i*X,32*mod)  for i in range(X)])-X)/32) % mod)
    # print("-"*20)
    # print(((33*sum([pow(33,i*X,32*mod)  for i in range(X)])-X)/32) % mod)
    # # print(((33*sum([pow(33,i*X,32*mod)  for i in range(X)])-X)/32) % mod)
    # r = pow(33,X)#,32*mod)
    # # r^X-1/r-1
    # print((((33*sum([pow(33,i*X,32*mod)  for i in range(X)])-X) % (32*mod)) /32 )% mod)

    # print("a"*20)
    # print(32**X< mod, 33**X, mod)
    # print(sum([pow(33,i*X,32*mod)  for i in range(X)]) % (32*mod))
    # t = ((pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X)-1))
    # # t = ((pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X,32*mod)-1))
    # print(t)
    # print("b"*20)

    # print(clipped_X)
    T = int(((pow(33,X*X, 32*mod * (pow(33,X)-1))-1)/(pow(33,X)-1)))
    print("TEST")
    # col_sum = ((33* T - X) / 32) % mod


    # print(sum([((33*pow(33,i*X) - 1)/32) for i in range(X)]) % mod)
    # print(sum([((33*pow(33,i*X) - 1)/32) % mod for i in range(X)]))
    # print(sum([((33*pow(33,i*X) - 1)/32)for i in range(X)]) % mod )
    # x = [((33*pow(33,i*X,32*mod) - 1)/32)for i in range(X)]
    # print(sum([x%mod for x in x]))
    # print(sum([x for x in x])%mod)

    # print(sum([int((33*pow(33,i*X) - 1)/32) % mod for i in range(X)]))

    # print([xi % mod for xi in x])
    # print([row_multiplier**i % mod for i in range(X)])
    # print(col_sum)
    print("__________")

    # print(X_33)

    # col_sum = X_33 * int((pow(X_33, X, mod * ((X_33 - 1) % mod)) - 1) / (X_33-1) % mod) - X/32
    # col_sum = int((pow(33, X*X, big_mod)-1) / 32)
    # print(col_sum)
    # print(X, X_33, col_sum, (1-X_33)/(1-33))
    # print(sum([33**i for i in range(X)]), (33**X-1 ) / 32, (X_33-1)/32)
    # print(33**X, pow(33, X, mod), 33**X % mod)
    # print(mod)
    col_sums = [int((pow(33,i+1,32*mod)* T - X) / 32) % mod for i in range(X)]
    # print(col_sums)
    # col_sums = [0 for _ in range(clipped_X)]
    # fi = 1
    # for i in range(X*X):
    #     if (i % X) < clipped_X:
    #         col_sums[i % X] = (col_sums[i%X] +  fi) % mod
    #     # fi = int((1 - pow(33, n, mod)) // (1-33))
    #     fi = (33*fi + 1) % mod
    # print(col_sums[:clipped_X])
    # print(len(m), clipped_X)
    # print(col_sums)
    n = 0
    p = 1
    for ni in reversed(col_sums):
        n += int(ni) * p
        p *= pow(10,len(str(ni)))
    # print(n)
    # n = int("".join([str(n) for n in col_sums]))
    # print(n)
    # print(n)
    # dig27 = []
    OTP_len = int(math.log(n) / math.log(27))
    # max_e = int(math.log(n) / math.log(27))
    print(OTP_len, len(m))
    n = n // (27 ** max(0,OTP_len - (len(m)+2)))
# for _ in range(max_e -(len(m)+3)):
#     n2 = int(n2 //27)
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

# for e in range(max_e, -1, -1):
#     if (e % 1000)==0:
#         print(e)
#     coef = int(n // p)
#     n -= coef * p
#     p = p // 27
#     dig27 += Ls[coef]

    o = ""
    for i,mi in enumerate(m):
        o += Ls[(Ls.index(mi) + Ls.index(dig27[i])) % 27]
    return o
# m = "THIS IS A TEST"
N, X = map(int, input().split(" "))
m = input()
# X = 4
# print(fn(0, X), fn(0, X+1))
# for i in range(1):
#     print("IIII", i)
#     [print(fn(0, X*i + j)) for j in range(X)]
# X = 50000
print(decrypt(m, N, X))
