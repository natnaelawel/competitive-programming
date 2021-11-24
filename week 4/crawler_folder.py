from typing import List


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    def size(self): 
        return len(self.items)
    
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = Stack()
        for i in logs:
            if i == "../":
                if s.isEmpty(): 
                    continue
                s.pop()
            elif i == "./":
                continue
            else:
                s.push(i)

        return s.size()
        