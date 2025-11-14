# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        S = [["X", 0]] + [[c, 0] for c in s]
        simplified = True
        while simplified:
            simplified = False
            i = len(S) - 1
            while i > 1:
                c2, n2 = S[i]
                c1, n1 = S[i-1]
                if c1 == "(" and c2 == ")":
                    # remove i and i2
                    S.pop(i)
                    S.pop(i-1)
                    S[i-2][1] += 1 + n1 + 1 + n2
                    simplified = True
                    i -= 1
                i -= 1
        return max([n for c, n in S])


# ()()())(())
# ...)(.)
#  1))1(23(62
