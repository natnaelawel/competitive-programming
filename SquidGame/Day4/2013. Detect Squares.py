from typing import List
from collections import defaultdict
class DetectSquares:
    
    def __init__(self):
        self.count_dict = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.count_dict[tuple(point)] += 1

    def count(self, point: List[int]) -> int:

        count = 0
        for p1, p2 in self.count_dict:
            x, y = point
            if abs(x-p1) == abs(y-p2) and abs(x-p1) > 0:
                count += self.count_dict[(p1,p2)] * self.count_dict.get(p1,y) * self.d.get(x,p2)
        return count
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)