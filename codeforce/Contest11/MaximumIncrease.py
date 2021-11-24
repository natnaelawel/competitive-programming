class Solution:
    def countMaxSubArray(self, nums):
        left = 0
        right = 1
        maxLen = 1
        prev = nums[left] 
        count = 1
        while right < len(nums):
            if nums[right] > prev:
                count += 1
            else:
                maxLen = max(count, maxLen)
                count = 1
            prev = nums[right]
            right += 1
        return max(maxLen, count)
sol = Solution()
t = int(input())
nums = list(map(int, input().split()))
print(sol.countMaxSubArray(nums))
