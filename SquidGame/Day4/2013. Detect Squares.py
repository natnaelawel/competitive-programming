from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        self.count_dict = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.count_dict[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        for (x, y) in self.count_dict:
            if abs(px-x) == abs(py-y) and abs(px-x) > 0:
                count += self.count_dict[(x,y)] * self.count_dict.get((x, py), 0) * self.count_dict.get((px,y), 0)
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)