class MinStack:
    
    def __init__(self):
        self.items = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        

    def pop(self) -> None:
        return self.items.pop()
        

    def top(self) -> int:
        return self.items[-1]
        
    
    def getMin(self) -> int:
        minValue = self.items[0]
        for i in self.items:
            if i < minValue:
                minValue = i
        return minValue
