class Solution:
    def findMinDis(self, paths):
        res = [-1]
        for i in range(len(paths)):
            if paths[i] == "R":
                res.append(i)
        res.append(len(paths))
        m = 0
        for i in range(1, len(res)):
            m = max(m, res[i] - res[i-1])
            
        return m
    
sol = Solution()
t = int(input())
result = []
for i in range(t):
    paths = input()
    result.append(sol.findMinDis(paths))
    
for res in result:
    print(res)