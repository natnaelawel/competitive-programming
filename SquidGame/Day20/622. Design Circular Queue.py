class MyCircularQueue:
    
    def __init__(self, k: int):
        self.max_size = k
        self.first = 0
        self.last = -1
        self.size = 0
        self.queue = [None] * k 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        insertPlace = (self.last + 1 ) % self.max_size
        self.last = insertPlace
        self.queue[insertPlace] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.first] = None
        self.first = (self.first + 1 ) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.last]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()