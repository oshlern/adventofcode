import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')
ll = [eval(l) for l in ll if len(l) > 0]

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
        if n == 0:
            continue
        else:
            return n
    if len(a) < len(b):
        return 1
    return 0

tot = 0
for i in range(len(ll)//2):
    if compare(ll[2*i], ll[2*i+1]) == 1:
        tot += i+1
print(tot)

def sort(l):
    if len(l) == 1:
        return l
    if len(l) == 2:
        if compare(l[0],l[1]) == 1:
            return l
        else:
            return l[::-1]
    else:
        i = len(l)//2
        a = sort(l[:i])
        b = sort(l[i:])

        out = []
        ai = 0
        bi = 0
        while len(out) < len(l):
            if ai >= len(a):
                out += b[bi:]
            elif bi >= len(b):
                out += a[ai:]
            elif compare(a[ai], b[bi]) == 1:
                out.append(a[ai])
                ai += 1
            else: 
                out.append(b[bi])
                bi += 1
        return out

ll.append([[2]])
ll.append([[6]])
ll = sort(ll)
i2 = ll.index([[2]]) + 1
i6 = ll.index([[6]]) + 1
print(i2*i6)