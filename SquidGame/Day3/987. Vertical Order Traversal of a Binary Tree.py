# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import defaultdict, deque
from typing import List, Optional


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_vals = defaultdict(list)
        
        queue = deque([(root, 0, 0)])
        
        while queue:
            size = len(queue)
            level_vals = defaultdict(list)

            for i in range(size):
                node, r, c = queue.popleft()
                level_vals[c].append(node.val)

                if node.left:
                    nr, nc = r + 1, c - 1
                    queue.append((node.left, nr, nc))

                if node.right:
                    nr, nc = r + 1, c + 1
                    queue.append((node.right, nr, nc))
            for k, v in level_vals.items():
                for val in sorted(v):
                    vertical_vals[k].append(val)
                
        cols = sorted(vertical_vals.keys())
        return [vertical_vals[col] for col in cols]