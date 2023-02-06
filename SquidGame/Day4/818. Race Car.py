from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        if target == 0:
            return 0
        
        queue = deque([(0, 1)])
        visited = set([(0, 1)])
        count = 0
        while queue:
            count += 1
            size = len(queue)
            for _ in range(size):
                pos, speed = queue.popleft()
                p1, sp1 = pos + speed, speed * 2
                
                if p1 == target:
                    return count
                p2 = pos 
                if speed > 0:
                    sp2 = -1
                else:
                    sp2 = 1
                queue.append((p1, sp1))
                if (p2, sp2) not in visited:
                    visited.add((p2, sp2))
                    queue.append((p2, sp2))
            
        return -1
                    