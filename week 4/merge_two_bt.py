# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, tree1: TreeNode, tree2: TreeNode) -> TreeNode:
        tree1 = self._mergeTrees(tree1, tree2)
        return tree1    
    def _mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None 
        if t1 and not t2:
            t2 = TreeNode(0)
        if t2 and not t1:
            t1 = TreeNode(0)
            # t1 = t2
        if t1 and t2:
            t1.val += t2.val
            t1.left =  self._mergeTrees(t1.left, t2.left)
            t1.right = self._mergeTrees(t1.right, t2.right)
        return t1
        