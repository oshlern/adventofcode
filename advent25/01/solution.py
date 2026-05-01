import sys
import re

filename = 'input.txt' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')


total = 0
pos = 50
for l in ll:
    direction = l[0]
    num = int(l[1:])
    # if direction == "L":
    #     num = -num
    d = -1 if direction == "L" else 1
    # new_pos = pos + num
    for i in range(num):
        pos = (pos + d) % 100
        if pos == 0 :
            total += 1
    # pos = (new_pos) % 100
    # if pos == 0 :
    #     total += 1
print(total)
