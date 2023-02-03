class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l, r, count):
            if count > 1:
                return False
            while l <= r:
                if s[l] != s[r]:
                    return check(l+1, r, count+1) or check(l, r-1, count+1)
                else:
                    l += 1
                    r -= 1
            return True
        return check(0, len(s)-1, 0)