from functools import lru_cache
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordSet = set(words)
        @lru_cache(None)
        def dp(word):
            curr_max = 1
            for i in range(len(word)):
                predecessor = word[:i] + word[i + 1:]
                if predecessor in wordSet:
                    curr_max = max(curr_max, dp(predecessor) + 1)
            return curr_max
        ans = 0
        for word in words:
            ans = max(ans, dp(word))
        return ans



