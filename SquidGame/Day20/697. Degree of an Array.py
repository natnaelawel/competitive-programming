class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        vals = {}
        for i, num in enumerate(nums):
            if num in vals:
                prev_cnt, start_idx, last_idx = vals[num]
                vals[num] = [prev_cnt + 1, start_idx, i]
            else:
                vals[num] = [1, i, i]
        max_val = 0
        min_sub = len(nums)
        for cnt, start_idx, last_idx in sorted(vals.values(), key= lambda x: -x[0]):
            if max_val > cnt:
                break
            min_sub = min(min_sub, last_idx - start_idx + 1)
            max_val = cnt 
        return min_sub
