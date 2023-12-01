# referenced from https://towardsdatascience.com/dodge-the-lasers-fantastic-question-from-googles-hiring-challenge-72363d95fec
from decimal import getcontext, Decimal
getcontext().prec = 100
def solution(n):
    r = Decimal(2).sqrt()
    s = r/(r-1)
    def f(k):
        if k == 0:
            return 0
        max_n = Decimal(int(r*k))
        max_si = int(max_n / s)
        return max_n * (max_n + 1) / 2 - max_si * (max_si + 1) - f(max_si)
    return f(n)

print(solution(77))

# flo
# (1*sqrt(2)) +
# floor(2*sqrt(2)) +
# floor(3*sqrt(2)) +
# floor(4*sqrt(2)) +
# floor(5*sqrt(2))

# = 

# 1*sqrt(2) +
# 2*sqrt(2) +
# 3*sqrt(2) +
# 4*sqrt(2) +
# 5*sqrt(2)

# - 
# (2*sqrt(2)) % 1 +
# (3*sqrt(2)) % 1 +
# (4*sqrt(2)) % 1 +
# (5*sqrt(2)) % 1

# # rational apprixomiation

# # sqrt(2) = a/b

# # sum (i * a/b % 1)
# # sum (i * a % b  / b)
# # sum (i * a % b) / b
# # (sum i * a) % b + Xb / b
# # X

# a = int(sqrt(2) * b)
# sqrt(2) - a/b = sqrt(2) - int(sqrt(2) * b)/b
# = sqrt(2) * b - int(sqrt(2) * b) / b
# = (sqrt(2) * b) % 1 / b < 1/b

# i*sqrt(2) - i*a/b < i/b


# # (sum i) * a % b    /b
# # (n*(n+1)/2 * a % b)/b


# cross 1
# approximate by big fraction

# = 
# n*n+1/2 * sqrt(2)
# -
# sqrt(2) % 1
# (3*sqrt(2)) % 1 = 3 * (sqrt(2) % 1) % 1




def sum()




