from collections import deque
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)
    
    def bfs(self, node):
        queue = deque([(node, 0)])
        maxWidth = 1
        while queue:
            level_size = len(queue)
            nodes = []
            for i in range(level_size):
                node, lastIndex = queue.popleft()
                if node.left:
                    currIndex = 2 * lastIndex + 1
                    nodes.append(currIndex)
                    queue.append((node.left, currIndex))

                if node.right:
                    currIndex = 2 * lastIndex + 2
                    nodes.append(currIndex)
                    queue.append((node.right, currIndex))
            if nodes:
                maxWidth = max(maxWidth, max(nodes) - min(nodes) + 1)
        return maxWidth
