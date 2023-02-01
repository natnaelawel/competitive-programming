from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [(age, score) for [age, score] in zip(ages, scores)]
        pairs.sort(reverse=True) 
        res = 0
        n = len(scores)
        dp = [0] * n
        for i, [age, score] in enumerate(pairs):
            dp[i] = score
            for j in range(i):
                if score <= pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + score)
            res = max(res, dp[i])
        return res

