import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

nums = [int(l) for l in ll]
# nums = [10,6,0,-5,-12]
# nums = [-1,2,1,0]

x = [n for n in nums]
# print(x)
N = len(nums)
inds = list(range(N))
print(nums)
print(len(nums))
print(len(set(nums)))
for i in range(N):
    ind = inds[i]
    new_ind = (ind + nums[i]) % (N-1)

for n in range(N):
    i = inds.index(n)
    j = (i + nums[n] + N-1) % (N-1)
    inds = inds[:i] + inds[i+1:]
    inds = inds[:j] + [n] + inds[j:]


def shift(x, i, d):
    if d == 0:
        return x
    if d == 1:
        n = x[i]
        j = (i + 1) % N
        x[i] = x[j]
        x[j] = n
for n in nums:
    i = x.index(n)
    j = (i + n + N-1) % (N-1)
#     j = (n + i + len(nums) - 1) % (len(nums) - 1)
#    nums = nums[:i] + nums[i+1:]
#    nums = nums[:j] + [n] + nums[new_idx:]
#     # n = x[i]
    # j = (i + ) % N
    # if j > 
    # x[i:j] = x[i+1:j+1]
    # x[j] = n
    x = x[:i] + x[i+1:]
    # j = (i + n+1) % (N-1)-1
    x = x[:j] + [n] + x[j:]
    # print(x, i, j, n)


out = 0
start = x.index(0)
for i in [1000, 2000, 3000]:
    v = x[(start + i) % N]
    print(start, v, (start + i) % N, N)
    out += v
# print(out)

Nums = [n for n in nums]
# print(nums)
for n in Nums:
    i = nums.index(n)
    item = nums[i]
    new_idx = (item + i + len(nums) - 1) % (len(nums) - 1)
    nums = nums[:i] + nums[i+1:]
    nums = nums[:new_idx] + [item] + nums[new_idx:]
    # print(item, i, new_idx, nums)

out = 0
start = nums.index(0)
for i in [1000, 2000, 3000]:
    v = nums[(start + i) % N]
    # print(start, v, (start + i) % N, N)
    out += v
print(out)

# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))