# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self._isSameTree(p, q)
        
    def _isSameTree(self, p:TreeNode, q: TreeNode):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False
        else:
            return self._isSameTree(p.left, q.left) and self._isSameTree(p.right, q.right)
        
            
        