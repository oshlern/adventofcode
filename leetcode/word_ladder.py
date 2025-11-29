# https://leetcode.com/problems/word-ladder/

from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        As = {}
        wordList = set(wordList + [beginWord])
        for word1 in wordList:
            As[word1] = set()
            for word2 in wordList:
                if sum([(c1 != c2) for c1,c2 in zip(word1, word2)]) == 1:
                    As[word1].add(word2)

        frontier = set([beginWord])
        unvisited = set(wordList)
        dist = 1
        while unvisited:
            if endWord in frontier:
                return dist
            unvisited -= frontier
            frontier = set().union(*[As[word] for word in frontier]) & unvisited
            dist += 1
        return 0
