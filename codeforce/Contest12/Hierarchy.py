import sys 
sys.setrecursionlimit(2000)
from collections import defaultdict
import heapq
class Solution:
    def buildGraph(self, e_q, apps):
        graph = defaultdict(list)
        e_q = {i+1:e_q[i] for i in range(len(e_q))}
        graph = {i+1: [] for i in range(len(e_q))}
        for i in range(len(apps)):
            a, b, c = apps[i]
            graph[a].append((c, -e_q[b], b))
        return graph 
    def countMinCost(self, node, graph, visited, pq):
        counter = 0
        if graph[node] == []:
            return 0
        while len(pq) > 0: 
            c, q, b = heapq.heappop(pq)
            if b not in graph:
                    break
            if b not in visited and  c != float("-inf"):
                counter += c
            visited.add(b)
            for node in graph[b]:
                if node[2] not in visited:
                    heapq.heappush(pq, node)
            if pq == []:
                return counter
            
        return counter 
            
            
 
        
    def solve(self, n_e, e_q, n_a, apps):
        if n_a == 0:
            return 0
        pq = []
        visited = set()
        graph = self.buildGraph(e_q, apps)
        mmax = 0
        for node in graph:
            if node not in visited :
                pq = [(float("-inf"), 0, node)]
                mmax = max(mmax, self.countMinCost(node, graph, visited, pq))
        return mmax if len(visited) == n_e else -1
sol = Solution()
n_e = int(input())
e_q =  list(map(int, input().split()))
n_a = int(input())
apps = []
for _ in range(n_a):
    a, b, c = list(map(int, input().split()))
    apps.append((a, b, c))
    
print(sol.solve(n_e, e_q, n_a, apps))
