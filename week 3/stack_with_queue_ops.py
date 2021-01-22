from collections import deque
class MyStack:
    def __init__(self):
        self.items =  deque()

    def push(self, x: int) -> None:
        self.items.push(x)
        

    def pop(self) -> int:
        return self.items.pop()
        

    def top(self) -> int:
        if self.empty():
            return None 
        else:
            return self.items[-1]
        
    def empty(self) -> bool:
        return len(self.items) == 0

