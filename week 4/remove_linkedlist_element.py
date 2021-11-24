# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        current = head
        prev = None
        if not current:
            return current
        if current.val == val and current.next is None:
            head = current.next
            return head
            
        while current and current.val == val:
            current = current.next
        head = current
        while current is not None:
            if current.val == val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head