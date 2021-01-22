# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        return self._rangeSumBST(root, low, high)

    def _rangeSumBST(self, curr_node: TreeNode, low:int, high:int)-> int:
        value = 0
        if not curr_node:
            return 0 
        if curr_node.val >= low and curr_node.val <= high:
            value = curr_node.val
        
        return value + self._rangeSumBST(curr_node.left, low, high) + self._rangeSumBST(curr_node.right, low, high)
