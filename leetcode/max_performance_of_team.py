# https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # argmax(sum(sp)*sum(ef))
        # = argmax(ln(sum(sp)) + ln(sum(ef)))
        # Es = list(zip(speed, efficiency))
        # Ls = Es[:k]
        Ss = speed[:k]
        Es = efficiency[:k]
        for i in range(k+1, n+1):
            s = speed[i]
            E = Es[i]
            total_s = sum(Ss)
            total_e = sum(Es)

        print(Es)
