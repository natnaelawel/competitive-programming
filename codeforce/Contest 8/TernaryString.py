t = input()
class Solution:
    def ternaryString(self,s):
        contains = dict()
        start = 0
        m = float("inf")
        
        for end in range(len(s)):
            right = s[end]
            if right not in contains:
                contains[right] = 0
            contains[right] += 1
            
            if len(contains) == 3:
                m = min(m, end - start + 1)
                left = s[start]
                contains[left] -= 1
                if contains[left] == 0:
                    del contains[left]
        
        return m if m != float("inf") else 0
sol = Solution()
result = []
for _ in range(int(t)):
    s = input()
    result.append(sol.ternaryString(s))
for i in result:
    print(i)