class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(n)}
        ingoing = {i: 0 for i in range(n)}
        for start, end in edges:
            graph[start].append(end)
            ingoing[end] += 1
        queue = []
        for node in range(n):
            if ingoing[node] == 0:
                queue.append(node)
        return queue

        