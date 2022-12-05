# from itertools import chain
import string
import functools

# filename = 'input3_2.txt'
filename = 'input3.txt'

# lines = input_file.readlines()

letters = string.ascii_letters
priorities = {letters[i]: i+1 for i in range(len(letters))}
total = 0

def make_set(l):
    s = []
    for a in l:
        for b in s:
            if a == b:
                break
        else:
            s.append(a)
    return s

def set_intersection(s1, s2):
    out = []
    for a1 in s1:
        for a2 in s2:
            if a1 == a2:
                out.append(a1)
    return out

with  open(filename, 'r') as input_file:
    try:
        while True:
            lines = [next(input_file) for i in range(3)]
            bags = map(lambda s: s.strip(), lines)
            bag_sets = map(make_set, bags)
            common = functools.reduce(set_intersection, bag_sets)
            pri = priorities[common.pop()]
            total += pri
    except StopIteration:
        print(total)



