class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []
        changed.sort()
        ans = []
        vals = Counter(changed)
        for num in changed:
            if vals[num] > 0 and num * 2 in vals and vals[num * 2] > 0 :
                vals[num] -= 1
                vals[num*2] -= 1
                ans.append(num)
                if vals[num] == 0:
                    del vals[num]
                if vals[num* 2] == 0:
                    del vals[num* 2]
        return ans if len(vals) == 0 else []
