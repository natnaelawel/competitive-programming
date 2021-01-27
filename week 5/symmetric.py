# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self._isSymmetric(root, root) 
    def _isSymmetric(self, t1, t2):
        if not t1 and not t2:
            return True 
        elif not t1 or not t2 or t1.val != t2.val:
            return False
        else:
            return self._isSymmetric(t1.left, t2.right) and self._isSymmetric(t1.right, t2.left)
        
        