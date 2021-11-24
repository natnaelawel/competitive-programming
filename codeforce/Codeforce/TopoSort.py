from collections import deque, defaultdict
class Solution:
    def canFinish(self, preRequests):
        graph = defaultdict(set)
        
        
        

preRequests = [[0, 1], [1, 4], [4, 5], [1, 2], [2, 3], [2, 6]]
# preRequests = [[0, 1], [1, 4], [4, 5], [1, 2], [2, 3], [2, 6], [6, 3]]
sol = Solution()
print(sol.canFinish(preRequests))
