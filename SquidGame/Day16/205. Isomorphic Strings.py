class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in m and t[i] not in seen:
                m[s[i]] = t[i]
                seen.add(t[i])
            elif s[i] not in m and t[i] in seen:
                return False
            elif m[s[i]] != t[i]:
                return False
        
        return True