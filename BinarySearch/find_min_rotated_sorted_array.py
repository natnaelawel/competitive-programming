class Solution: 
    def findMin(self, nums):
        res = nums[0]
        l, r = 0, len(nums) -1
        while l <= r:
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break
            mid = (l + r) // 2 
            res = min(res, nums[mid])
            # it means it is strictly increasing
            if nums[mid] >= nums[l]:
                l = mid + 1
            # it mean it is strictly decreasing
            else: 
                r = mid - 1
        return res
    
sol = Solution()
array = [3, 4, 5, 6, 1, 2]
print(sol.findMin(array))