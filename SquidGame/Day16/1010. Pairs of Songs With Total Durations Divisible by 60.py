class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mp = defaultdict(int)
        ans = 0
        for time_val in time:
            rem_t = time_val % 60
            if rem_t == 0:
                ans += mp[0]
            else:
                ans += mp[60-rem_t]
            
            mp[rem_t] += 1
        return ans