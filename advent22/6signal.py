# from itertools import chain
# import string
# import functools

filename = 'inputs/6.txt'
# filename = 'inputs/6_2.txt'
last_cs = ""

with open(filename, 'r') as input_file:
    line = next(input_file)

    last_cs = ""
    for i, c in enumerate(line):
        if len(last_cs) < 14:
            last_cs += c
            continue
        else:
            last_cs = last_cs[1:] + c
        unique = True
        for j1 in range(len(last_cs)):
            for j2 in range(j1+1, len(last_cs)):
                if last_cs[j1] == last_cs[j2]:
                    unique = False
        if unique:
            print(i+1)
            print(unique, last_cs)
            break



