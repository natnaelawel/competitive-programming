class Solution: 
    def num_island(self, grid): 
        m = len(grid) 
        n = len(grid[0])
        counter = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, m, n, i, j, directions)
                    counter += 1
                
        return counter
    
    def is_inside(self, m, n, i, j):
        return 0 <= i < m and 0 <= j < n;
                
    def dfs(self, grid, m, n, i, j, directions):
        grid[i][j] = "0"
        for (x, y) in directions:
            newX = i + x 
            newY = j + y 
            
            if self.is_inside(m, n, newX, newY) and grid[newX][newY] == 1:
                self.dfs(grid, m, n, newX, newY, directions)
                
sol = Solution()
grid = [
    [1,1,0,0,0],
    [1,0,0,0,0],
    [0,1,0,1,0],
    [1,0,0,1,1],
    [0,1,1,0,1],
]        

print(sol.num_island(grid))
        