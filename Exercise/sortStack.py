class Solution:
    def sortStack(self, stack):
        if stack == []:
            return 
        last = stack.pop()
        self.sortStack(stack)
        self._insertInPlace(stack, last)
        return stack
    
    def _insertInPlace(self, stack, num):
        if stack == []:
            stack.append(num)
            return
        elif stack[-1] <= num:
            stack.append(num)
        elif stack[-1] > num:
            last = stack.pop()
            self._insertInPlace(stack, num)
            stack.append(last)
            
sol = Solution()
stack = [1, 4, 2, 8, 5, 5]
print(sol.sortStack(stack))