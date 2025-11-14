# https://leetcode.com/problems/maximum-performance-of-a-team/?source=submission-ac

import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        Bs, tot_s, best = [], 0, 0
        for i, eng in enumerate(sorted(list(zip(speed, efficiency)), key=lambda x: x[1], reverse=True)):
            tot_s += eng[0]
            heapq.heappush(Bs, eng[0])
            if i >= k:
                tot_s -= heapq.heappop(Bs)
            if tot_s * eng[1] > best:
                best = tot_s * eng[1]
        return best % (10**9 + 7)
