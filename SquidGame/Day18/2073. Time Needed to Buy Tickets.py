class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        r = 0
        i = 0
        while True:
            if tickets[k] == 0:
                return i
            if tickets[r] == 0:
                pass 
            else:
                i += 1
                tickets[r] -= 1
            r += 1
            r %= len(tickets)
            
        