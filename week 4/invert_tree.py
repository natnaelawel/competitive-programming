# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self._invertTree(root)
        return root
    
    def _invertTree(self, root):
        if root:
            if root.left and not root.right:
                root.right = root.left 
                root.left = None 
                self._invertTree(root.right)
            elif root.right and not root.left:
                root.left = root.right 
                root.right = None 
                self._invertTree(root.left)

            elif root.left and root.right:
                temp = root.left 
                root.left = root.right 
                root.right = temp 

                self._invertTree(root.left)

                self._invertTree(root.right)
