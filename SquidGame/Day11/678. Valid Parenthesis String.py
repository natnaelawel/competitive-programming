class Solution:
    def checkValidString(self, s: str) -> bool:
        @lru_cache(None)
        def dp(i, stack):
            stack = list(stack)
            if i >= len(s):
                return len(stack) == 0
            ans = False
            if s[i] == "(":
                stack.append(s[i])
                ans |= dp(i+1, tuple(stack[:]))
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    ans |= dp(i+1, tuple(stack[:]))
            else:
                stack.append("(")
                ans |= dp(i+1, tuple(stack[:]))
                stack.pop()
                if stack:
                    stack.pop()
                    ans |= dp(i+1, tuple(stack[:]))
                    stack.append("(")
                ans |= dp(i+1, tuple(stack[:]))
            return ans

        return dp(0, ())
