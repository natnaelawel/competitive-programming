t = input()
class Solution:
    def printIndices(self, n, p):
        lMin = p[0]
        rMin = p[-1]
        leftMin = []
        rightMin = []
        for i in range(n):
            lMin = min((p[i], lMin))
            leftMin.append(lMin)
        for i in range(n-1, -1, -1):
            rMin = min((p[i], rMin))
            rightMin.append(rMin)
        rightMin = rightMin[::-1]  
        for i in range(1, n-1):
            if p[i] > leftMin[i] and p[i] > rightMin[i]:
                print("YES")
                print(p.index(leftMin[i])+1, i+1,p.index(rightMin[i])+1)
                return
        print("NO")
sol = Solution()
for _ in range(int(t)):
    n = input()
    p = list(map(int, input().split()))
    sol.printIndices(int(n), p)