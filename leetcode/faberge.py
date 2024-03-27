# https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/train/python
def height(n,m):
    c = 1
    return sum([c:=(c * (m-i)) // (i+1) for i in range(n)])

# def height(n,m):
# #     if m == 0 or n == 0:
# #         return 0
# #     return height(n-1, m-1) + 1 + height(n, m-1)

# #     H = [0 for _ in range(n+1)]
# #     for x in range(m):
# #         print(x, H)
# #         last = H[0]
# #         for i in range(1,n+1):
# #             last, H[i] = H[i], last + 1 + H[i]
# #         print(x, H)
# #     print(n,m)
# #     return H[-1]
#     if n >= m: return 2**m - 1
#     m_fac = 1
#     i_fac = 1
#     out = 0
#     c = 1
#     for i in range(1,n+1):
#         c = (c * (m-i+1)) // i
# #         m_fac *= (m-i+1)
# #         i_fac *= i
# #         out += m_fac // i_fac
#         out += c
#     print(n,m,out)
#     return out