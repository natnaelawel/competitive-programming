class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        left_one_pre = [0] * (n+1)
        right_one_pre = [0] * (n+1)
        left_zero_pre = [0] * (n+1)
        right_zero_pre = [0] * (n+1)
        for i in range(len(s)):
            if s[i] == "0":
                left_zero_pre[i+1] = left_zero_pre[i] + 1
                left_one_pre[i+1] = left_one_pre[i] 
            else:
                left_one_pre[i+1] = left_one_pre[i] + 1
                left_zero_pre[i+1] = left_zero_pre[i] 
            if s[n-i-1] == "0":
                right_zero_pre[i+1] = right_zero_pre[i] + 1
                right_one_pre[i+1] = right_one_pre[i] 
            else:
                right_one_pre[i+1] = right_one_pre[i] + 1
                right_zero_pre[i+1] = right_zero_pre[i] 
        right_zero_pre.reverse()
        right_one_pre.reverse()
        ans = 0
        for i in range(n):
            if s[i] == "0":
                ans += left_one_pre[i] * right_one_pre[i+1]
            else:
                ans += left_zero_pre[i] * right_zero_pre[i+1]

        return ans




