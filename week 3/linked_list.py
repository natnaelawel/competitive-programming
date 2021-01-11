class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


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
        if index < 0 or index >= self.size:
            return None
        elif index == 0: 
            newNode.next = self.head
            self.head = newNode
            return
        while index > 0:
            prev = current
            current = current.next
            index -= 1
        newNode.next = current
        prev.next = newNode
        self.size += 1


    def deleteAtIndex(self, index):
        current = self.head
        prev = None
        if index < 0 or index > self.size:
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


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
obj.get(1)
obj.deleteAtIndex(1)
obj.get(1)

param_1 = obj.get(0)
param_2 = obj.get(1)
param_3 = obj.get(2)

print(obj.size)
print(obj.get(0))
print(obj.get(1))
print(obj.get(2))
print(obj.get(3))
