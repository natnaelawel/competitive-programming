from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minVal =  float("-inf")
        f, s, t = [minVal, minVal, minVal]
        
        for num in nums:
            if num == f or num == s or num == t:
                continue
            if num > f:
                t = s
                s = f
                f = num
            elif num > s:
                t = s
                s = num
            elif num > t:
                t = num
        return t if t != float("-inf") else f