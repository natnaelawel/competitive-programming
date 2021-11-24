import sys 
sys.setrecursionlimit(2000)
class Solution:
    def getLast(self, graph, node, visited):
        visited.add(node)
        if graph[node] in visited or graph[node] == -1:
            return node
        else:
            return self.getLast(graph, graph[node], visited)
    def solve(self, requests):
        req = list()
        for old, new in requests:
            req.append(old)
            req.append(new)
        graph = {node: -1 for node in req}
        visited = set()
        for old, new in requests: 
            graph[old] = new
        result = []
        for node in graph:
            if node not in visited :
                last = self.getLast(graph, node, visited)
                if node != last:
                    result.append((node, last))
        print(len(result))
        for old, new in result:
            print(old, new)
sol = Solution()
t = int(input())
requests = []
for _ in range(int(t)):
    old, new = input().split()
    requests.append((old, new))
sol.solve(requests)