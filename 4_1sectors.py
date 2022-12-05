# from itertools import chain
# import string
# import functools

# filename = 'input4_2.txt'
filename = 'input4.txt'

# lines = input_file.readlines()

total = 0

with open(filename, 'r') as input_file:
    try:
        while True:
            line = next(input_file)
            line = line.strip()
            intervals = map(lambda s: s.split('-'), line.split(','))
            intervals = list(map(lambda interval: list(map(int, interval)), intervals))
            if (   (intervals[0][0] <= intervals[1][0] and intervals[0][1] >= intervals[1][1])
                or (intervals[0][0] >= intervals[1][0] and intervals[0][1] <= intervals[1][1])):
                total += 1
    except StopIteration:
        print(total)



