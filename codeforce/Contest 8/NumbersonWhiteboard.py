t = input()
import math
class Solution:
    def findMinNum(self,nums):
        n = len(nums)
        last = n
        results = []
        for i in range(n-1, 0, -1):
            res = math.ceil((i + last) / 2)
            results.append((i, last))
            last = res
                
        print(2)
        for num1, num2 in results:
            print(num1, num2) 
        return
    # def findMinNum(self,nums):
    #     results = []
    #     for i in range(len(nums)-1, 0, -1):
    #         res = math.ceil((nums[i] + nums[i-1]) / 2)
    #         results.append((nums[i], nums[i-1]))
    #         nums[i-1] = res
    #         print(nums)
                
    #     print(nums[0])
    #     for num1, num2 in results:
    #         print(num1, num2) 
    #     return
    # def findMinNum(self,nums):
    #     heapq.heapify(nums)
    #     results = []
    #     while len(nums) > 1:
    #         num1, num2 = -heapq.heappop(nums), -heapq.heappop(nums)
    #         results.append((num1, num2))
    #         res = math.ceil((num1 + num2) / 2)
    #         heapq.heappush(nums, -res)
                
    #     print(-nums[0])
    #     for num1, num2 in results:
    #         print(num1, num2) 
    #     return
sol = Solution()
for _ in range(int(t)):
    s = input()
    sol.findMinNum([i for i in range(1, int(s)+1)])