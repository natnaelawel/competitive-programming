class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res=[]
        ops = ["*", "+", "-"]
        for i,ch in enumerate(expression):
            isOps = ch in ops
            if isOps:
                first, last = expression[:i],expression[i+1:] 
                left = self.diffWaysToCompute(first)
                right = self.diffWaysToCompute(last)
                
                for j in left:
                    for k in right:
                        if ch == '*':
                            res.append(j*k)
                        elif ch =='-':
                            res.append(j-k)
                        else:
                            res.append(j+k)
        if not res:
            res.append(int(expression))
        return res