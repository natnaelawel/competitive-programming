class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for num in nums:
            nextElms = nums.copy()
            nextElms.remove(num)
            self.helper([num], nextElms, nums, result)
        return result
    
    def helper(self, currNums, restNums, nums, result):
        if len(currNums) == len(nums):
            result.append(currNums)
            return
        else:
            for num in restNums:
                cn = currNums.copy()
                cn.append(num)
                rest = restNums.copy()
                rest.remove(num)
                self.helper(cn, rest, nums, result)
            