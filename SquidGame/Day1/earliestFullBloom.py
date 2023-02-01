from typing import List

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        n = len(plantTime)
        sorted_pt_gt = sorted([(plantTime[i], growTime[i]) for i in range(n)], key = lambda x: -x[1],)
        start = sorted_pt_gt[0][0]
        last, total_time = 0, start
        for pt, gt in sorted_pt_gt:
            total_time = max(total_time, (gt + pt + last))
            last += pt
        return total_time