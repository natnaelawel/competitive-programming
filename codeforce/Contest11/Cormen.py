class Solution:
    def findDays(self, a, k):
        count = 0
        for i in range(1, len(a)):
            prev, curr = a[i-1], a[i]
            s = curr + prev
            if s > k:
                pass
            else:
                count += k - s 
                a[i] = a[i] + k - s
        print(count)
        print(*a)     
sol = Solution()
t, k = list(map(int, input().split()))
a = list(map(int, input().split()))
sol.findDays(a, k)
