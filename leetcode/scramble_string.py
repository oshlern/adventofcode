# https://leetcode.com/problems/scramble-string/
import random
from collections import Counter
from functools import lru_cache


class Solution:
    @lru_cache
    def isScramble(self, s1: str, s2: str) -> bool:
        # print(s1, s2)
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        if len(s1) == 1:
            return False
        for i in range(1, len(s1)):
            x1, y1 = s1[:i], s1[i:]
            x2, y2 = s2[:i], s2[i:]
            Y2, X2 = s2[:-i], s2[-i:]
            if (Counter(x1) == Counter(x2)) and (Counter(y1) == Counter(y2)):
                if self.isScramble(x1, x2) and self.isScramble(y1, y2):
                    return True
            if (Counter(x1) == Counter(X2)) and (Counter(y1) == Counter(Y2)):
                if self.isScramble(x1, X2) and self.isScramble(y1, Y2):
                    return True

        return False

        # print(s1)
        # print(self.scramble(s1))
        # pass
    def scramble(self, s):
        if len(s) == 1:
            return s
        i = random.randint(1, len(s)-1)
        x, y = s[:i], s[i:]
        if random.random() > 0.5: # assuming 50-50 randomness
            x, y = y, x
        x, y = self.scramble(x), self.scramble(y)
        return x + y


# 123456789
# 56789 1234
# 23456789 1
#
