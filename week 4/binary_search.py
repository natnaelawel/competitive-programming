from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target , 0, (len(nums)-1))
    
    # recursive method
    def _search(self, nums: List[int], target:int, left, right)->int:
        if right >= left:
            midIndex = (left + right) // 2
            midValue = nums[midIndex]
            if target == midValue: 
                return midIndex 
            elif midValue > target:
                return self._search(nums, target,  left, midIndex - 1)
            else:
                return self._search(nums, target, midIndex +1, right)
        else:
            return -1
        
    # iterative method
#     def _search(self, nums: List[int], target: int) ->int:
#         # if len(nums) == 1:
#         #     if nums[0] == target:
#         #         return 0 
#         #     else: 
#         #         return -1
            
#         left  = 0 
#         right = len(nums) - 1
#         while left <= right: 
#             midIndex = (left + right) // 2 
#             midValue = nums[midIndex]
#             if target == midValue: 
#                 return midIndex 
#             if target < midValue:
#                 right = midIndex - 1
#             else:
#                 left = midIndex + 1
#         return -1    