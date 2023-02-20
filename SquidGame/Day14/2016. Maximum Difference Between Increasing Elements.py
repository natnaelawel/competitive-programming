class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_min = float("inf")
        max_diff = -1
        for i in range(len(nums)):
            if curr_min > nums[i]:
                curr_min = nums[i]
            max_diff = max(max_diff, nums[i] - curr_min)
        return max_diff if max_diff > 0 else -1