# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.minDiff = 100000
        def dfs(node):
            if node.left:
                minLeft, maxLeft = dfs(node.left)
                self.minDiff = min(node.val - maxLeft, self.minDiff)
            if node.right:
                minRight, maxRight = dfs(node.right)
                self.minDiff = min(minRight - node.val, self.minDiff)
            
            if node.left and node.right:
                 return (minLeft, maxRight)
            elif node.left:
                return (minLeft, node.val)
            elif node.right:
                return (node.val, maxRight)
            else:
                return (node.val, node.val)
        
        dfs(root)
        return self.minDiff