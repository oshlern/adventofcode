import sys
import re

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split(',')

total = 0
for l in ll:
    start, end = l.split('-')
    for n in range(int(start), int(end)+1):
        s = str(n)
        # half = len(s)//2
        # if s[:half] == s[half:]:
            # total += n
        for i in range(2, len(s)+1):
            if s == s[:len(s)//i] * i:
                total += n
                break

print(total)
