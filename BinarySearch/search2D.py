class Solution:
    # O(log m) + O(log n)
    def findNum(self, grid, target):
        row, col = len(grid), len(grid[0])
        def getTargetArr():
            l = 0
            r = row - 1
            res = grid[0]
            while l <= r: 
                mid = (l + r) // 2
                print(grid[mid])
                if grid[mid][0] <= target <= grid[mid][-1]:
                    return grid[mid]
                elif grid[mid][0] > target:
                    r = mid - 1
                elif grid[mid][-1] < target:
                    l = mid + 1
            return res
        arr = getTargetArr()
        l = 0 
        r = col - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                l = mid + 1
            else: 
                r = mid - 1
        return False
                
                
sol = Solution()
grid = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [15, 16, 17, 18]]
target = 19
print(sol.findNum(grid, target))