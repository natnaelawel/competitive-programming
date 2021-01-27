# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_num = max(nums)
        tree = TreeNode(max_num)
        index = nums.index(max_num)
        self._constructMaximumBinaryTree(tree, index, nums)
        return tree
        
    def _constructMaximumBinaryTree(self,t, index, nums):
        left_nums = nums[:index]
        right_nums = nums[index+1:]
        if t:
            if left_nums:
                left_max = max(left_nums)
                t.left = TreeNode(left_max) 
                left_index = left_nums.index(left_max)
                self._constructMaximumBinaryTree(t.left, left_index, left_nums)


            if right_nums:
                right_max = max(right_nums)
                t.right = TreeNode(right_max) 
                right_index = right_nums.index(right_max)
                self._constructMaximumBinaryTree(t.right, right_index, right_nums)
