from collections import defaultdict, deque
class Solution:
    def TopologicalSorting(self, nums):
        digraph = defaultdict(list)
        for u, v in nums:
            digraph[u].append(v)
        inDegree = {node: 0 for node in digraph}
        for node in digraph:
            for neighbor in digraph[node]:
                if neighbor in inDegree:
                    inDegree[neighbor] += 1
                else: 
                    inDegree[neighbor] = 1
        queue = deque()
        for node in digraph:
            if inDegree[node] == 0:
                queue.append(node)
                
        topologicalSorting = []
        while queue:
            node = queue.popleft()
            topologicalSorting.append(node)
            
            for neighbor in digraph[node]:
                inDegree[neighbor] -= 1 
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(topologicalSorting) == len(digraph):
            print(*topologicalSorting)
        else: 
            print("Graph has a cycle")
sol = Solution()
nums = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 4], [4, 5]]
sol.TopologicalSorting(nums)