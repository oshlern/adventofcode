# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        line = []
        while sum(len(w)+1 for w in line) - 1 <= maxWidth:
            line.append(words[i])
            i += 1
            if

    def build_line(words, maxWidth):
        n_chars = len(words[0])
        i = 1
        while i < len(words):
            word = words[i]
            i += 1
            if n_chars + 1 + len(word) > maxWidth:
                break

        if i >= len(words):

        # l_words = []

        #     if i >= len(words):
        #         break
        #         return build_last_line(l_words, maxWidth), None
        #     line.append(words[i])
        #     i += 1
        # l_words.pop()
        # n_words = len(l_words)
        # n_extra_spaces = maxWidth - sum(len(w) for w in l_words)
        # slots = [" " for i in range(max(n_words-1, 1)]
        # for i in range(n_spaces):
        #     slots[i % len(slots)] += " "
        # l = ""
        # for i in range(n_words):
        #     l += l_words[i]
        #     if i < len(slots):
        #         l += slots[i]
        # return l




    def line_len(line):
