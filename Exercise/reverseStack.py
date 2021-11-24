class Solution:
    def _reverse(self, stack, n):
        if stack == []:
            return stack.append(n)
        last = stack.pop()
        self._reverse(stack, n)
        stack.append(last)
        return stack
    def reverseStack(self, stack):
        if stack == []:
            return
        last = stack.pop()
        self.reverseStack(stack)   
        self._reverse(stack, last)     
        return stack
sol = Solution()
stack = [1, 5, 2, 6, 4]
print(sol.reverseStack(stack))