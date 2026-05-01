# https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, N: int) -> List[str]:
        opts = [[""], ["()"]]
        for n in range(2, N+1):
            out = []
            for i in range(n):
                s_ins = opts[i]
                s_outs = opts[n-1-i]
                out += [ "(" + s_in + ")" + s_out for s_in in s_ins for s_out in s_outs ]
                print(opts)
            opts.append(out)
        return opts[-1]
