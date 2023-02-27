"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        mapping = {}
        t = head
        while t:
            newT = Node(t.val)
            mapping[t] = newT
            t = t.next
        
        h = head
        while h:
            H = mapping[h]
            H.next = mapping[h.next] if h.next else None
            H.random = mapping[h.random] if h.random else None
            h = h.next
        return mapping[head]