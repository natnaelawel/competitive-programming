from typing import *
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        wdict = defaultdict(list)
        lpar = paragraph.lower().replace(",", " ")
        npar = ""
        print(lpar)
        for i in lpar:
            if ord(i) == ord(" ") or 97 <= ord(i) <= 122:
                npar += i
        for i in npar.split(" "):
            if i != " " or i != "":
                wdict[i.lower()].append(i)
        result = [(key, len(val)) for key, val in wdict.items()]
        result = sorted(result, key = lambda item: (item[1], item[0]))
        # print(result)
        for i in range(len(result)-1, -1, -1):
            # print(result[i])
            if result[i][0] not in banned and result[i][0] != "":
                return result[i][0]
        
sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
# paragraph = "a."
# banned = []
# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]
print(sol.mostCommonWord(paragraph, banned))