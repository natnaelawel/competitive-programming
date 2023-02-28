class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxVal = 0
        memo = dict()
        def helper(r, c):
            nonlocal maxVal
            if r >= m or c >= n:
                return 0
            
            if (r, c) in memo:
                return memo[(r, c)]
            
            right = helper(r, c + 1)
            down = helper(r + 1, c)
            diag = helper(r + 1, c + 1)
            memo[(r, c)] = 0
            if matrix[r][c] == "1":
                memo[(r, c)] = 1 + min(right, down, diag)
                maxVal = max(memo[(r, c)], maxVal)
            return memo[(r, c)]
            
        helper(0, 0)
        return maxVal ** 2