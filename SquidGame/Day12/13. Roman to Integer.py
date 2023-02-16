class Solution:
    def romanToInt(self, s: str) -> int:
        l, r = 0, 1
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        while l < len(s):
            if r < len(s):
                if values[s[l]] < values[s[r]]:
                    total += values[s[r]] - values[s[l]]
                    l = r + 1
                    r = l + 1
                else: 
                    total += values[s[l]]
                    l += 1
                    r += 1
            else: 
                total += values[s[l]]
                l += 1
        return total
        