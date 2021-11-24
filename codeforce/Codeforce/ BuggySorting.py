class Solution:
    def BuggySorting(self, n):
        if n < 3:
            return -1 
        nums = [str(i) for i in range(n, 0, -1)]
     
        return " ".join(nums)
    
sol = Solution()
n = input()
print(sol.BuggySorting(int(n)))