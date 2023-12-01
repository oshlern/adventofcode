import sys
import numpy as np

filename = 'input' if len(sys.argv) == 1 else sys.argv[1]
ll = open(filename).read().strip().split('\n')

nums = [int(l) for l in ll]
k = 811589153
nums = [n*k for n in nums]
# nums = [10,6,0,-5,-12]
# nums = [-1,2,1,0]

N = len(nums)
inds = list(range(N))
print(nums)
for _ in range(10):
    for n in range(N):
        i = inds.index(n)
        j = (i + nums[n] + N-1) % (N-1)
        inds = inds[:i] + inds[i+1:]
        inds = inds[:j] + [n] + inds[j:]
    # print([nums[ind] for ind in inds])

out = 0
start = inds.index(nums.index(0))
for i in [1000, 2000, 3000]:
    v = nums[inds[(start + i) % N]]
    print(start, v, (start + i) % N, N)
    out += v
print(out)

# ll = [int(l) for l in ll if len(l) > 0]
# for l in ll:
#     c = l.split(' -> ')
#     a = np.array(eval('['+c[0]+']'))