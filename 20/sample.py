import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

nums = [int(l) for l in ll]

# myfile = open("input.txt")
# content = myfile.read().splitlines()

# decryption_key = 811589153
# og_nums = [int(x)*decryption_key for x in content]
og_nums = nums
curr_nums = list(range(len(og_nums)))

assert(og_nums.count(0)==1)

print(curr_nums)
print(og_nums)
# for _ in range():
for i, num in enumerate(og_nums):
    loc = curr_nums.index(i)
    del curr_nums[loc]
    insertion_index = (loc+num)%len(curr_nums)
    if insertion_index == 0:
      curr_nums.append(i)
    else:
      curr_nums.insert(insertion_index, i)
    print(curr_nums)
    print([og_nums[x] for x in curr_nums])
    print(i, loc, insertion_index)
    # print()


zero_index = curr_nums.index(og_nums.index(0))
a = og_nums[curr_nums[(zero_index+1000)%len(curr_nums)]]
b = og_nums[curr_nums[(zero_index+2000)%len(curr_nums)]]
c = og_nums[curr_nums[(zero_index+3000)%len(curr_nums)]]
print(a, b, c, a+b+c)