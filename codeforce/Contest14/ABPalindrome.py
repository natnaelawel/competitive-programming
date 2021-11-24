class Solution:
    def buildPalindrome(self, s, a, b):
        l, r = 0, len(s)-1
        res = []
        if len(s) == 1:
            if s[0] == "0":
                if a < 1:
                    return -1
            elif s[0] == "1":
                if b < 1:
                    return -1
                
        while l<= r:
            left, right = s[l], s[r]
            if left != "?" and right !="?" and left != right: 
                return -1
            if l == r:
                res.append(("?", "??", l, r))
            else:
                if ord(left) > ord(right):
                    res.append((right, left, r, l))
                else:
                    res.append((left, right, l, r))
            l += 1
            r -= 1
        res.sort()
        for left, right, l, r in res:
            if left == right:
                if left == "0":
                    if a > 1:
                        a -= 2 
                    else:
                        return -1
                elif left == "1":
                    if b > 1:
                        b -= 2 
                    else:
                        return -1
                elif left == "?":
                    if a > 1:
                        a -= 2
                        s[l] = "0"
                        s[r] = "0" 
                    elif b > 1:
                        b -= 2
                        s[l] = "1"
                        s[r] = "1"
                    else:
                        return -1
                    
            else: 
                if left == "0":
                    a -= 2
                    s[r] = "0"
                elif right == "0":
                    a -= 2
                    s[l] = "0"
                    
                elif left == "1": 
                    b -= 2
                    s[r] = "1"
                    
                elif right == "1":
                    b -= 2
                    s[l] = "1"
                    
                else:
                    if a > 0:
                        a -= 1 
                        s[l] = "0"
                    elif b > 0:
                        b -= 1
                        s[l] = "1"
                    else:
                        return -1
                        
                          
        return "".join(s)
sol = Solution()
t = int(input())
inputs = []
for _ in range(t):
    a, b = list(map(int, input().split()))
    s = list(input())
    inputs.append((s, a, b))
for s, a, b in inputs:
    print(sol.buildPalindrome(s, a, b))





# 27
# 2 0
# 00
# 0 6
# ?10011
# 19 1
# 1111100001?00011?111
# 7 12
# ??00?101??1?0?100??
# 4 2
# ?10000
# 3 6
# 11?111100
# 1 11
# 111?1001001?
# 15 1
# 00?11010?10110??
# 3 0
# 101
# 6 12
# ?01??110??011?0?01
# 1 1
# 00
# 9 2
# ???01010??0
# 10 2
# 1110?0000?01
# 1 19
# 00000110100101100000
# 2 15
# 101011011?11?1111
# 4 8
# 01????101?1?
# 0 3
# 010
# 4 2
# 100?01
# 8 6
# 1??0??11?00??1
# 1 0
# 0
# 4 9
# 1?011??01?0??
# 3 7
# 1000000001
# 6 14
# ?011?11?1?110?1????1
# 7 6
# 0111100011110
# 3 6
# 11001?001
# 1 11
# 100001100001
# 2 11
# 110??1?1???11
