from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for ui, vi in adjacentPairs:
            graph[ui].append(vi)
            graph[vi].append(ui)

        res =[]
        for k, v in graph.items():
            if len(v) == 1:
                start = k
                break
        visited = set()

        def dfs(start):
            if start in visited:
                return 
            visited.add(start)
            res.append(start)
            for nbr in graph[start]:
                if nbr not in visited:
                    dfs(nbr)

        dfs(start)  
        return res  