# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList + [beginWord])
        for word1 in wordList:
            As[word1] = set()
            for word2 in wordList:
                if sum([(c1 != c2) for c1,c2 in zip(word1, word2)]) == 1:
                    As[word1].add(word2)

        frontier = deque([(beginWord, 1, self.char_dist(beginWord, endWord))])
        unseen = set(wordList) - set(beginWord)
        i = 0
        while frontier:
            word, dist, end_dist = frontier.popleft()
            i += 1
            print(i, word)
            if word == endWord:
                return dist
            ns = [n for n in unseen if self.char_dist(word, n) == 1]
            ns = [(n, self.char_dist(n, endWord)) for n in ns]
            ns = [(n, d) for n, d in ns if d <= end_dist]
            # ns = sorted(ns, key=lambda n: n[1])
            frontier.extend([(n, dist + 1, d) for n, d in ns])
            unseen = unseen.difference([n for n, d in ns])
        return 0

    def char_dist(self, word1, word2):
        return sum(word1[i] != word2[i] for i in range(len(word1)))
