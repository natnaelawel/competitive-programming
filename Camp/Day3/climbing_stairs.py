class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.countWays(n, memo)
        
        
    def countWays(self, n, memo):
        if n in memo: 
            return memo[n]
        if n <= 1:
            return 1
        else: 
            memo[n] = self.countWays(n - 1, memo) + self.countWays(n - 2, memo)
            return memo[n]
       