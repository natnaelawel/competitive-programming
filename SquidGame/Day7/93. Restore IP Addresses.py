from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []
        self.helper("", 0, s, res)
        return res
        
    def isValid(self, s):
        if len(s) == 1:
            return True
        if len(s) > 1 and s[0] == "0":
            return False
            
        if not (len(s) > 1 and 0 < int(s) < 256):
            return False
        return True
        
    def helper(self, curr, i, s, res):
        if i == len(s):
            if curr[0] == ".":
                curr = curr[1:]
            if curr[-1] == ".":
                curr = curr[:len(curr)]
            if len(curr.split(".")) == 4:
                res.append(curr)
            
        for j in range(i+1, i+4):
            c = s[i: j]
            if self.isValid(c):
                self.helper(curr + "."+ c, j, s, res)
            
        