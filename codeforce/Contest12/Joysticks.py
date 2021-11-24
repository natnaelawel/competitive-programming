import heapq
class Solution:
    def countMaxTime(self, first, second):
        counter = 0
        if first <= 1 and second <= 1:
            return 0
        while first >= 1 and second >= 1:
            if first >= second: 
                second += 1
                first -= 2
            else:
                second -= 2 
                first += 1
            counter += 1
                
        return counter
    
sol = Solution()
x, y = list(map(int, input().split()))
print(sol.countMaxTime(x, y))