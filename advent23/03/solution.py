import sys

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
print(open(filename).readlines())
ll = open(filename).read().strip().split('\n')

# efficient approach, store 1 or 2 rows at a time
total = 0
width, height = len(ll[0]), len(ll)
for r_i, r in enumerate(ll):
    n = ""
    include_n = False
    for c_i, c in enumerate(r):
        # print(n)
        if c.isdigit():
            if not include_n:
                for s_r in range(max(0,r_i-1), min(height, r_i+2)):
                    for s_c in range(max(0,c_i-1), min(width,c_i+2)):
                        s = ll[s_r][s_c]
                        print(c, s, s_c, s_r, n, c_i, width)
                        if not (s.isdigit() or s == '.'):
                            # print(n, s)
                            include_n = True
                            # if n:
            n += c
            print(c,n, include_n)
        else:
            if include_n:
                total += int(n)
            n = ""
            include_n = False
    if include_n:
        total += int(n)
print(total)



# # efficient approach, store 1 or 2 rows at a time
# total = 0
# last_ns = []
# this_Ss = []


# symbols = []
# for row_i, row in enumerate(ll):
#     n = ""
#     n_start = None
#     n_end = None
#     for c_i, c in row:
#         if c.isdigit():
#             if n:
#                 n.append(c)
#             else:
#                 n_start = c_i
#         elif c == ".":
#             if n:
#                 n_end = c_i - 1
#                 ns[row_i].append((n, n_start, n_end))
#         else:
#             symbols.append((row_i, c_i))
                