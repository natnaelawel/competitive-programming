from collections import defaultdict
from heapq import heappop, heappush, heappushpop

class AllOne:
    def __init__(self):
        self.valid_mp = defaultdict(int)        
        self.min_heap, self.max_heap = [], []
    def inc(self, key: str) -> None:
        self.valid_mp[key] += 1
        new_val = self.valid_mp[key]
        heappush(self.min_heap, (new_val, key))
        heappush(self.max_heap, (-new_val, key))

    def dec(self, key: str) -> None:
        self.valid_mp[key] -= 1
        if self.valid_mp[key] == 0:
            del self.valid_mp[key]
            return
        heappush(self.min_heap, (self.valid_mp[key], key))
        heappush(self.max_heap, (-self.valid_mp[key], key))
        
    def getMaxKey(self) -> str:
        if self.max_heap:
            prev_val, prev_key = self.max_heap[0]
            while self.max_heap and (prev_key not in self.valid_mp or prev_val != -self.valid_mp[prev_key]):
                heappop(self.max_heap)
                if self.max_heap:
                    prev_val, prev_key = self.max_heap[0]

        return self.max_heap[0][1] if self.max_heap else ""
    
    def getMinKey(self) -> str:
        if self.min_heap:
            prev_val, prev_key = self.min_heap[0]
            while self.min_heap and (prev_key not in self.valid_mp or prev_val != self.valid_mp[prev_key]):
                heappop(self.min_heap)
                if self.min_heap:
                    prev_val, prev_key = self.min_heap[0]
        return self.min_heap[0][1] if self.min_heap else ""

# # Your AllOne object will be instantiated and called as such:
# # obj = AllOne()
# # obj.inc(key)
# # obj.dec(key)
# # param_3 = obj.getMaxKey()
# # param_4 = obj.getMinKey()