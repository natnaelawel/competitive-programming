# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: 
            root = TreeNode(val)
            return root
        self._insertIntoBST(root, val)
        return root
    def _insertIntoBST(self, root: TreeNode, val:int):
        if val < root.val:
            if not root.left: 
                root.left = TreeNode(val)
                return
            else:
                return self._insertIntoBST(root.left, val)
            
        else:
            if not root.right:
                root.right = TreeNode(val)
                return
            else:
                return self._insertIntoBST(root.right, val)
            
