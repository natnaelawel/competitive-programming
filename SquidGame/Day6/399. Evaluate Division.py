import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i, eq in enumerate(equations):
            f, t, w = eq[0], eq[1], values[i]
            graph[f].append((t,w))
            graph[t].append((f,1/w))
        
        def costOfPath(current, target, cost, visited):
            if current not in graph or target not in graph:
                return -1
            if current == target:
                return cost            
            for (t,w) in graph[current]:
                if t not in visited:
                    visited.add(current)
                    pathCost = costOfPath(t,target,cost*w,visited)
                    if pathCost > 0:
                        return pathCost 
            return -1
                    
        results = [] 
        for query in queries:
            results.append(costOfPath(query[0], query[1], 1, set()))
        
        return results 