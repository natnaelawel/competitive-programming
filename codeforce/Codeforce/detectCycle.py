from collections import deque, defaultdict
class Solution:
    def getParent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.getParent(parent, parent[i])

    def makeUnion(self, parent, x, y):
        parent[x] = y 
        
    def detectCycle(self, edges, n):
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        parent = [-1 for i in range(n)]
        for node in graph:
            for neighbor in graph[node]:
                x = self.getParent(parent, node)
                y = self.getParent(parent, neighbor)
                if x == y:
                    return True  
                self.makeUnion(parent, x,y)
        return False
        
        
        

edges = [[0, 1], [1, 2], [2, 0]]
# edges = [[0, 1], [1, 2], [0, 3]]

sol = Solution()
print(sol.detectCycle(edges, 3))
