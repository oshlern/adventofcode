# from itertools import chain
import string

input_file = open('inputs/3_2.txt', 'r')
lines = input_file.readlines()

letters = string.ascii_letters
priorities = {letters[i]: i+1 for i in range(len(letters))}
total = 0

for line in lines:
    bags = line.strip()
    n = len(bags)//2
    # print(n, len(bags))
    bag1 = set(bags[:n])
    bag2 = set(bags[n:])
    common = bag1.intersection(bag2)
    # print(common)
    pri = priorities[common.pop()]
    total += pri
print(total)


