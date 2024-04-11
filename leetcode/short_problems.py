# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python
# recursive. could add cache
def decompose(n):
    return dec(n*n, n)
def dec(n, lim):
    sqrt = n**0.5
    if sqrt < lim:
        if sqrt % 1 == 0:
            return [int(sqrt)]
        lim = int(sqrt - (sqrt % 1) + 1)
    for xk in range(lim-1,0,-1):
        if (out := dec(n-xk**2, xk)):
            return out + [xk]

# https://www.codewars.com/users/oshlern/completed_solutions
def mystery(n):
    out = 0
    while n:
        o = 1 << n.bit_length()
        n = o - n - 1
        out += o
    return out >> 1
def mystery_inv(n):
    out = 1
    sign = 1
    while n:
        o = 1 << (n.bit_length()-1)
        out += sign * (2*o) - sign * 1
        sign *= -1
        n -= o
    return out - 1
def name_of_mystery():
    return "Gray code"

# https://www.codewars.com/users/oshlern/completed_solutions
import math
def dioph_solver(z_max):
    n_sols = 0
    max_z_sols = []
    for z in range(1,z_max+1):
        z3 = z*z*z        
        z_sols = [[x,int(y),z] for x in range(1,math.ceil(math.sqrt(z3))) \
                  if (y:=math.sqrt((z3-x*x)/3)) % 1 == 0]
        if z_sols:
            n_sols += len(z_sols)
            max_z_sols = z_sols
    return [n_sols, sorted(max_z_sols, key=lambda a: (sum(a),-a[0]))]

# https://www.codewars.com/kata/53d40c1e2f13e331fc000c26
def fib(n):
    """Calculates the nth Fibonacci number"""
    N = abs(n)
    sa, sb = 1, 1
    a,b = 0, 1
    while N:
        if N%2:
            a, b = (sb-sa)*a + sa*b, sa*a + sb*b
        sa, sb = (sb-sa)*sa + sa*sb, sa*sa + sb*sb
        N = N//2

    if n <= 0 and n%2 == 0:
        a = -a
    return a

# https://www.codewars.com/kata/55df87b23ed27f40b90001e5
# N-parasitic numbers ending with N
def calc_special(lastDigit, base):
    i_to_str = [str(i) if i < 10 else chr(ord('A')+i-10) for i in range(base)]
    k, carry = lastDigit, 0
    num = i_to_str[k]
    while (product := k*lastDigit + carry) != lastDigit:
        k, carry = product % base, product // base
        num = i_to_str[k] + num
    return num

# https://www.codewars.com/kata/59eb1e4a0863c7ff7e000008
# Boolean order, satisfiability with parentheses
from functools import cache
@cache
def fn(s, ops):
    if not ops:
        return (s=="f", s=="t")
    out0, out1 = 0, 0
    for i,op in enumerate(ops):
        a0, a1 = fn(s[:i+1], ops[:i])
        b0, b1 = fn(s[i+1:], ops[i+1:])
        match op:
            case '&':
                out0 += a0*b0 + a1*b0 + a0*b1
                out1 += a1*b1
            case '^':
                out0 += a0*b0 + a1*b1
                out1 += a1*b0 + a0*b1
            case '|':
                out0 += a0*b0
                out1 += a1*b0 + a0*b1 + a1*b1
    return out0, out1
def solve(s,ops):
    return fn(s, ops)[1]

# https://www.codewars.com/kata/585894545a8a07255e0002f1
# Screen Locking Patterns
from functools import cache
ds = [(i,j) for i in [-1,0,1] for j in [-1,0,1] if i!=0 or j!=0]
ds = [[3*d0+d1 for d0,d1 in ds if 0<=i//3+2*d0<3 and 0<=i%3+2*d1<3] for i in range(9)]
@cache
def count(i, l, left):
    if l == 1:
        return 1 if i in left else 0
    left = tuple(j for j in left if j != i)
    blocked = set(i+2*d for d in ds[i] if i+d in left)
    return sum(count(j, l-1, left) for j in left if j not in blocked)
def count_patterns_from(firstPoint, length):
    return count(ord(firstPoint)-ord('A'), length, tuple(range(9)))

# https://www.codewars.com/kata/6465e051c6ec5c000f3e67c4
# Count numbers without 5s
def no_5s(a, b):
    if a > b:
        return 0
    an =  cnt(-a  ) if a<0 else -cnt(a-1)
    bn = -cnt(-b-1) if b<0 else  cnt(b  )
    return an + bn
def digitize(a): # a>0
    A = []
    while a > 0:
        d = a%10
        A = [d] + A
        a = (a - d)//10
    return A
def cnt(a): #1-a # a>0
    A = digitize(a)
    tot = 0
    if len(A) == 5:
        a = 10**4
        A = digitize(a)
    for i,d in enumerate(A): #range(1, len(A)+1):
        nd = len(A) - i
        if nd == 1:
            tot += (d-(d>=5))
        else:
            tot += (d-(d>5)) * 9**(nd-2) * 8
        if d == 5:
            break
    if len(A) > 5:
        tot -= 8*9*9*9*8
    k = 0
    while True:
        k+=1
        k5 = k**5
        if k5 > a:
            break
        if k5 % 5 == 0:
            continue
        K = digitize(k5)
        if (5 in K) or (len(K) == 5):
            continue
        tot -= 1
    return tot

# https://www.codewars.com/kata/5412509bd436bd33920011bc
# return masked string
def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]

# https://www.codewars.com/kata/523f5d21c841566fde000009
def array_diff(a, b):
    return [x for x in a if x not in b]

# https://www.codewars.com/kata/514b92a657cdc65150000006
def solution(number):
    if number <= 0:
        return 0
    triangle = lambda n: (n*(n+1))//2
    mults_sum = lambda n, k: k*triangle((number-1)//k)
    return mults_sum(number, 3) + mults_sum(number, 5) - mults_sum(number, 15)

# https://www.codewars.com/kata/5908242330e4f567e90000a3/train/python
from numpy import *
def circleIntersection(a,b,R): t=2*arccos(linalg.norm((a[0]-b[0],a[1]-b[1]))/2/R);return nan_to_num(floor(R**2*(t-sin(t))))

# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
import math
def format_duration(seconds):
    if seconds == 0:
        return "now"
    names = ["years", "days", "hours", "minutes", "seconds"]
    rates = [365, 24, 60, 60, 1]
    n_secs = [math.prod(rates[i:]) for i in range(len(rates))]
    out = []
    for name, n_sec in zip(names, n_secs):
        q, seconds = divmod(seconds, n_sec)
        if q > 0:
            if q == 1:
                name = name[:-1]
            out.append(f"{q} {name}")
    out[-2:] = [" and ".join(out[-2:])]
    out = ", ".join(out)
    return out

# https://www.codewars.com/kata/53f40dff5f9d31b813000774/train/python
def recoverSecret(triplets):
    #   'triplets is a list of triplets from the secrent string. Return the string.'
    out = ""
    while triplets:
        inits, not_inits = set(), set()
        for t in triplets:
            inits.add(t[0])
            not_inits.update(t[1:])
        c = (inits - not_inits).pop()
        triplets = [[l for l in t if l != c] for t in triplets if t != [c]]
        out += c
    return out