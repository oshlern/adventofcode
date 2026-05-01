import sys
import re

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

# total = 0
# for l in ll:
#     b = l[:2]

#     for c in l[2:]:
#         if b[1] > b[0]:
#             b = b[1] + c
#         elif (candidate := b[0] + c) > b:
#             b = candidate
#     print(b)
#     total += int(b)

total = 0
N = 12
for l in ll:
    b = "0"*N
    for c in l:
        for bi in range(1,N):
            if b[bi-1] < b[bi]:
                b = b[:bi-1] + b[bi:] + c
                break
        if b[-1] < c:
            b = b[:-1] + c
    

        #     if c > b[bi] and i + (N-bi) < len(l):
        #         b = b[:bi] + l[i:i+(N-bi)]
        #         break
        # if b[-1] > b[0]:
        #     b = b[1] + c
        # elif (candidate := b[0] + c) > b:
            # b = candidate
    print(b)
    total += int(b)



print(total)
