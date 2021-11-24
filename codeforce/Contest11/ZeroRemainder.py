class Solution:
    def binarySearch(self, nums, n):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > n:
                l =  mid - 1 
            elif nums[mid]< n:
                r = mid + 1
            else: 
                return mid
    def findMinMove(self, nums, k):
        re = [(k - (n% k)) for n in nums if n % k != 0]
        m = {}
        mmax = -1
        for r in re: 
            if r in m:
                m[r] += k 
                mmax = max(mmax, m[r])
            else: 
                m[r] = r
                mmax = max(mmax, m[r])
                
        return mmax + 1
        
        
        
        # nums.sort()
        # nSets = set()
        # x = 0
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] % k == 0:
        #         continue
        #     while True:
        #         f = x % k 
        #         s = nums[i] % k 
        #         if (f + s) % k == 0:
        #             x += 1
        #             break 
        #         elif k % (f + s) == 0:
        #             x += k // (f+s)
        #             break
        #         else: 
        #             x += 1
        
        # return x
        # nSets = set()
        # x = 0
        # one = False
        # nums.sort()
        # while len(nSets) < len(nums):
        #     for i in range(len(nums)):
        #         if nums[i] % k == 0:
        #             nSets.add(i)
        #             continue
        #         f = x % k
        #         s = nums[i] % k 
        #         if i not in nSets and (f + s) % k == 0:
        #             nums[i] = f + s
        #             nSets.add(i)
        #             one = True
        #             break
        #     x += 1
        # return x if one else 0
        
sol = Solution()
t = int(input())
res = []
for _ in range(t):
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    res.append(sol.findMinMove(nums, k))
for r in res: 
    print(r)