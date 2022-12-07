# from itertools import chain
# import string
# import functools

# filename = 'inputs/4_2.txt'
filename = 'inputs/4.txt'

# lines = input_file.readlines()

total = 0

def in_range(interval, val):
    Min, Max = interval
    if Min <= val and Max >= val:
        return True
with open(filename, 'r') as input_file:
    try:
        while True:
            line = next(input_file)
            line = line.strip()
            intervals = map(lambda s: s.split('-'), line.split(','))
            intervals = list(map(lambda interval: list(map(int, interval)), intervals))

            if (   in_range(intervals[0], intervals[1][0])
                or in_range(intervals[0], intervals[1][1])
                or in_range(intervals[1], intervals[0][0])):
                total += 1
    except StopIteration:
        print(total)



