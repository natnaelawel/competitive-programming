from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        buses = defaultdict(set)
        graph = defaultdict(set)
        for bus, routes in enumerate(routes):
            for route in routes:
                buses[bus].add(route)
                graph[route].add(bus)
        count = 0
        visited = set()
        queue = deque()
        for bus in graph[source]:
            queue.append(bus)
        while queue:
            size = len(queue)
            count += 1
            for _ in range(size):
                bus = queue.popleft()
                if target in buses[bus]:
                    return count
                if bus not in visited:
                    visited.add(bus)
                    new_buses = set()
                    for route in buses[bus]:
                        new_buses |= graph[route]
                    for bus in new_buses:
                        if bus not in visited:
                            queue.append(bus)
            
        return -1