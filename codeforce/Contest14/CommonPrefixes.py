import random
class Solution:
    def constructPairs(self, c, first, second):
        ran = "abcdefghijklmnopqrstuvwxyz"
        if len(second) < len(first):
            second = first[:c]
        elif len(second) > len(first):
            first = second[:c]
        if first == second and first =="":
            if c == 0:
                ch1 = random.choice(ran)
                first += ch1
                ch = random.choice(ran)
                while ch == ch1:
                    ch = random.choice(ran)
                second += ch
            else: 
                for _ in range(c-len(first)):
                    ch = random.choice(ran)
                    first += ch 
                    second += ch 
        return [first, second]
            
    def buildCommonPrefix(self, n, nums):
        res = {i: "" for i in range(len(nums)+1)}
        pairs = []
        for i in range(len(nums)):
            pairs.append((nums[i], i, i+1 ))
        pairs.sort(reverse=True)
        for c, f, s in pairs:
            first, second = self.constructPairs(c, res[f], res[s])
            res[f] = first
            res[s] = second
        for r in res:
            if res[r] != "":
                print(res[r])
sol = Solution()
t = int(input())
inputs = []
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    inputs.append((n, nums))
for n, nums in inputs:
    sol.buildCommonPrefix(n, nums)



