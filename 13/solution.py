import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
# ll = open(filename).read().strip().split('\n\n')
ll = open(filename).read().strip().split('\n')
ll = [eval(l) for l in ll if len(l) > 0]
ll.append([[2]])
ll.append([[6]])

def compare(a, b):
    if type(a) == int and type(b) == int:
        if (a < b):
            return 1
        if a == b:
            return 0
        if a > b:
            return -1

    if type(a) == int and type(b) == list:
        a = [a]
    elif type(a) == list and type(b) == int:
        b = [b]
    
    for i in range(len(a)):
        if i > len(b)-1:
            return -1
        n = compare(a[i], b[i])
        if n == 1:
            return 1
        if n == -1:
            return -1
    if len(a) < len(b):
        return 1
    return 0



def sort(l):
    if len(l) == 1:
        return l
    if len(l) == 2:
        if compare(l[0],l[1]) == 1:
            return l
        else:
            return [l[1], l[0]]
    else:
        i = len(l)//2
        a = sort(l[:i])
        b = sort(l[i:])
        print(i, a, b)
        
        out = []
        ai = 0
        bi = 0
        while len(out) < len(l):
            # if i == 2:
            #     print(ai, bi, out)

            if ai >= len(a):
                out += b[bi:]
                continue
            if bi >= len(b):
                out += a[ai:]
                continue
            # print(len(a), len(b), ai, bi)
            if compare(a[ai], b[bi]) == 1:
                out.append(a[ai])
                ai += 1
            else: 
                out.append(b[bi])
                bi += 1
        # print(out)
        return out

ll = sort(ll)

for i in range(len(ll)):
    if ll[i] == [[2]]:
        i2 = i+1
    if ll[i] == [[6]]:
        i6 = i+1
for l in ll:
    print(l)
print(i2, i6)
# # print(ll)
# o = []
# for i,l in enumerate(ll):
#     a, b = l.split('\n')
#     a = eval(a)
#     b = eval(b)
#     print(i, compare(a,b))

#     if compare(a,b) == 1:
#         # print(i)
#         o.append(i+1)

# print(sum(o))
    