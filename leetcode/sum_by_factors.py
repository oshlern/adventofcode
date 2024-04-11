def sum_for_list(lst):
#     ps = [2,3]
#     for k in range(3,int(max(I)**0.5),2):
    print(lst)
#     print(max(map(abs,lst))**0.5)
    print(max(map(abs,lst))//2)
    ps, out = [], []
#     for k in range(2,int(max(map(abs,lst))**0.5)+1):
#     for k in range(2,max(map(abs,lst))):
#     ps = []
#     fs = [set() for _ in lst]
    ns = list(map(abs,lst))
    k = 2
    while k*k <= max(ns):
        if all(k%p != 0 for p in ps):
            ps.append(k)
            ls = []
            for i in range(len(ns)):
                if ns[i] % k == 0:
#                     fs[i].add(k)
                    ls.append(lst[i])
                    while ns[i] % k == 0:
                        ns[i] //= k
            if ls:
                out.append([k, sum(ls)])
        k += 1
    for k in set(ns):
        if k != 1:
            
    return out
#     out = [(p, [n for n,f in zip(lst,fs) if p in f]) for p in ps]
#     out = in range(lenfor p in ps]
#     ps = [2]
#     if (I := [i for i in lst if i%2 == 0]):
#         out.append([2, sum(I)])
#     for k in range(3,max(map(abs,lst)),2):
#         if all(k%p != 0 for p in ps):
#             ps.append(k)
#             if (I := [i for i in lst if i%k == 0]):
#                 out.append([k, sum(I)])
#     return out