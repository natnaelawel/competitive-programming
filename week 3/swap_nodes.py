# from LinkedList.linkedlist import LinkedList, Node
# from LinkedList.linkedlist import LinkedList, Node


from linkedlist import Node, LinkedList

class Solution:
    def __init__(self, llist: Node) -> None:
        self.head = llist

    def printNodes(self, head :Optional[Node]):
        current: Node = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print("")

    def swapNodes(self, key1: Node, key2: Node):
        if key1 == key2:
            return
        prev1 = None
        current1 = self.head
        while current1 and current1.data != key1:
            prev1 = current1
            current1 = current1.next

        prev2 = None
        current2 = self.head

        while current2 and current2.data != key2:
            prev2 = current2
            current2 = current2.next
        if not current1 or not current2:
            return
        print("before")
        self.printNodes()
        if prev1:
            prev1.next = current2
            print("after prev 1")
            self.printNodes()
        else:
            self.head = current2
            self.printNodes()
            
        if prev2:
            print("after prev 2")
            
            prev2.next = current1
            self.printNodes()
            
        else:
            self.head = current1

        self.printNodes()
        current1.next, current2.next = current2.next, current1.next

        # print(prev1.data, ' prev')
        # print(current1.data, ' current')

        # print(prev2.data, ' prev')
        # print(current2.data, ' current')


llist = LinkedList()

llist.append(0)
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
head = llist.head

sol = Solution(head)
sol.swapNodes(1, 4)

sol.printNodes()
