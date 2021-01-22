class MyStack:
    def __init__(self):
        self.items = []
    
    def push(self, x:int) -> None:
        self.items.append(x)
        
    def pop(self)->int:
        if not self.isEmpty():
            popedItem = self.items.pop()
            
        return popedItem 
    
    def peek(self) -> int:
        if not self.isEmpty():
            return self.items[-1]
        return None

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    
class MyQueue:
    def __init__(self):
        self.items = MyStack()

    def push(self, x: int) -> None:
        self.items.push(x)


    def pop(self) -> int:
        if not self.empty():
            newStack = MyStack()
            while not self.items.isEmpty():
                newStack.push(self.items.pop())
            popedItem = newStack.pop()
            while not newStack.isEmpty():
                self.items.push(newStack.pop())
            
        return popedItem

    def peek(self) -> int:
        if not self.empty():
            newStack = MyStack()
            while not self.items.isEmpty():
                newStack.push(self.items.pop())
            peekItem = newStack.peek()
            while not newStack.isEmpty():
                self.items.push(newStack.pop())
        return peekItem

    def empty(self) -> bool:
        return self.items.isEmpty()