class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        ans, n = 0, len(s)
        s = list(s)
        for i in range(n):
            hasSwap = False
            j = 0
            while j < n:
                if s[j] == "0" and j+1 < n and s[j+1] == "1":
                    s[j], s[j+1] = "1", "0"
                    hasSwap = True
                    j += 2
                else:
                    j += 1
            ans += hasSwap
        return ans
