# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        out = []
        while words:
            line, i = self.build_line(words, maxWidth)
            print("line", line, i)
            out.append(line)
            words = words[i:]
        return out

    def build_line(self, words, maxWidth):
        n_chars = len(words[0])
        i = 1
        while i < len(words):
            word = words[i]
            i += 1
            if n_chars + 1 + len(word) > maxWidth:
                i -= 1
                break
            n_chars += 1 + len(word)

        ws = words[:i] # exclude last i
        spaces = [" " for _ in range(i-1)]

        left_justify = i == 1 or i == len(words)
        n_extra_spaces = maxWidth - n_chars
        if not left_justify:
            for j in range(maxWidth - n_chars):
                spaces[j % len(spaces)] += " "

        line = ""
        for j in range(i):
            line += ws[j]
            if j < len(spaces):
                line += spaces[j]
        if left_justify:
            line += " "*n_extra_spaces
        return line, i
