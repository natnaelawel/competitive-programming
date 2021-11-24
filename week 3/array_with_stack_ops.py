from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack_ops = []
        for i in range(1, target[-1]+ 1):
            if i in target:
                stack_ops.append("Push")
            else:
                stack_ops.append("Push")
                stack_ops.append("Pop")
                
        return stack_ops