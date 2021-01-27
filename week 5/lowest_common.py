# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._lowestCommonAncestor(root, p, q)
    
    def _lowestCommonAncestor(self,root, p, q):
        if not root:
            return None
        if p.val < root.val and q.val < root.val:
            return self._lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val: 
            return self._lowestCommonAncestor(root.right, p, q)
        else:
            return root
