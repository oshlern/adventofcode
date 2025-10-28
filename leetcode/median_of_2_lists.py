import math

def get(nums, i):
    if i < len(nums):
        return nums[i]
    else:
        return math.inf

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n_1, n_2 = len(nums1), len(nums2)
        # it1, it2 = iter(nums1), iters(num2)
        tot_n = n_1 + n_2
        # median_i = tot_n
        i1, i2 = 0, 0
        while i1 + i2 < tot_n/2:
            cur1, next1 = get(nums1, i1), get(nums1, i1+1)
            cur2, next2 = get(nums2, i2), get(nums2, i2+1)
            if cur1 < cur2:
                i1 += 1
            elif cur2 < cur1:
                i2 += 1
            else:
                if next1 < next2:
                    i1 += 1
                else:
                    i2 += 1
        cur_ns = sorted([cur1, next1, cur2, next2])
        if tot_n % 2 == 1:
            return cur_ns[0]
        else:
            return (cur_ns[0] + cur_ns[1]) / 2

        # a1, a1 = next(it1)

# 1 7 9
# 1 4 5 7 7 7 7 8 9 123 5
#   _ _
