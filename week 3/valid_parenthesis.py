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


class Solution:
    def check(self, ch1, ch2):
        if ch1 == "(" and ch2 == ")":
            return True
        if ch1 == "{" and ch2 == "}":
            return True
        if ch1 == "[" and ch2 == "]":
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stacks = Stack()
        isValid = True
        for i in s:
            # print(stacks.get_stack())
            if i in ")}]" and stacks.isEmpty():
                return False
            if i in "({[":
                stacks.push(i)
            else:
                top = stacks.pop()
                # print(top, stacks.get_stack())
                if not self.check(top, i):
                    isValid = False
        if stacks.isEmpty() and isValid:
            return True
        else:
            return False
