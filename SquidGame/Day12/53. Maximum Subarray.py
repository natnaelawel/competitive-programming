class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = -10000
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            max_value = max(curr_sum, max_value)
            if curr_sum < 0:
                curr_sum = 0
        return max_value