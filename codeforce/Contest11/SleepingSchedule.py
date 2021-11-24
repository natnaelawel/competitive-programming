import sys 
sys.setrecursionlimit(5000)
class Solution:
    def findGoodTime(self, t1, t2, tlen, days):
        memo = {}
        days.insert(0, 0)
        def dfs(curr, step):
            if (curr, step) in memo:
                return memo[(curr, step)]
            if step == len(days)-1:
                return 1 if t1 <= curr <= t2 else 0
            if t1 <= curr <= t2:
                res = 1 + max(dfs((curr + days[step] - 1) % tlen, step+1), dfs((curr + days[step]) % tlen, step+1))
            else: 
                res = max(dfs((curr + days[step] - 1) % tlen, step+1), dfs((curr + days[step]) % tlen, step+1))
            memo[(curr, step)] = res
            return res
        return dfs(0, 0) 
    
sol = Solution()
dlen, tlen, t1, t2 = [int(x) for x in input().split()]
days = list(map(int, input().split()))
 
print(sol.findGoodTime(t1, t2, tlen, days))