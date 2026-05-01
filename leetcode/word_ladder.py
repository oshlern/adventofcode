# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList + [beginWord])

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



# from collections import defaultdict, deque

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordList = set(wordList + [beginWord])

#         frontier = deque([(beginWord, 1)])
#         unseen = set(wordList) - set(beginWord)
#         while frontier:
#             word, dist = frontier.popleft()
#             if word == endWord:
#                 return dist
#             ns = [n for n in unseen if self.char_dist(word, n) == 1]
#             # ns = sorted(ns, key=lambda n: self.char_dist(n, endWord))
#             frontier.extend([(n, dist + 1) for n in ns])
#             unseen = unseen.difference(ns)
#         return 0

#     def char_dist(self, word1, word2):
#         return sum(word1[i] != word2[i] for i in range(len(word1)))



# Dijkstra

# https://leetcode.com/problems/word-ladder/

# from collections import defaultdict
# import heapq

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if beginWord not in wordList:
#             wordList.append(beginWord)
#         # wordList = set(wordList + [beginWord])
#         h = {word: self.char_dist(word, endWord) for word in wordList}
#         g = defaultdict(lambda: 10_000)
#         f = defaultdict(lambda: 10_000)
#         g[beginWord] = 0
#         f[beginWord] = h[beginWord]

#         q = [(f[beginWord], beginWord)]
#         q_set = set([w for _,w in q])


#         # frontier = deque([(beginWord, 1, self.char_dist(beginWord, endWord))])
#         # unseen = set(wordList) - set(beginWord)
#         # i = 0
#         while q:
#             f_val, word = heapq.heappop(q)
#             q_set.remove(word)
#             if word == endWord:
#                 return g[word] + 1

#             # ns = [n for n in wordList if self.char_dist(word, n) == 1]
#             # ns = [(n, self.char_dist(n, endWord)) for n in ns]
#             tentative = g[word] + 1
#             for n in wordList:
#                 if self.char_dist(word, n) != 1:
#                     continue
#                 if tentative < g[n]:
#                     g[n] = tentative
#                     f[n] = tentative + h[n]
#                     if n not in q_set:
#                         heapq.heappush(q, (f[n], n))
#                         q_set.add(n)
#         return 0

#     def char_dist(self, word1, word2):
#         return sum(word1[i] != word2[i] for i in range(len(word1)))
