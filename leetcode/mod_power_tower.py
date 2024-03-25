def tower(base, h, m):
    factorization = [(p, k)] # m
    
    for p,k in factorization:
        a = base % p
        r = (base // p^ r)
        
        if r:
            if exp >= k/r: 0
        else:
            e = exp % (p-1) * p^(k-1)
            e = CRT(exp % p-1, exp % p^(k-1))
            a ** e % p^k
        b^e2 % p^(k-1)
        b^b^b^b % p^k = 
        b ^ CRT(e1 % (p-1), e1 % p^(k-1))
        b ^ CRT(e2 % (p-1), e2 % p^(k-2))
        e2 % p
        e0 % p^3 = 
        b^ CRT(e1 % (p-1), e1 % p^2)
            b^ CRT(e2 % (p-1), e2 % p)
        b ^ CRT(e1 % p-1, b ^ CRT(e2 % p-1, ))

        e0 %p^1 = b^(e1 % p-1) % p

        e0 %p^2 = b^(e1 % (p-1)p^1) % p^2
                = b^crt(e1 % p-1, e1 % p^1) % p^2
                = b^crt(e1 % p-1, b^(e2 % p-1) % p) % p^2
        
        
        e0 %p^3 = b^e1 % p^3
                = b^(e1 % (p-1)p^2) % p^3
                = b^(crt(e1 % (p-1), e1 % p^2) % p^3
                = b^(crt(e1 % (p-1), e1 % p^2) % p^3

        e0 %p^2 = b^crt(e1 % p-1, b^(e2 % p-1) % p) % p^2
        e0 %p^2 = b^(e1 % p-1, b^(e2 % p-1))
        

def p_tower(base, h, p, k): # b^b^b % p^k
#     [(pi, ki)]= factorize(p - 1)

    out = 0
    for i in range(max(0,k-h), k):
        exp = CRT(tower(b, h-k + i, p-1), p-1, out, p^i)
        out = pow(b, exp, p^(i+1))
                     
    b % p^k
    b^b^b 

                     
        
        out = b ** CRT(tower(b, i, p-1), pow(b,out,p-1))
    b ** CRT(tower(b, h-1, p-1),
    
        
        
        base ^ exp2
        
        
        
        
        k -= 1
        base 

a % p
a^a^a^a^a
 a % p 
a^a = a^(a % p-1)
a^a^a = a^(a^a % p-1)
        
    
    
    
    """Return base ** base ** ... ** base, where the height is h, modulo m. """
    pass

n % 34

n % pi^ki

# split into pi^ki
for relatively prime, just need to find power % phi(n)
ap (a^m % p) * p^m.  a^k p^k = 0
(p-1) * k

base, mod
a * gcd(base, mod)
a * d **exp % m
a ** d % m   * d**exp % m

a * p^r
a ** exp % p  *  p^exp*r if exp*r > k: 0
exp % p-1, exp > k/r

a ** exp % p^r
M = (p-1) * p^(k-1)
exp % M





 
seqs = []
for i in range(10):
    x = 1
    seqs.append([(x:= (x*i)%10) for _ in range(4)])
    
def is_zero(lst):
    i = 0 # counts consequtive zeros
    while i < len(lst) and lst[i] == 0:
        i += 1
    return i % 2

def last_digit(lst, m=10):
    if len(lst) == 0:
        return 1
    b, lst = lst[0], lst[1:]
    if is_zero(lst):                                    # e=0 --> b^e = 1
        return 1
    elif b == 0:
        return 0                                        # b=0 --> b^e = 0

    if m == 10:
        return seqs[b%10][(last_digit(lst, 4)-1)%4] # (b^e)%10 from precomputed period-4 seqs
    elif m == 4:
        match b % 4:                                    # logical casework
            case 0:
                return 0
            case 1:
                return 1
            case 2:                                     # e>1 --> (2^e)%4 = 0
                return 0 if (lst and lst[0] > 1 and not is_zero(lst[1:])) else 2
            case 3:                                     # e%2 determines if (3^e)%4 = 3 or 1
                return 3 if last_digit(lst, 2) else 1
    elif m == 2:
        return b % 2 # (b^e)%2 = (b)%2  note: ruled out e=0 earlier