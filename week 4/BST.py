# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self._searchBST(root, val)
    
    def _searchBST(self, current_node, val)-> TreeNode:
        if not current_node:
            return None 
        if current_node.val == val:
            return current_node
        
        if val < current_node.val:
            return self._searchBST(current_node.left, val)
        elif val > current_node.val:
            return self._searchBST(current_node.right, val)
        