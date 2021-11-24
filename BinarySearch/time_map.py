from collections import defaultdict 
class TimeMap: 
    def __init__(self) -> None:
        self.store = defaultdict(list)
        
    def set(self, key:str, value: str, timestamp: int)-> None: 
        self.store[key].append([value, timestamp])
        
     
    def get(self, key:str, timestamp: int)-> str: 
        l = 0 
        r = len(self.store[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if self.store[key][mid][1] == timestamp: 
                return self.store[key][mid][0]
                  
            elif self.store[key][mid][1] < timestamp: 
                res = self.store[key][mid][0]
                l = mid + 1
            
            
        return res
# [[1, 5, 4, 0]]
sol = TimeMap()
