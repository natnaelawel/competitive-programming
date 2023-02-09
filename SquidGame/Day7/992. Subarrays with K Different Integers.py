from collections import defaultdict
from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            ans, l, r = 0, 0, 0
            count_map = defaultdict(int)
            while r < len(nums):
                count_map[nums[r]] += 1
                while len(count_map) > k:
                    count_map[nums[l]] -= 1
                    if count_map[nums[l]] == 0:
                        del count_map[nums[l]]
                    l += 1
                ans += r - l + 1
                r += 1
            return ans

        return helper(nums, k) - helper(nums, k-1)