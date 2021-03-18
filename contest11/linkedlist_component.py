from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        current = head
        i = 0
        outer = []
        inner = []
        G = set(G)
        print(G)
        while current:
            if current.val in G:
                inner.append(current.val)
            else:
                if len(inner):
                    outer.append(inner)
                inner = []
            current = current.next
            i += 1
        if inner:
            outer.append(inner)
        return len(outer) 
        
sol = Solution()
e = ListNode(4)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)
a = ListNode(0, b)

e = ListNode(0)
d = ListNode(2, e)
c = ListNode(1, d)
b = ListNode(3, c)
a = ListNode(4, b)
# a = ListNode(0)

# g = [4, 3, 1,, 2, 0]
# g = [0]
g = [1, 3, 0]

print(sol.numComponents(a, g))
