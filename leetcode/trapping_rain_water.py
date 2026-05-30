# https://leetcode.com/problems/trapping-rain-water
class Solution:
    def trap(self, height: List[int]) -> int:
        # Water is trapped if there is height to the left and right >= it
        # Left max, right max, between

        left_max, left_max_i = self.find_first_max(height)
        right_max, right_max_i = self.find_first_max(reversed(height))
        right_max_i = len(height) - 1 - right_max_i
        # print(left_max_i, right_max_i)

        left_water = self.water_left_trapped(height[:left_max_i])
        right_water = self.water_left_trapped(reversed(height[right_max_i+1:]))
        middle_water = 0
        if left_max_i != right_max_i:
            for h in height[left_max_i:right_max_i]:
                middle_water += left_max - h
        # print(left_water, middle_water, right_water)
        return left_water + middle_water + right_water

    def find_first_max(self, ns):
        first_max, first_max_i = -1, -1
        for i,n in enumerate(ns):
            # print(i, n, first_max, first_max_i)
            if n > first_max:
                first_max = n
                first_max_i = i
        return first_max, first_max_i

    def water_left_trapped(self, height):
        # print(height)
        greatest_seen = 0
        total_water = 0
        for i,h in enumerate(height):
            if h >= greatest_seen:
                greatest_seen = h
            else:
                total_water += greatest_seen - h
                # print(i, greatest_seen -h, total_water)
        return total_water
