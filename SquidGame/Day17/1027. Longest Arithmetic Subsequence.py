class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        mp = {}
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                if (j, diff) in mp:
                    mp[i, diff] = mp[j, diff] + 1
                else:
                    mp[i, diff] = 2
        return max(mp.values())
