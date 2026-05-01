def sum_of_products(a):
    """ returns sum of all products of subarrays of a """
    if len(a) == 0:
        return 0
    return a[0] + (a[0] + 1) * sum_of_products(a[1:])
# https://www.codewars.com/kata/570e236e93214be19d000e1a/train/python






def sum_of_prods(s):
    """ returns sum of all products of 
        even-odd-even indiced subarrays of s """
    assert len(s) % 2
    ks = [0, 0]
    for i,a in enumerate(s):
        e = i%2 == 0
        ks[not e] += a * ks[e] + (a if e else 0)
    return ks[0]

    
#     ke, ko = [0, 0], [0, 0]
#     for i,a in enumerate(s):
#         p = i % 2
#         ke[p], ko[p] = a * ko[not p], a * (ke[not p] + (i-1)%2)
#         print(s, i, a, ke, ko)
#     return sum(ko)


# def sop(s): # returns [ke-[ie, io], ko-[ie, io]]
    
#     if len(s) == 0:
#         return {"ke": {"ie": 0, "io": 0}, "ko": {"ie": 0, "io": 0}}
#      {"ke": 
#             {"ie": , "io": 0}, "ko": {"ie": 0, "io": 0}}
    

# https://www.codewars.com/kata/570e79d2de4dc800c900190a/train/python