import math
class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        rem = 0
        isNeg = False
        if x < 0: 
            isNeg = True
            x = -x
        while x > 0:
            rem = x % 10
            res = (res * 10) + rem
            x = x // 10
        res = -res if isNeg else res
        if math.pow(-2, 31) >= res or res >= math.pow(2, 31):
            return 0
        return res
        
        
sol = Solution()
print(sol.reverse(-123))
            
    