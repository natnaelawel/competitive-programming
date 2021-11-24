from collections import deque
class Solution:
    def countGroup(self, graph, inDegree):
        # indegree = defaultdict(list)
        # for k, v in graph.items(): 
        #     indegree[v].append(k)
        # queue = deque([])
        print(inDegree)        

sol = Solution()
t = int(input())
from collections import defaultdict
graph = {i: [] for i in range(t)}
inDegree = defaultdict(list)
for i in range(1, t+1):
    p = int(input())
    if p == -1:
        graph[0].append(i)
        inDegree[i].append(0)
    else:
        graph[p].append(i)
        inDegree[i].append(p)
    
print(sol.countGroup(graph, inDegree))


# import sys
# sys.setrecursionlimit(2500)

# class Solution:
#     def countGroup(self, manager, superior):
#         ng = [0]
#         for m in manager:
#             self.dfs(superior, m, 1, ng)
#         return ng[0]
#     def dfs(self, graph, curr, step, ng):
#         if curr not in graph:
#             ng[0] = max(step, ng[0])
#             return
#         for node in graph[curr]:
#             self.dfs(graph, node,step+1, ng)
    
# sol = Solution()
# t = int(input())
# from collections import defaultdict
# manager = list()
# superior = defaultdict(list)
# for i in range(1, t+1):
#     p = int(input())
#     if p == -1:
#         manager.append(i)
#     else:
#         superior[p].append(i)
    
# print(sol.countGroup(manager, superior))

    