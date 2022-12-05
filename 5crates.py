# from itertools import chain
# import string
# import functools

filename = 'input5_3.txt'
# filename = 'input5.txt'


positions = []

# lines = input_file.readlines()

total = 0

with open(filename, 'r') as input_file:
    # line = "["
    line = next(input_file)
    n = int((len(line))/4)
    containers = [[] for _ in range(n)]
    while line[0] == '[':
        for i in range(n):
            ind = i * 4 + 1
            char = line[ind]
            if char == ' ':
                continue
            else:
                containers[i].append(char)
        line = next(input_file)
    next(input_file)
    try:
        while True:
            print(containers)
            line = next(input_file)
            line = line.strip().split(" ")
            num, src, dst = int(line[1]), int(line[3])-1, int(line[5])-1
            print(num, src+1, dst+1, len(containers))
            # print(containers[src], containers[dst])

            containers[dst] = containers[src][:num] + containers[dst]
            containers[src] = containers[src][num:]
    except StopIteration:
        print([c[-1] for c in containers])



