# merging takes log n because merge step double the list 
# it takes n because must look at every item
# so it takes 0(nlogn)

from typing import List

class Sorting(object):
    def __init__(self, items: List[int]):
        self.items = items

    def merge_sort(self, first, mid, last):
        self._merge_sort(first, mid,last)

    def _merge_sort(self, first, last):
        if first < last:
            mid = (first + last) // 2
            self._merge_sort(first, mid)
            self._merge_sort(mid + 1, last)
            self.merge_sort( first, mid, last)

nums = [3, 5,1, 6,4, 7,3]
sorting = Sorting(nums)

print(sorting.merge_sort(0, (0 + len(nums))// 2), len(nums))