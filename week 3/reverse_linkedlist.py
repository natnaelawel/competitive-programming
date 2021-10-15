class ListNode:
    def __init__(self, val=0, nextItem = None):
        self.val = val
        self.next = nextItem
        
class Solution:
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
    def reverseL(self, head):
        if head is None or head.next == None:
            return (head, head)
        newHead, tail = self.reverseL(head.next)
        newHead.next = head
        head.next = None
        return (head, tail)
    
    def printNodes(current):
        while current != None:
            print(current.val)
            current = current.next

        

newNode5 = ListNode(5)
newNode4 = ListNode(4, newNode5)
newNode3 = ListNode(3, newNode4)
newNode2 = ListNode(2, newNode3)
newNode1 = ListNode(1, newNode2)



# printNodes(reverseL(newNode1)[1])
# printNodes(reverseL(newNode1))