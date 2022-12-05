# from itertools import chain
# import string
# import functools
# import re
# from collections import defaultdict, Counter

fname = 'input5_2.txt'
filename = 'input5.txt'


positions = []

# lines = input_file.readlines()

def display_containers(cs):
    max_h = max([len(c) for c in cs])
    for h in range(max_h):
        s = ""
        for c in cs:
            ind =  len(c) + h - max_h
            if ind >= 0:
                char = c[ind]
            else:
                char = " "
            s += " " + char + "  "
        print(s)
    s = " ".join(" {} ".format(i+1) for i in range(len(cs)))
    print(s)


total = 0

with open(filename, 'r') as input_file:
    line = next(input_file)

    containers = []
    while line[0] == '[':
        line_length = len(line)//4
        if len(containers) < line_length:
            containers += [[] for _ in range(line_length - len(containers))]
        for i in range(1,len(line),4):
            ind = i//4 + 1 
            char = line[i]
            if char == ' ':
                continue
            else:
                containers[ind-1].append(char)
        line = next(input_file)
    next(input_file)
    try:
        while True:
            # print(containers)
            # display_containers(containers)
            line = next(input_file)
            line = line.strip().split(" ")
            num, src, dst = int(line[1]), int(line[3])-1, int(line[5])-1
            # print(num, src+1, dst+1, len(containers))
            # print(containers[src], containers[dst])

            containers[dst] = containers[src][:num] + containers[dst]
            containers[src] = containers[src][num:]
    except StopIteration:
        print(''.join([c[0] for c in containers]))



