class Solution:
    def giveLetters(self, dorms, letters):
        prevSum = 0
        for index in range(len(letters)):
            while prevSum < dorms[index]:
                prevSum += dorms[index]
            s = prevSum - dorms[index]
            print(index, s)


sol = Solution()
n, m = input().split()
dorms = list(map(int, input().split()))
letters = list(map(int, input().split()))

sol.giveLetters(dorms, letters)