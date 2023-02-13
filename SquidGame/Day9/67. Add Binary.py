class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = ("0" * (len(b) - len(a)))+ a if len(b) > len(a) else a
        b = ("0" * (len(a) - len(b)))+ b if len(a) > len(b) else b
        carry = 0
        res = []
        for i in range(len(a)-1, -1, -1):
            sm = int(a[i]) + int(b[i]) + carry
            rs = sm % 2
            carry = sm // 2
            res.append(str(rs))
        if carry:
            res.append("1")
        res.reverse()
        return "".join(res)
        
        