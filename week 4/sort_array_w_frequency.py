from typing import Counter, List, Optional

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result = Counter(nums)
        return [k for k, v in sorted(result.items(), key=lambda item: (-item[1], item[0]), reverse=True) for i in range(v)]
