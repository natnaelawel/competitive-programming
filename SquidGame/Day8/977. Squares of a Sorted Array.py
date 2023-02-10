from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, res = 0, len(nums)-1, []
        while l <= r:
            left, right = nums[l]**2, nums[r]**2
            if left > right:
                res.append(left)
                l += 1
            else:
                res.append(right)
                r -= 1
        return res[::-1]


