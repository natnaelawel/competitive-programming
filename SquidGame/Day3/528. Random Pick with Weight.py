from bisect import bisect_left
from random import randint
from typing import List
class Solution:
    def __init__(self, w: List[int]):
        self.pre_sum = []
        sum_ = 0
        for num in w:
            sum_ += num
            self.pre_sum.append(sum_)

    def pickIndex(self) -> int:
        num = randint(1, self.pre_sum[-1])
        return bisect_left(self.pre_sum, num)
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()