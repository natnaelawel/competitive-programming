class Node:
    def __init__(self, val=0, nextItem = None):
        self.val = val
        self.next = nextItem


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        current = self.head
        if index < 0 or index >= self.size:
            return -1
        while index > 0:
            current = current.next
            index -= 1
        return current.val

    def addAtHead(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        current = self.head
        while current.next != None:
            current = current.next
        newNode = Node(val)
        current.next = newNode
        self.size += 1

    def addAtIndex(self, index, val):
        current = self.head
        prev = None
        newNode = Node(val)
        if index < 0 or index > self.size:
            return None
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            self.size += 1
            return
        else:
            self.size += 1
            while index > 0:

                prev = current
                current = current.next
                index -= 1
            newNode.next = current
            prev.next = newNode

    def deleteAtIndex(self, index):
        current = self.head
        prev = None
        if index < 0 or index >= self.size:
            return None
        elif self.size == 0:
            self.head = None
        elif index == 0:
            self.head = current.next
        else:
            while index > 0:
                prev = current
                current = current.next
                index -= 1
            prev.next = current.next
        self.size -= 1

    def deleteANode(self, node):
        current = self.head
        prev = None
        # if index < 0 or index >= self.size:
        #     return None
        if self.size == 0:
            self.head = None
        elif current.next == None and current.val == node.val:
            self.head = current.next
        else:
            while current.next.val != node.val:
                prev = current
                current = current.next
            prev.next = current.next
        self.size -= 1

    def middleNode(self):
        current = head
        size = 0
        while current != None:
            size += 1
            current = current.next
        current = head
        mid = (size + 1) // 2
        midIndex = mid if size % 2 != 0 else mid + 1
        i = 1
        while i <= midIndex-1:
            current = current.next
            i += 1
        return current

    def copyList(self, head):
        current = head 
        cloned = Node()
        current_cloned = cloned 
        while current: 
            current_cloned.next = Node(current.val, current.next)
            current_cloned = current_cloned.next
            current = current.next 
        return cloned.next
    
    def isPalindrom(self, head):
        self.printNodeValues(head)
        self.printNodeValues(self.copyList(head))
        # reversedListHead = Node(head.val)
        # reversedList = Node(head.val)
        # current = head 
        # while current != None: 
        #     newNode = Node(current.val)
        #     reversedList.next = newNode
        #     reversedList =  reversedList
        #     current  = current.next 
        # # self.printNodeValues(head)
        # # self.printNodeValues(reversedList)
        # current = head
        # # reversedHead = reversedList
        # while current != None:
        #     if current.val != reversedHead.val:
        #         return False
        #     current  = current.next 
        #     reversedHead = reversedHead.next
            
        # return True

    def reverseLinkedList(self):
        i = 0
        while i < self.size:
            current_head = self.get(0)
            self.deleteAtIndex(0)
            self.addAtTail(current_head)
            # self.printNodeValues(self.head)
            # print("headvalues")
            i += 1
        return Node(self.head.val, self.head.next)
    

    def printNodes(self):
        current = self.head
        values = ""
        while current != None:
            values += str(current.val) + " , "
            current = current.next

        print(values)

    def printNodeValues(self, current):
        values = ""
        while current != None:
            values += str(current.val) + " , "
            current = current.next

        print(values)


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

# ispalindrome


obj.addAtHead(1)
obj.addAtHead(2)
obj.addAtHead(3)
obj.addAtHead(2)
# print(obj.isPalindrom(obj.head))
# obj.reverseLinkedList()
obj.printNodeValues(obj.head)
obj.printNodeValues(obj.reverseLinkedList())

# obj.addAtTail(3)
# obj.addAtIndex(1,2)
# obj.get(1)
obj.deleteAtIndex(3)
obj.printNodes()
# obj.get(1)
# obj.addAtHead(7)
# # obj.printNodes()
# obj.addAtHead(2)
# # obj.printNodes()
# obj.addAtHead(1)
# # obj.printNodes()
# obj.addAtIndex(3,0)
# # obj.printNodes()
# obj.deleteAtIndex(2)
# # obj.printNodes()
# obj.addAtHead(6)

# obj.addAtTail(4)
# # obj.printNodes()
# obj.get(4)
# obj.addAtHead(4)
# obj.addAtIndex(5,0)
# obj.addAtHead(6)
# obj.deleteAtIndex(0)


# obj.addAtHead(2)
# obj.deleteAtIndex(1)
# obj.addAtHead(2)
# obj.addAtHead(7)
# obj.addAtHead(3)
# obj.addAtHead(2)
# obj.addAtHead(5)
# obj.addAtTail(5)
# obj.get(5)
# obj.printNodes()
# obj.deleteAtIndex(6)
# obj.deleteAtIndex(4)
# # print(obj.middleNode())
# obj.deleteANode(3)

# obj.deleteAtIndex(1)
# obj.get(1)

# param_1 = obj.get(0)
# param_2 = obj.get(1)
# param_3 = obj.get(2)

# print(obj.size)
# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(3))


# print(obj.head)