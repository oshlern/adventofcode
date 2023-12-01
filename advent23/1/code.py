import os

# fname = "test_input.txt"
# fname = "test_input2.txt"
fname = "input.txt"
with open(fname) as f:
    txt = f.read()


# ds = list(map(str, range(10)))
# # print(ds)
# tot = 0
# for l in txt.split("\n"):
#     first, last = None, None
#     for c in l:
#         if c in ds:
#             if first is None:
#                 first = int(c)
#             last = int(c)
#             # print(c, first, last)
#     tot += first*10 + last
# print(tot)



digits = list(map(str, range(10)))
# spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
spellings = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


ds = {}
for i in range(10):
    ds[digits[i]] = i
    ds[spellings[i]] = i

# del(ds["zero"])
# del(ds["0"])
print(ds)
# print(ds)
tot = 0
for l in txt.split("\n"):
    l_ds = []
    while l:
        skip_len = 1
        for d in ds:
            if l.startswith(d):
                l_ds.append(ds[d])
                # l = l[len(d):]
                # print(d, l)
                skip_len = len(d)
                break
        l = l[1:]
    
    # print(l_ds)
    first, last = l_ds[0], l_ds[-1]
    # print(first, last)
    tot += first*10 + last
    if len(l_ds)< 2:
        print(l_ds, first, last)
print(tot)
print(ds)





# testing another user's code

import re

def f(x):
    for i, s in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
        x = x.replace(s, s[0]+str(i+1)+s[-1])
    z = re.findall(r'\d', x)
    return int(z[0] + z[-1])

print(sum(map(f, open('input.txt'))))

X = open(fname).read().split('\n')
x = X[0]
print(x)
for i, s in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
    x = x.replace(s, str(i+1))
print(x)