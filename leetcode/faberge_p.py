# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/train/python
MOD = 998244353
p = MOD
def height(n, m):
    print(n, m)
    if n >= m: return pow(2, m, p) - 1
    if n > m//2:
        return (pow(2, m, p) - height(m-n-1, m) - 2) % p
    out = 0
    c = 1
    c_p = 0
    num = m+1
    denom = 0
    x, y = 0, 0
    m2 = m//2 + m%2
    
#         total sum - (m-n)
#         m2 + n-m2
        
    for i in range(1,n+1):
        num -= 1
        denom += 1
#         if num % p == 0:
#             c_p += num // p
#         else:
        c = c * num
        c, r = divmod(c, denom)
        if r != 0:
            x += 1
            c += (pow(denom, p-2, p) * r) #% p
        else:
            y += 1
#         else:
        if c >= p:
            c = c % p
                
        
#         c = (c * num * pow(denom, p-2, p)) % p
#             num = (num * num) % M
#         if denom % p == 0:
#             c_p -= denom // p
#         else:
#         c = (c * pow(denom, p-2, p)) % p
#             c = (c * inv(denom, M)) % M
#             denom = (denom * denom) % M
        
#         if c_p == 0:
        out = (out + c) % p
            
#         out
#             c = 0
#         else:
#             c = (c * num * inv(denom, M)) % M
#         c = (c * (m-i+1)) // i
# #         m_fac *= (m-i+1)
# #         i_fac *= i
# #         out += m_fac // i_fac
#         c = choose_mod(m, i, MOD)
#         out = (out + c) % MOD
#     print(m, n)
    return out % p