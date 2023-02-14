from functools import lru_cache


class Solution:
    def minimumDeletions(self, s: str) -> int:
        bCount, count = [], 0
        for c in s:
            count += c == 'b'
            bCount.append(count)
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 0
            ans = dp(i-1)
            if s[i] == 'a':
                return min(ans+1, bCount[i])
            return ans
        return dp(len(s)-1)
    