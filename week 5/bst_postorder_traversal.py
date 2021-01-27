# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self._post_order(root, result)
        return result
        
    def _post_order(self, root, result):
        if root: 
            self._post_order(root.left, result)        
            self._post_order(root.right, result)
            result.append(root.val)