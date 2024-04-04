def equal_to_24(a,b,c,d):
#     print(a,b,c,d)
    for s in e((str(a),str(b),str(c),str(d))):
#         print(s)
        try:
            if eval(s) == 24:
                return s
        except ZeroDivisionError:
            pass
#     if e((a,b,c,d)): return "True"
    return "It's not possible!"

# def e(ns):
#     if len(ns) == 1:
#         return ns[0] == 24
#     for i in range(len(ns)-1):
#         pre, a, b, post = ns[:i], ns[i], ns[i+1], ns[i+2:]
#         if e(pre+(a+b,)+post): return True
#         if e(pre+(a-b,)+post): return True
#         if e(pre+(a*b,)+post): return True
#         if b!=0 and e(pre+(a/b,)+post): return True

def e(ns):
#     if len(ns) == 1: yield ns[0]
#     for x in range(len(ns)):
#         for y in range(len(ns)):
#             if x == y: continue
#             i, j = min(x,y), max(x,y)
#             for op in "-/":
#                 yield from e(ns[:i] + ns[i+1:j] + ns[j+1:] + ("("+ns[x]+op+ns[y]+")",))
#     for i in range(len(ns)-1):
#         for j in range(i+1,len(ns)):
# #             if x == y: continue
# #             i, j = min(x,y), max(x,y)
#             for op in "+*":
#                 yield from e(ns[:i] + ns[i+1:j] + ns[j+1:] + ("("+ns[i]+op+ns[j]+")",))
