class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        res = 0
        for word in words:
            i, j, m, n = 0, 0, len(word), len(s)
            while i < m and j < n:
                char = word[i]
                count1 = 0
                while i < m and word[i] == char:
                    count1 += 1
                    i += 1
                if word[i-1] != s[j]:
                    break
                
                l = j
                count2 = 0
                while j < n and s[j] == s[l]:
                    count2 += 1
                    j += 1
                if (count1 < count2 and count2 < 3) or count2 < count1:
                    break
            else:
                res += i == m and j == n
        
        return res