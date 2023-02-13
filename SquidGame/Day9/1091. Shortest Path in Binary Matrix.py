class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        def isValid(x, y):
            return 0 <= x< n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited
        
        def bfs():
            q = deque([(0, 0, 1)])
            if not isValid(0, 0):
                return 
            while q:
                x, y, dst = q.popleft()
                visited.add((x, y))

                if x == n-1 and y == n-1:
                    return dst

                drs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
                for dr in drs:
                    nx, ny = x + dr[0], y + dr[1]
                    if isValid(nx, ny):
                        visited.add((nx, ny))
                        q.append((nx, ny, dst+1))
                  
        result = bfs()
            
        return result if result else -1    