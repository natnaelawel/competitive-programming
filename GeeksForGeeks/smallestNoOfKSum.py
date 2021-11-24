class Solution:
    def smallestNumber(self, n, d):
        l = [0] * d
        n -= 1
        for i in range(d-1, 0, -1):
            if n > 9:
                n -= 9 
                l[i] = 9
            else:
                l[i] = n 
                n = 0
        l[0] += 1
        print(l)
        num = 0
        for i in range(len(l)):
            num = num * 10 + l[i]
        return num
sol = Solution()
n = 9
d = 2
print(sol.smallestNumber(n, d))