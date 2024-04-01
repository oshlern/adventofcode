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
    if b == 0:
        return 0                                        # b=0 --> b^e = 0

    if m == 10:
        return seqs[b%10][(last_digit(lst, 4)-1)%4] # (b^e)%10 from precomputed period-4 seqs
    if m == 4:
        match b % 4:                                    # logical casework
            case 0:
                return 0
            case 1:
                return 1
            case 2:                                     # e>1 --> (2^e)%4 = 0
                return 0 if (lst and lst[0] > 1 and not is_zero(lst[1:])) else 2
            case 3:                                     # e%2 determines if (3^e)%4 = 3 or 1
                return 3 if last_digit(lst, 2) else 1
    if m == 2:
        return b % 2                                    # (b^e)%2 = (b)%2  note: ruled out e=0 earlier


# from functools import reduce
# reduce((lambda x1,x2: pow(x2,x1,100)), reversed(lst), 1)

# base = 10

# def gen_pow(i, mod):
#     seq = [] #[1]
#     x = i
#     for idx in range(mod):
#         seq.append(x)
#         x = (x*i)%mod
#         if x == i:
#             pow_b = lambda e, seq=tuple(seq): 1 if e == 0 else seq[(e-1) % len(seq)]
#             return pow_b, idx+1
#         if x == 0:
#             pow_b = lambda e, seq=tuple(seq): 1 if e == 0 else "zero" if e > len(seq) else: seq[e-1]
#             return pow_b, idx+1

        
#         x1 ^ () % 10
        
#         x2^x3 % 4
        

# def gen_seqs(base):
#     seqs = []
#     for i in range(base):
#         seq = [] #[1]
#         x = i
#         for _ in range(base):
#             seq.append(x)
#             x = (x*i)%base
#             if x == i:
#                 break
#             if x == 0:
#                 pow_b = lambda e, seq=tuple(seq): 1 if e == 0 else "zero" if e > len(seq) else: seq[e-1]
#                 break
#     if nozero:
#         pow_b = lambda e, seq=tuple(seq): 1 if e == 0 else seq[(e-1) % len(seq)]
#     if zero:
        
#         seqs.append(seq)
    

#     lens = [len(seq) for seq in seqs]
#     print("base", base, lens)


# 0 0, 1 1,   2 4 8 6 2, 3 9 7 1 3,  4 6 4  5 5   6 6  7 9 3 1 7  8 4 2 6 8  9 1 9
# 0, 1, 2 0, 3 1
# 0 1
# >1

# m^tot(n) %n 
# a^tot(n) * b^tot(n) % n
# b^tot(n) % n
# P pi^(ei*tot(n))


# tot(n) mod k = 1 or 0 ??
# P p^k-1(p-1) % k
# 

# totients = {
#     10: 4,
#     4: 4,
# #     2: 2
# }
# def last_digit_mod(lst, m):
#     if len(lst) == 0:
#         return 1
#     b = lst[0]
#     e = last_digit_mod(lst[1:], totients[m])
    
#     if e == "zero":
#         return 1
#     if b == 0:
#         return "zero"
#     out = pow(b, e, m)
#     if out == 0:
#         out = "zero"
#     print(lst, "b: {}, e: {}, out: {}, m: {}".format(b, e, out, m))
#     return out

# def last_digit_mod2(lst):
#     if len(lst) == 0:
#         return 1
#     i = 0 # counts consequtive zeros
#     while i+1 < len(lst) and lst[i+1] == 0:
#         i += 1
#     if i % 2 == 0: # if exp is not zero
#         return lst[0]%2 if lst[0] else "zero"
#     else:
#         return 1

# def last_digit_mod4(lst):
#     if len(lst) == 0:
#         return 1
#     b = lst[0]
#     e = last_digit_mod2(lst[1:])
#     if e == "zero":
#         return 1
#     if b == 0:
#         return "zero"
#     return pow(b, e, 4)
#     if len(lst)
#     i = 0 # counts consequtive zeros
#     while i+1 < len(lst) and lst[i+1] == 0:
#         i += 1
#     if i % 2 == 0: # if exp is not zero
#         return lst[0]%2 if lst[0] else "zero"
#     else:
#         return 1

# def conseq_0s(lst):
#     i = 0 # counts consequtive zeros after b
#     while i < len(lst) and lst[i] == 0:
#         i += 1
#     return i

# def is_zero(lst):
#     i = 0 # counts consequtive zeros
#     while i < len(lst) and lst[i] == 0:
#         i += 1
#     return i % 2

# def last_digit_mod(lst, m):
#     if len(lst) == 0:
#         return 1
#     b, lst = lst[0], lst[1:]
#     if is_zero(lst):
#         return 1
#     elif b == 0:
#         return 0

#     if m == 10:
#         e = last_digit_mod(lst, 4)
#         x = pow(b, e if e else 4, m)
#         print(b, lst, e4, x)
#         return x
#     elif m == 4:
#         match b % m:
#             case 0:
#                 return 0
#             case 1:
#                 return 1 
#             case 2:
#                 return 0 if lst and lst[0] > 1 and not is_zero(lst[1:]) else 2
#             case 3:
#                 return 3 if last_digit_mod(lst, 2) else 1
#     elif m == 2:
#         return b % m

#     print("FAILED")

# def last_digit(lst):
#     if len(lst) == 0:
#         return 1
#     b = lst[0] % 10
#     e = last_digit_mod(lst[1:], totients[m])
    
#     if e == "zero":
#         return 1
#     if b == 0:
#         return "zero"
#     out = pow(b, e, m)
#     if out == 0:
#         out = "zero"
#     print(lst, "b: {}, e: {}, out: {}, m: {}".format(b, e, out, m))
#     return out

    # return last_digit_mod(lst, 10)
#     if x == "zero":
#         return 0
#     return x

#     if len(lst) == 1:
#         e = 1
#     elif len(lst) == 2:
#         e = lst[1] if lst[1] else "zero"
#     else:
        
#     e = lst[1] if len(lst) > 1 else 1
#     if e == 
    
        
#         b = "zero"
#     if len(lst) == 1:
#         return "zero" if lst[0] == 0 else lst[0] % m
#     if len(lst) == 2:
#         if lst[1] == 0:
#             return 1
#         return pow(lst[0], lst[1], m)
#     else:
#         if m == 10:
#             new_m = 4
#         elif m == 4:
#             new_m = 2
#         elif m == 2:
#             new_m = 2
#         else:
#             assert False, "Unimplemented totient calculations"
#         rest = last_digit_mod(lst[1:], new_m)
#         print(rest)
#         return pow(lst[0], rest, m)

def last_digit(lst):
    x = last_digit_mod(lst, 10)
    if x == "zero":
        return 0
    return x


# seqs = gen_seqs(10)
# seq4s = gen_seqs(4)

print(pow(7,6,10))
print(pow(7,26,10))
print(pow(7,6**21,10))
print(pow(7,(6**21)%4,10))
# print(seqs[7])
# def last_digit(lst):
#     def Pow(b, e):
#         if e == "zero":
#             return 1
#         elif b == "zero":
#             return "zero"
#         seq = seqs[b % base]
#         return seq[(e-1) % len(seq)]
        
#     X= reduce((lambda x1,x2: Pow(x2,x1)), reversed(lst), 1)
#     print(lst)
# #     X = 
    
#     x = 1
#     for l in reversed(lst):
#         x = Pow(l, x)
#         print("x:", x, "l:", l)
#     print(X)
#     return X % 10





    
        
        
        