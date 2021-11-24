class Solution:
    def tribonacci(self, n: int) -> int:
        return self._tribonacci(n) 
    def _tribonacci(self, n, memo={}):
        if n in memo: 
            return memo[n]
        if n == 0:
            return 0 
        elif n < 3: 
            return 1 
        result = self._tribonacci(n-3, memo) + self._tribonacci(n-2, memo) + self._tribonacci(n-1, memo)
        memo[n] = result
        return result
        