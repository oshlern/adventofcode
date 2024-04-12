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

# https://www.codewars.com/kata/551f23362ff852e2ab000037/train/python
def longest_slide_down(pyramid):
    s = pyramid.pop()
    for layer in reversed(pyramid):
        s = [n + max(s[i], s[i+1]) for i,n in enumerate(layer)]
    return s[0]

# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python
def is_interesting(number, awesome_phrases):
    if is_special(number,   awesome_phrases): return 2
    if is_special(number+1, awesome_phrases): return 1
    if is_special(number+2, awesome_phrases): return 1
    return 0
def is_special(number, awesome_phrases):
    s = str(number)
    return number > 99 and (
            all(c=="0"  for c in s[1:])
         or all(c==s[0] for c in s[1:])
         or all(s[i:i+2] in "1234567890" for i in range(len(s)-1))
         or all(s[i:i+2] in "9876543210" for i in range(len(s)-1))
         or s == s[::-1] \
         or number in awesome_phrases)

# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python
from collections import Counter
def top_3_words(text):
    T = iter(text.lower())
    counts = Counter()
    valid_chars = "abcdefghijklmnopqrstuvwxyz'"
    try:
        while True:
            word = ""
            while (c := next(T)) in valid_chars:
                word += c
            if word and set(word)!=set("'"):
                counts[word] += 1
                word = ""
    except StopIteration:
        if word and set(word)!=set("'"):
            counts[word] += 1
            word = ""
    return [word for word,count in counts.most_common(3)]

# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
class RomanNumerals:
    symbols = [("M__",1000), ("CDM",100), ("XLC",10), ("IVX",1)]

    @staticmethod
    def to_roman(val : int) -> str:
        out = ""
        for (I,V,X),n in RomanNumerals.symbols:
            a, val = divmod(val, n)
            if a == 10-1:
                out += I+X
            elif a >= 5:
                out += V+I*(a-5)
            elif a == 5-1:
                out += I+V
            else:
                out += I*a
        return out

    @staticmethod
    def from_roman(roman_num : str) -> int:
        out = 0
        for (I,V,X),n in RomanNumerals.symbols:
            if roman_num.startswith(I+X):
                out += (10-1)*n
                roman_num = roman_num[2:]
            if roman_num.startswith(I+V):
                out += (5-1)*n
                roman_num = roman_num[2:]
            if roman_num.startswith(V):
                out += 5*n
                roman_num = roman_num[1:]
            while roman_num.startswith(I):
                out += 1*n
                roman_num = roman_num[1:]
        return out

# https://www.codewars.com/kata/52a382ee44408cea2500074c/train/python
def determinant(matrix):
    return sum((-1)**i * matrix[0][i] * determinant([r[:i]+r[i+1:] for r in matrix[1:]]) for i in range(len(matrix))) if matrix else 1

# https://www.codewars.com/kata/520446778469526ec0000001/train/python
def same_structure_as(A,B):
    return (A_list := type(A)==list) == (B_list := type(B)==list) and (not A_list or len(A) == len(B) and all(same_structure_as(a,b) for a,b in zip(A,B)))

# https://www.codewars.com/kata/5765870e190b1472ec0022a2/train/python
def path_finder(maze):
    maze = maze.split('\n')
    N = len(maze)
    start = (0,0)
    end = (N-1,N-1)
    q = [start]
    seen = set(q)
    while q:
        v = q.pop()
        for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
            n = (v[0]+i,v[1]+j)
            if 0<=n[0]<N and 0<=n[1]<N and n not in seen and maze[n[0]][n[1]] == '.':
                seen.add(n)
                q.append(n)
    return end in seen

# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/train/python
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, r):
        if r < -8 or r == 0 or r > 8:
            raise Exception("rank out of range")
        r, sr = r + (r<0), self.rank + (self.rank<0)
        d = r - sr
        if d == 0:
            progress = 3
        elif d == -1:
            progress = 1
        elif d <= -2:
            progress = 0
        elif d > 0:
            progress = 10*d*d
        r_up, progress = divmod(self.progress+progress, 100)
        sr += r_up
        self.rank = min(sr, 8) - (sr<=0)
        self.progress = 0 if self.rank == 8 else progress

# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python
def next_smaller(n):
    s = str(n)
    for i in range(len(s)-2,-1,-1):
        x = ''.join(sorted(s[i+1:], reverse=True))
        for j in range(len(x)):
            if x[j] < s[i]:
                if i==0 and x[j]=="0": continue
                out = s[:i]+x[j] + x[:j]+s[i]+x[j+1:]
                return int(out)
    return -1

# https://www.codewars.com/kata/52423db9add6f6fc39000354/train/python
def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]: # Game of Life
    for _ in range(generations):
        cells = [[0]+r+[0] for r in cells]
        cells = [[0]*len(cells[0])] + cells + [[0]*len(cells[0])]
        h, w = len(cells), len(cells[0])
        def num_neighbors(i,j):    
            return sum(cells[x][y] for x in range(max(0,i-1), min(h,i+2)) for y in range(max(0,j-1), min(w,j+2)) if (x,y)!=(i,j))
        ns = [[num_neighbors(i,j) for j in range(w)] for i in range(h)]
        cells = [[int((2 if cells[i][j] else 3)<=ns[i][j]<=3) for j in range(w)] for i in range(h)]
    while sum(cells[0]) == 0:
        cells = cells[1:]
    while sum(cells[-1]) == 0:
        cells = cells[:-1]
    while sum(cells[i][0] for i in range(len(cells))) == 0:
        cells = [cells[i][1:] for i in range(len(cells))]
    while sum(cells[i][-1] for i in range(len(cells))) == 0:
        cells = [cells[i][:-1] for i in range(len(cells))]
    return cells

# https://www.codewars.com/kata/546d15cebed2e10334000ed9/train/python
import re
def solve_runes(runes):
    runes = runes.replace('=', "==")
    for i in range(10):
        if str(i) in runes: continue
        s = runes.replace('?',str(i))
        if re.search(r"(^|[^\d])0\d+", s): continue
        if eval(s): return i
    return -1

# https://www.codewars.com/kata/52bef5e3588c56132c0003bc/train/python
def tree_by_levels(node):
    out = []
    level = [node] if node else []
    while level:
        out += [n.value for n in level]
        level = [c for n in level for c in [n.left, n.right] if c]
    return out

# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/train/python
def spiralize(size):
    # Go forward until can't then turn and repeat
    spiral = [[0]*size for _ in range(size)]
    i, j = 0, 0
    steps, rotations = 0, 0
    while True:
        spiral[i][j] = 1
        steps += 1
        if j==size-1 or sum(spiral[i][j+1:j+3]):
            # Turn right (turn board ccw)
            if steps <= 2:
                break
            spiral = list(map(list,zip(*spiral)))[::-1]
            i, j = size-1-j, i
            steps = 0
            rotations += 1
        else:
            j += 1

    # Unrotate
    for _ in range((-rotations)%4):
        spiral = list(map(list,zip(*spiral)))[::-1]        
    return spiral

# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b/train/python
import re
def expand(expr): # binomial expansion
    pattern = r'\((-?\d*)(.)([+-]\d+)\)\^(\d+)'
    a,x,b,n = re.match(pattern, expr).groups()
    a,x,b,n = int(a+"1"*(a in "-")), x, int(b), int(n)
    out = ""
    nCi = 1
    for i in range(n+1):
        c = nCi * a**(n-i) * b**i
        e = n-i
        nCi = (nCi * (n-i)) // (i+1)
        if c:
            out += "+" if c>0 else "-"
            c = abs(c)
            if e:
                if c != 1:
                    out += str(c)
                out += x
                if e != 1:
                    out += "^"+str(e)
            else:
                out += str(c)
            
    if out[0] == '+':
        out = out[1:]
    return out