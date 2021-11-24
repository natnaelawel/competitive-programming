class Solution:
    def smallestNumber(self, n):
        if 0 <= n <= 9:
            return n
        l = list()
        for i in range(9, 1, -1):
            while n % i == 0:
                l.append(i)
                n //= i
        num = 0
        i = 0
        while l:
            last = l.pop()
            num = (10 * num) + last
            i += 1
        return num
sol = Solution()
num = 100
print(sol.smallestNumber(num))