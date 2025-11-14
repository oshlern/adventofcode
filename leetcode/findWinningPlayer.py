https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/description/

class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        highest = skills[0]
        n_victories = 0
        for s in skills[1:]:
            if s > highest:
                highest = s
                n_victories = 1
            else:
                n_victories += 1

            if n_victories == k:
                break
        return skills.index(highest)
