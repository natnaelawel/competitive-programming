class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def helper(opening, closing, res):
            nonlocal result
            if len(res) == 2 * n:
                result.append(res)
                return
            
            if opening < n:
                helper(opening + 1, closing, res + "(")
            if opening > closing:
                helper(opening, closing + 1, res + ")")

        helper(0, 0, "")
        return result
        