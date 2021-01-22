class Solution:
    def superDigit(self, n, k):
        n = self.split_add(n) * k
        return self._superDigit(n)

    def _superDigit(self, n):
        if n < 10:
            return n
        n = self.split_add(n)
        return self._superDigit(n)

    def split_add(self, n):
        if n <= 0:
            return 0
        rem = n % 10
        return rem + self.split_add(n//10)


sol = Solution()

print(sol.superDigit(148, 3))
print(sol.superDigit(123, 9))
print(sol.superDigit(9875, 4))