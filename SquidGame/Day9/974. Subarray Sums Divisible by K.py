class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp, count, sum_ = defaultdict(int), 0, 0
        mp[0] = 1
        for num in nums:
            sum_ += num
            if sum_ % k in mp:
                count += mp[sum_ % k]
            mp[sum_ % k] += 1
        return count