from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        if n == 1:
            return [0]
        if n == 2:
            return edges[0]
        indegree = {node: 0 for node in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        levelNodes = []
        for node, cnt in indegree.items():
            if cnt == 1:
                levelNodes.append(node)
        visited = set()
        while n > 2:
            leafnodes = []
            while levelNodes:
                node = levelNodes.pop()
                n -= 1
                visited.add(node)
                for nbr in graph[node]:
                    if nbr not in visited:
                        indegree[nbr] -= 1
                        if indegree[nbr] == 1:
                            leafnodes.append(nbr)
            for node in leafnodes:
                levelNodes.append(node)
        return levelNodes
