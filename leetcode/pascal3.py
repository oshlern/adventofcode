# https://www.codewars.com/kata/5a331ea7ee1aae8f24000175/train/python
def triangle(row):
    inp_row = [0 if c=='R' else 1 if c=='G' else -1 for c in row]
    pascal_row = build_row(len(row)-1)
    out = sum(a*b for a,b in zip(pascal_row, inp_row)) % 3
    return "RGB"[out]

def build_row(n): # pascal triangle, 0-indexed, mod 3, *(-1)^n 
    p = 1
    row = [-1 if n%2 else 1]
    while n >= p:
        d = (n % (3*p)) // p
        n_zeros = p-1 - (n % p)
        match d:
            case 0:
                row = row
            case 1:
                row = row + [0]*n_zeros + row
            case 2:
                row = row + [0]*n_zeros + [-c for c in row] + [0]*n_zeros + row
        p *= 3
    return row

# # len()
# def tr(r, l):
#     l = len(r).bit_length
#     for l in 
#     if l == 1:

# N = n*(n-1)/2
# 3^k
# 0 1
# 2

# 1 2
# 0

# 0 2
# 1

# 0 0 
# 0

# 1 1
# 1

# 2 2
# 2

# 0 1 2
#  2 0
#   1

# 0 1 0
#  2 2
#   2

# 1 1 0
#  1 2
#   0

# 0 1 1
#  2 1
#   0

# 1 1 1
#  1 1
#   1

# 0 1 2 012
#  2 0 102
#   1 201
#    021
# # permutation actors

# # 0 0  0 1  0 2
# #  0    2    1
# # 1 0  1 1  1 2
# #  2    1    0
# # 2 0  2 1  2 2
# #  1    0    2

# out = i % 3
# out = -i-j % 3
# out = i-j+k % 3

# -(-i-j%3) -(-j-k%3) %3
# i + 2j + k % 3

# -(i + 2j + k % 3) - (j + 2k + l % 3) %3
# -i - 3j -3k - l

# i
# 2i + 2j
# 4i + 8j + 4k
# 8i + 24j + 24k + 8l
# -1 -1
# 1+2+1
# (-1*(a+b))^n
# -(1 1)
# 1 2 1
# -(1 3 3 1)
# 1 4 6 4 1

# n = l-1
# nC0 nC1 nC2... nCn
# n!/0!, n!/
# n!/(n-k!)k! % 3
# n*(n-1)*...*(n-k)/1*2*3*...*k

# find n
# RGB to 012   0,1,-1
# out = sum_k=1^n nCk * r[k] %3

# nCk = P niCki
# sum_k0=0^p-1 sum_ki=0^p-1  P niCki * r[k]
# sum_k0=0^p-1 n0Ck0  ... sum_ki=0^p-1 niCki r[k]


# DFS of Lucas theorem
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1

# 1
# 1 1
# 1 2 1
# 1 0 0 1
# 1 1 0 1 1
# 1 2 1 1 2 1
# 1 0 0 2 0 0 1
# 1 1 0 2 2 0 1 1
# 1 2 1 2 1 2 1 2 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 0 0 0 0 0 0 0 1 1
# 1 2 1 0 0 0 0 0 0 1 2 1
# 1 0 0 1 0 0 0 0 0 1 0 0 1
# 1 1 0 1 1 0 0 0 0 1 1 0 1 1
# 1 2 1 1 2 1 0 0 0 1 2 1 1 2 1
# 1 0 0 2 0 0 1 0 0 1 0 0 2 0 0 1
# 1 1 0 2 2 0 1 1 0 1 1 0 2 2 0 1 1
# 1 2 1 2 1 2 1 2 1 1 2 1 2 1 2 1 2 1

# def build_row(N): # N is reverse digit representation
#     d = N.pop()
#     row = build_row(N)
#     if d == 0:
#         out = row
#     if d == 1:
#         out = row + 0s + row
#     if d == 2:
#         out = row + 0s - row + 0s + row

# def build_row(n): # N is reverse digit representation
#     row = [1] # [-1 if n%2]
#     p = 1
#     while n >= p:
#         match (n % (p*3)) // p: # current digit
#             case 0:
#                 row = row
#             case 1:
#                 row = row + [0]*(p-n) + row
#             case 2:
#                 row = row + [0]*(p-n) + [-c for c in row] + [0]*(p-n) + row
#         p *= 3
#     return row
        
        
#     row = build_row(N)
#     if d == 0:
#         out = row
#     if d == 1:
#         out = row + 0s + row
#     if d == 2:
#         out = row + 0s - row + 0s + row
    
    
    

# i,j: i%9, j%9
# i,j: i>9, j<i%9 --> i%9, j
# i,j: i>9, j<i%9 --> i%9, j

# 1 0 0 0 0 0 0 0 0 1
# 1 1 0 0 0 0 0 0 0 1 1

  


# # 0 0 0  0 0 1  0 0 2
# #  0 0    0 2    0 1
# #   0      1      2

# # 0 1 0  0 1 1  0 1 2
# #  2 2    2 1    2 0
# #   2      0      1

# # 0 2 0  0 2 1  0 2 2
# #  1 1    1 0    1 2
# #   1      2      0
# #  ---------
# # 1 0 0  1 0 1  1 0 2
# #  2 0    2 2    2 1
# #   1      2      0

# # 1 1 0  1 1 1  1 1 2
# #  1 2    1 1    1 0
# #   0      1      2

# # 1 2 0  1 2 1  1 2 2
# #  0 1    0 0    0 2
# #   2      0      1
# # ------
# # 2 0 0  2 0 1  2 0 2
# #  1 0    1 2    1 1
# #   2      0      1

# # 2 1 0  2 1 1  2 1 2
# #  0 2    0 1    0 0
# #   1      2      0

# # 2 2 0  2 2 1  2 2 2
# #  2 1    2 0    2 2
# #   0      1      2


# # 0 1 2 2  0 1 0 2  0 0 2
# #  2 0 2    2 2 1   0 1
# #   1 1      2 0
# #    1        1

