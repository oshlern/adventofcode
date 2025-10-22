class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr = sorted(arr)
        pairs = []
        min_diff = float('inf')
        for a1, a2 in zip(sorted_arr, sorted_arr[1:]):
            diff = a2 - a1
            if diff < min_diff:
                pairs = []
                min_diff = diff
            if diff == min_diff:
                pairs.append([a1, a2])
        return pairs
