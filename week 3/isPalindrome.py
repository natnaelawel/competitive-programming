class ListNode:
    def __init__(self, val=0, nextItem = None):
        self.val = val
        self.next = nextItem
        
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        current = head
        if current is None or current.next is None:
            return True
        reversedOne = self.reverseList(current)
        currentReversed = reversedOne
        while current.next != None:
            if currentReversed.val != current.val:
                return False
            current = current.next 
            currentReversed = currentReversed.next
        if current.val != currentReversed.val: 
            return False
        return True
    def reverseList(self, head):
        node_values = []
        current = head
        while current: 
            node_values.append(current.val)
            current = current.next

        reversedListNode = None
        reversedHead = None
        for i in range(len(node_values) -1, -1, -1):
            if i == len(node_values) - 1:
                reversedHead = ListNode(node_values[i])
                reversedListNode = reversedHead
            else:
                reversedHead.next = ListNode(node_values[i])
                reversedHead = reversedHead.next
        return reversedListNode
    def printNodes(self, node):
        while node != None:
            print(node.val, ", ")
            node = node.next